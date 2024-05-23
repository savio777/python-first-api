from typing import List
from uuid import UUID
from datetime import datetime


class User:
    idpublic: UUID
    name: str
    email: str
    years: int
    createdAt: datetime
    updatedAt: datetime


class ResponseListAll:
    data: List[User]
    page: int
    pages: int
    count: int


class QueryParamsListAll:
    name: str
    email: str
    years: int
    page: int
