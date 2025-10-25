"""
Company Data Models

PSEUDO CODE:
------------
1. Define Company model with all relevant fields
2. Define ContactInfo for contact details
3. Define Address for location
4. Define CompanyProfile for full company data
5. Add validation for URLs, emails, etc.
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, HttpUrl, EmailStr
from datetime import datetime


class Address(BaseModel):
    """
    Physical address
    
    Used for company locations
    """
    street: Optional[str] = Field(None, description="Street address")
    city: Optional[str] = Field(None, description="City")
    state: Optional[str] = Field(None, description="State/Province")
    country: Optional[str] = Field(None, description="Country")
    postal_code: Optional[str] = Field(None, description="Postal/ZIP code")
    
    class Config:
        json_schema_extra = {
            "example": {
                "street": "123 Main St",
                "city": "Toronto",
                "state": "ON",
                "country": "Canada",
                "postal_code": "M5H 2N2"
            }
        }


class ContactInfo(BaseModel):
    """
    Contact information for a company or person
    
    PSEUDO CODE:
    1. Store email (validated format)
    2. Store phone number
    3. Store social media links
    4. All fields optional since we may not have all info
    """
    email: Optional[EmailStr] = Field(None, description="Contact email")
    phone: Optional[str] = Field(None, description="Phone number")
    website: Optional[HttpUrl] = Field(None, description="Website URL")
    linkedin: Optional[HttpUrl] = Field(None, description="LinkedIn URL")
    instagram: Optional[HttpUrl] = Field(None, description="Instagram URL")
    twitter: Optional[HttpUrl] = Field(None, description="Twitter/X URL")
    
    class Config:
        json_schema_extra = {
            "example": {
                "email": "contact@example.com",
                "phone": "+1-555-0100",
                "website": "https://example.com",
                "linkedin": "https://linkedin.com/company/example"
            }
        }


class Company(BaseModel):
    """
    Company entity model
    
    PSEUDO CODE:
    1. Store basic company info (name, website, industry)
    2. Store optional detailed info (description, size, revenue)
    3. Store contact information
    4. Store location
    5. Store metadata (when found, source, etc.)
    
    This model is used for:
    - Target companies found by research agent
    - Your company profile (Carm Visuals)
    - Any company data passed between services
    """
    # Required fields
    name: str = Field(..., description="Company name", min_length=1)
    
    # Basic info
    website: Optional[HttpUrl] = Field(None, description="Company website")
    industry: Optional[str] = Field(None, description="Industry/sector")
    description: Optional[str] = Field(None, description="Company description")
    
    # Size and revenue
    employee_count: Optional[int] = Field(None, description="Number of employees", ge=0)
    revenue: Optional[str] = Field(None, description="Annual revenue (e.g., '$1M-$5M')")
    founded_year: Optional[int] = Field(None, description="Year founded", ge=1800, le=2100)
    
    # Contact and location
    contact_info: Optional[ContactInfo] = Field(None, description="Contact information")
    address: Optional[Address] = Field(None, description="Physical address")
    
    # Additional data
    services: Optional[List[str]] = Field(default=None, description="Services offered")
    technologies: Optional[List[str]] = Field(default=None, description="Technologies used")
    pain_points: Optional[List[str]] = Field(default=None, description="Identified pain points")
    
    # Metadata
    source: Optional[str] = Field(None, description="Where this data came from")
    found_at: Optional[datetime] = Field(None, description="When this data was found")
    confidence_score: Optional[float] = Field(None, description="Data confidence (0-1)", ge=0, le=1)
    metadata: Optional[Dict[str, Any]] = Field(default=None, description="Additional metadata")
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Tech Innovations Inc",
                "website": "https://techinnovations.com",
                "industry": "Technology",
                "description": "AI-powered solutions for businesses",
                "employee_count": 50,
                "revenue": "$5M-$10M",
                "founded_year": 2018,
                "contact_info": {
                    "email": "info@techinnovations.com",
                    "phone": "+1-555-0100"
                },
                "services": ["Web Development", "AI Consulting"],
                "source": "research-agent",
                "confidence_score": 0.95
            }
        }


class CompanyProfile(BaseModel):
    """
    Full company profile with detailed information
    
    PSEUDO CODE:
    1. Extend Company model
    2. Add mission, vision, values
    3. Add team information
    4. Add portfolio/examples
    5. Add differentiators
    
    This is used for YOUR company (Carm Visuals) to store:
    - Your services
    - Your mission/values
    - Your team
    - Your differentiators
    
    This data is loaded from settings and used by draft agent
    to personalize outreach emails FROM you.
    """
    # Basic company info
    company: Company = Field(..., description="Basic company information")
    
    # Brand messaging
    tagline: Optional[str] = Field(None, description="Company tagline")
    mission: Optional[str] = Field(None, description="Mission statement")
    vision: Optional[str] = Field(None, description="Vision statement")
    values: Optional[List[str]] = Field(default=None, description="Core values")
    
    # Offerings
    services_detailed: Optional[List[Dict[str, str]]] = Field(
        default=None,
        description="Detailed services with descriptions"
    )
    portfolio_examples: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="Portfolio examples with details"
    )
    
    # Differentiators
    unique_selling_points: Optional[List[str]] = Field(
        default=None,
        description="What makes you unique"
    )
    certifications: Optional[List[str]] = Field(default=None, description="Certifications")
    awards: Optional[List[str]] = Field(default=None, description="Awards received")
    
    # Team
    team_members: Optional[List[Dict[str, str]]] = Field(
        default=None,
        description="Team members with roles"
    )
    
    # Social proof
    client_testimonials: Optional[List[Dict[str, str]]] = Field(
        default=None,
        description="Client testimonials"
    )
    case_studies: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="Case studies"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "company": {
                    "name": "Carm Visuals",
                    "website": "https://carmvisuals.com",
                    "industry": "Design & Marketing"
                },
                "tagline": "Bringing your vision to life",
                "mission": "To help businesses succeed through exceptional design",
                "values": ["Quality", "Innovation", "Client-First"],
                "services_detailed": [
                    {
                        "name": "Web Design",
                        "description": "Custom, responsive websites"
                    }
                ],
                "unique_selling_points": [
                    "10+ years experience",
                    "100% satisfaction guarantee"
                ],
                "team_members": [
                    {
                        "name": "Justin",
                        "role": "Founder & Lead Designer"
                    }
                ]
            }
        }
