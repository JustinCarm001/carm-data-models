"""
Common/Shared Data Models
"""

from typing import Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    """Status enumeration"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class ServiceMetrics(BaseModel):
    """
    Service performance metrics
    
    Track duration, token usage, costs, etc.
    """
    duration_seconds: float = Field(..., description="Operation duration")
    tokens_used: Optional[int] = Field(None, description="LLM tokens used")
    estimated_cost: Optional[float] = Field(None, description="Estimated cost in USD")
    requests_made: Optional[int] = Field(None, description="Number of API requests")
    cache_hits: Optional[int] = Field(None, description="Number of cache hits")
    cache_misses: Optional[int] = Field(None, description="Number of cache misses")
    
    class Config:
        json_schema_extra = {
            "example": {
                "duration_seconds": 45.2,
                "tokens_used": 1500,
                "estimated_cost": 0.015,
                "requests_made": 3,
                "cache_hits": 1,
                "cache_misses": 2
            }
        }


class ErrorResponse(BaseModel):
    """
    Standard error response
    """
    error: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(None, description="Error code")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Error timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "error": "Failed to connect to LLM service",
                "error_code": "LLM_CONNECTION_ERROR",
                "details": {"service": "azure-openai", "endpoint": "..."},
                "timestamp": "2024-01-15T10:30:00Z"
            }
        }
