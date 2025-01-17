from pydantic import BaseModel, Field


class QueryRequest(BaseModel):
    query: str

class NumericQueryRequest(BaseModel):
    query: str
    numeric_filter: dict = {}