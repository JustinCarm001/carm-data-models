"""
Tool Data Models
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime


class Tool(BaseModel):
    """Tool model"""
    id: int = Field(..., description="Tool ID")
    name: str = Field(..., description="Tool name")
    slug: str = Field(..., description="Tool slug")
    description: str = Field(..., description="Tool description")
    is_active: bool = Field(True, description="Is tool active")


class ToolSettings(BaseModel):
    """Tool-specific settings for a user"""
    tool_id: int = Field(..., description="Tool ID")
    user_id: int = Field(..., description="User ID")
    settings: Dict[str, Any] = Field(default_factory=dict, description="Tool settings")
    is_enabled: bool = Field(True, description="Is tool enabled for this user")


class ToolExecution(BaseModel):
    """Record of a tool execution"""
    tool_id: int = Field(..., description="Tool ID")
    user_id: int = Field(..., description="User ID")
    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = Field(None)
    status: str = Field(..., description="Execution status")
    input_data: Optional[Dict[str, Any]] = Field(None)
    output_data: Optional[Dict[str, Any]] = Field(None)
    error_message: Optional[str] = Field(None)
