"""
User Data Models
"""

from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class User(BaseModel):
    """User model"""
    id: int = Field(..., description="User ID")
    username: str = Field(..., description="Username")
    email: EmailStr = Field(..., description="Email address")
    full_name: Optional[str] = Field(None, description="Full name")
    is_active: bool = Field(True, description="Is user active")
    created_at: datetime = Field(default_factory=datetime.utcnow)


class UserProfile(BaseModel):
    """Extended user profile"""
    user: User = Field(..., description="Base user info")
    company_id: Optional[int] = Field(None, description="Associated company ID")
    role: Optional[str] = Field(None, description="User role")
    permissions: Optional[List[str]] = Field(default=None, description="User permissions")
    preferences: Optional[dict] = Field(default=None, description="User preferences")
