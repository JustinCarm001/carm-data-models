"""
Service Response Models
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from .company import Company
from .email import EmailDraft
from .common import ServiceMetrics


class ResearchResponse(BaseModel):
    """Response from research agent"""
    companies: List[Company] = Field(..., description="Found companies")
    total_found: int = Field(..., description="Total companies found")
    sources_used: List[str] = Field(..., description="Sources that were used")
    duration_seconds: float = Field(..., description="How long research took")
    metrics: Optional[ServiceMetrics] = Field(None, description="Service metrics")


class ScrapeResponse(BaseModel):
    """Response from scraper service"""
    scraped_data: List[Dict[str, Any]] = Field(..., description="Scraped company data")
    successful_scrapes: int = Field(..., description="Number of successful scrapes")
    failed_scrapes: int = Field(..., description="Number of failed scrapes")
    duration_seconds: float = Field(..., description="How long scraping took")
    metrics: Optional[ServiceMetrics] = Field(None, description="Service metrics")


class DraftResponse(BaseModel):
    """Response from draft agent"""
    drafts: List[EmailDraft] = Field(..., description="Generated email drafts")
    total_generated: int = Field(..., description="Total drafts generated")
    template_used: Optional[str] = Field(None, description="Template that was used")
    duration_seconds: float = Field(..., description="How long drafting took")
    metrics: Optional[ServiceMetrics] = Field(None, description="Service metrics")


class OrchestrationResponse(BaseModel):
    """Response from orchestrator"""
    task_id: str = Field(..., description="Unique task ID")
    status: str = Field(..., description="Task status")
    research_results: Optional[List[Company]] = Field(None, description="Research results")
    scraped_data: Optional[List[Dict[str, Any]]] = Field(None, description="Scraped data")
    drafts: Optional[List[EmailDraft]] = Field(None, description="Email drafts")
    total_duration_seconds: float = Field(..., description="Total workflow duration")
    step_durations: Optional[Dict[str, float]] = Field(None, description="Duration per step")
    errors: Optional[List[str]] = Field(None, description="Any errors encountered")
