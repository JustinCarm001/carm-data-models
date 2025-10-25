"""
Email Data Models

PSEUDO CODE:
------------
1. Define EmailDraft model for draft emails
2. Define EmailTemplate for reusable templates
3. Define Message for generic messages
4. Add validation for email addresses
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from .company import Company


class EmailDraft(BaseModel):
    """
    Email draft model
    
    PSEUDO CODE:
    1. Store email content (subject, body)
    2. Store recipient information
    3. Store target company data
    4. Store personalization data used
    5. Store metadata (created time, agent, etc.)
    
    This is what the draft-agent returns after creating
    a personalized outreach email.
    """
    # Email content
    subject: str = Field(..., description="Email subject line", min_length=1)
    body: str = Field(..., description="Email body content", min_length=1)
    preview_text: Optional[str] = Field(None, description="Preview text (for email clients)")
    
    # Recipient info
    recipient_email: EmailStr = Field(..., description="Recipient email address")
    recipient_name: Optional[str] = Field(None, description="Recipient name")
    
    # Company context
    company: Company = Field(..., description="Target company")
    
    # Personalization
    personalization_data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Data used for personalization"
    )
    
    # Template info
    template_name: Optional[str] = Field(None, description="Template used")
    tone: Optional[str] = Field(None, description="Tone used (professional, casual, etc.)")
    
    # Metadata
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Creation time")
    created_by: Optional[str] = Field(None, description="Service/agent that created this")
    version: Optional[int] = Field(1, description="Draft version number")
    
    # Status
    is_approved: Optional[bool] = Field(False, description="Has user approved this draft?")
    is_sent: Optional[bool] = Field(False, description="Has this been sent?")
    sent_at: Optional[datetime] = Field(None, description="When was it sent?")
    
    class Config:
        json_schema_extra = {
            "example": {
                "subject": "Partnership Opportunity for Tech Innovations Inc",
                "body": "Hi John,\n\nI noticed your company...",
                "preview_text": "Quick question about your web presence",
                "recipient_email": "john@techinnovations.com",
                "recipient_name": "John Smith",
                "company": {
                    "name": "Tech Innovations Inc",
                    "website": "https://techinnovations.com"
                },
                "personalization_data": {
                    "pain_point": "outdated website",
                    "service": "Web Design"
                },
                "template_name": "professional_outreach",
                "tone": "professional"
            }
        }


class EmailTemplate(BaseModel):
    """
    Reusable email template
    
    PSEUDO CODE:
    1. Store template content with placeholders
    2. Store template metadata (name, description)
    3. Define required and optional variables
    4. Store usage instructions
    
    Templates use placeholders like {company_name}, {service}, etc.
    Draft agent fills these in with actual data.
    """
    # Template identification
    name: str = Field(..., description="Template name", min_length=1)
    description: Optional[str] = Field(None, description="Template description")
    category: Optional[str] = Field(None, description="Template category (outreach, follow-up, etc.)")
    
    # Template content
    subject_template: str = Field(..., description="Subject line template with placeholders")
    body_template: str = Field(..., description="Email body template with placeholders")
    preview_text_template: Optional[str] = Field(None, description="Preview text template")
    
    # Template variables
    required_variables: List[str] = Field(..., description="Required placeholder variables")
    optional_variables: Optional[List[str]] = Field(default=None, description="Optional variables")
    
    # Template settings
    tone: Optional[str] = Field("professional", description="Default tone")
    length: Optional[str] = Field("medium", description="Target length (short, medium, long)")
    
    # Metadata
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    usage_count: Optional[int] = Field(0, description="How many times used")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "professional_outreach",
                "description": "Professional cold outreach template",
                "category": "outreach",
                "subject_template": "Partnership Opportunity for {company_name}",
                "body_template": "Hi {recipient_name},\n\nI noticed {company_name}...",
                "required_variables": ["company_name", "recipient_name"],
                "optional_variables": ["pain_point", "service"],
                "tone": "professional",
                "length": "medium"
            }
        }


class Message(BaseModel):
    """
    Generic message model
    
    Used for any text-based communication or response
    """
    content: str = Field(..., description="Message content")
    sender: Optional[str] = Field(None, description="Message sender")
    recipient: Optional[str] = Field(None, description="Message recipient")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Message timestamp")
    message_type: Optional[str] = Field(None, description="Message type (email, sms, notification)")
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata")
    
    class Config:
        json_schema_extra = {
            "example": {
                "content": "Email draft has been created",
                "sender": "draft-agent",
                "recipient": "user-123",
                "message_type": "notification"
            }
        }
