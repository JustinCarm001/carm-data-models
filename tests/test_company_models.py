import pytest
from pydantic import ValidationError

from carm_data_models.company import Address, ContactInfo, Company, CompanyProfile


def test_address_and_contactinfo_validation():
    a = Address(street="123", city="X", state="Y", country="CA", postal_code="A1B2C3")
    assert a.city == "X"

    c = ContactInfo(email="user@example.com", website="https://example.com")
    assert c.email == "user@example.com"

    with pytest.raises(ValidationError):
        ContactInfo(email="not-an-email")


def test_company_and_profile_nested_models():
    company = Company(name="Acme", website="https://acme.com")
    assert company.name == "Acme"

    profile = CompanyProfile(company=company, tagline="We build stuff")
    assert profile.company.name == "Acme"

