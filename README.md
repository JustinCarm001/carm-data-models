# carm-data-models

Shared data models for all CarmVisuals services.

## Purpose

This package provides **Pydantic data models** that define the structure of data passed between services. Think of these as blueprints or contracts that ensure all services speak the same language.

## Why Use Data Models?

1. **Type Safety** - Catch errors at development time, not runtime
2. **Validation** - Automatically validate data structure
3. **Documentation** - Models serve as documentation
4. **Consistency** - All services use the same data structures
5. **Serialization** - Easy JSON conversion

## Features

- Pydantic models for all core entities
- Automatic validation
- JSON serialization/deserialization
- Type hints for IDE support
- Clear documentation

## Installation

```bash
# From GitHub (during development)
pip install git+https://github.com/JustinCarm001/carm-data-models.git

# Or locally for development
pip install -e .
```

## Usage

### Company Model

```python
from carm_data_models import Company, ContactInfo

# Create a company object
company = Company(
    name="Tech Startup Inc",
    website="https://techstartup.com",
    industry="Technology",
    description="AI-powered solutions",
    contact_info=ContactInfo(
        email="info@techstartup.com",
        phone="+1-555-0100"
    )
)

# Convert to JSON
company_json = company.model_dump_json()

# Load from JSON
company_from_json = Company.model_validate_json(company_json)

# Access fields with type safety
print(company.name)  # IDE knows this is a string
```

### Email Draft Model

```python
from carm_data_models import EmailDraft, Company

target_company = Company(name="Acme Corp", website="acme.com")

draft = EmailDraft(
    subject="Partnership Opportunity",
    body="Dear Acme team...",
    recipient_email="contact@acme.com",
    recipient_name="John Smith",
    company=target_company,
    personalization_data={
        "pain_point": "scaling challenges",
        "service": "Web Design"
    }
)
```

### Service Request/Response Models

```python
from carm_data_models import ResearchRequest, ResearchResponse, Company

# Research agent request
request = ResearchRequest(
    criteria="tech startups in Toronto",
    max_results=10,
    sources=["web_search", "linkedin"]
)

# Research agent response
response = ResearchResponse(
    companies=[company1, company2, company3],
    total_found=10,
    sources_used=["web_search", "linkedin"],
    duration_seconds=45.2
)
```

## Available Models

### Core Entity Models
- `Company` - Company information
- `ContactInfo` - Contact details
- `User` - User information
- `Tool` - Tool metadata
- `CompanyProfile` - Full company profile with services

### Communication Models
- `EmailDraft` - Draft email structure
- `EmailTemplate` - Email template
- `Message` - Generic message

### Request/Response Models
- `ResearchRequest` / `ResearchResponse` - Research agent
- `ScrapeRequest` / `ScrapeResponse` - Scraper service
- `DraftRequest` / `DraftResponse` - Draft agent
- `OrchestrationRequest` / `OrchestrationResponse` - Orchestrator

### Data Models
- `ScrapedData` - Data from web scraping
- `ResearchResult` - Research findings
- `ServiceMetrics` - Performance metrics

## Development

```bash
# Install in editable mode
cd packages/carm-data-models
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black src/
isort src/
```

## Project Structure

```
carm-data-models/
├── src/carm_data_models/
│   ├── __init__.py
│   ├── company.py          # Company-related models
│   ├── email.py            # Email-related models
│   ├── user.py             # User-related models
│   ├── tool.py             # Tool-related models
│   ├── requests.py         # Service request models
│   ├── responses.py        # Service response models
│   └── common.py           # Common/shared models
├── tests/
├── pyproject.toml
└── README.md
```

## Type Safety Example

```python
from carm_data_models import Company

# This works
company = Company(name="Acme", website="acme.com")

# This raises validation error - missing required field
company = Company(website="acme.com")  # Error: 'name' is required

# This raises validation error - wrong type
company = Company(name=123, website="acme.com")  # Error: 'name' must be string
```
