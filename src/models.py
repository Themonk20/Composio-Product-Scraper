from typing import List
from pydantic import BaseModel, Field


class AppResearch(BaseModel):
    name: str = Field(description="Application name")

    category: str = Field(description="Application category")

    description: str = Field(description="One line description")

    auth_methods: List[str] = Field(description="Authentication methods")

    self_serve: str = Field(description="Yes / No / Partial")

    api_type: str = Field(description="REST, GraphQL, SOAP, etc")

    api_scope: str = Field(description="Small, Medium, Broad")

    mcp_available: bool

    buildable: bool

    blocker: str

    evidence: List[str]

    toolkit_priority: str
    
    integration_difficulty: str