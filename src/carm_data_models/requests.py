"""
Service Request Models
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    """Request to research agent"""
    criteria: str = Field(..., description="Search criteria", min_length=1)
    max_results: int = Field(10, description="Maximum number of companies", ge=1, le=100)
    sources: Optional[List[str]] = Field(default=None, description="Sources to use")
    filters: Optional[Dict[str, Any]] = Field(default=None, description="Additional filters")


class ScrapeRequest(BaseModel):
    """Request to scraper service"""
    companies: List[Dict[str, str]] = Field(..., description="Companies to scrape")
    sources: List[str] = Field(..., description="Sources to scrape (website, linkedin, etc.)")
    timeout_seconds: Optional[int] = Field(30, description="Timeout per company")


class DraftRequest(BaseModel):
    """Request to draft agent"""
    companies: List[Dict[str, Any]] = Field(..., description="Target companies with data")
    sender_company: Dict[str, Any] = Field(..., description="Sender company profile")
    template_name: Optional[str] = Field(None, description="Template to use")
    tone: Optional[str] = Field("professional", description="Email tone")
    personalization_level: Optional[str] = Field("high", description="Personalization level")


class OrchestrationRequest(BaseModel):
    """Request to orchestrator"""
    task_type: str = Field(..., description="Type of task (e.g., 'research_and_draft')")
    criteria: str = Field(..., description="Research criteria")
    max_companies: int = Field(10, ge=1, le=100)
    sender_company_id: int = Field(..., description="Sender company ID")
    user_id: int = Field(..., description="User ID")
    options: Optional[Dict[str, Any]] = Field(default=None, description="Additional options")
