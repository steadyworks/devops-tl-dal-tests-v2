from typing import Generic, Optional, Type, TypeVar
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel

ModelType = TypeVar("ModelType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class AsyncPostgreSQLDAL(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    IMMUTABLE_FIELDS = {"id", "created_at"}

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, session: AsyncSession, id: UUID) -> Optional[ModelType]:
        return await session.get(self.model, id)

    async def create(
        self,
        session: AsyncSession,
        obj_in: CreateSchemaType,
    ) -> ModelType:
        obj = self.model.model_validate(obj_in)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def update(
        self,
        session: AsyncSession,
        db_obj: ModelType,
        obj_in: UpdateSchemaType,
    ) -> ModelType:
        update_data = obj_in.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            if field not in self.IMMUTABLE_FIELDS and hasattr(db_obj, field):
                setattr(db_obj, field, value)

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update_by_id(
        self,
        session: AsyncSession,
        id: UUID,
        obj_in: UpdateSchemaType,
    ) -> Optional[ModelType]:
        db_obj = await self.get(session, id)
        if not db_obj:
            return None
        return await self.update(session, db_obj, obj_in)
