from backend.db.dal.base import AsyncPostgreSQLDAL
from backend.db.data_models import Assets, Jobs, Pages, PagesAssetsRel, Photobooks
from backend.db.schemas import (
    AssetsCreate,
    AssetsUpdate,
    JobsCreate,
    JobsUpdate,
    PagesAssetsRelCreate,
    PagesAssetsRelUpdate,
    PagesCreate,
    PagesUpdate,
    PhotobooksCreate,
    PhotobooksUpdate,
)


class AssetsDAL(AsyncPostgreSQLDAL[Assets, AssetsCreate, AssetsUpdate]):
    pass


class JobsDAL(AsyncPostgreSQLDAL[Jobs, JobsCreate, JobsUpdate]):
    pass


class PagesDAL(AsyncPostgreSQLDAL[Pages, PagesCreate, PagesUpdate]):
    pass


class PagesAssetsRelDAL(
    AsyncPostgreSQLDAL[PagesAssetsRel, PagesAssetsRelCreate, PagesAssetsRelUpdate]
):
    pass


class PhotobooksDAL(AsyncPostgreSQLDAL[Photobooks, PhotobooksCreate, PhotobooksUpdate]):
    pass
