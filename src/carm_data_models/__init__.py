"""
carm-data-models: Shared data models for CarmVisuals services
"""

# Company models
from .company import Company, ContactInfo, CompanyProfile, Address

# Email models
from .email import EmailDraft, EmailTemplate, Message

# User models
from .user import User, UserProfile

# Tool models
from .tool import Tool, ToolSettings, ToolExecution

# Request models
from .requests import (
    ResearchRequest,
    ScrapeRequest,
    DraftRequest,
    OrchestrationRequest,
)

# Response models
from .responses import (
    ResearchResponse,
    ScrapeResponse,
    DraftResponse,
    OrchestrationResponse,
)

# Common models
from .common import ServiceMetrics, ErrorResponse, Status

__version__ = "0.1.0"

__all__ = [
    # Company
    "Company",
    "ContactInfo",
    "CompanyProfile",
    "Address",
    # Email
    "EmailDraft",
    "EmailTemplate",
    "Message",
    # User
    "User",
    "UserProfile",
    # Tool
    "Tool",
    "ToolSettings",
    "ToolExecution",
    # Requests
    "ResearchRequest",
    "ScrapeRequest",
    "DraftRequest",
    "OrchestrationRequest",
    # Responses
    "ResearchResponse",
    "ScrapeResponse",
    "DraftResponse",
    "OrchestrationResponse",
    # Common
    "ServiceMetrics",
    "ErrorResponse",
    "Status",
]
