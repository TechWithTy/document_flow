from pydantic import BaseModel, Field


class ListParams(BaseModel):
    page: int = Field(1, ge=1)
    page_size: int = Field(50, ge=1, le=200, alias="pageSize")


class ListLoopsParams(ListParams):
    profile_id: str = Field(..., alias="profileId")