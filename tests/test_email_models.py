from datetime import datetime, timedelta
import pytest
from pydantic import ValidationError

from carm_data_models.company import Company
from carm_data_models.email import EmailDraft, EmailTemplate, Message


def test_email_draft_requires_fields_and_sets_defaults():
    comp = Company(name="Acme")
    draft = EmailDraft(
        subject="Hello",
        body="Body",
        recipient_email="to@example.com",
        company=comp,
    )
    assert draft.recipient_email == "to@example.com"
    assert isinstance(draft.created_at, datetime)

    with pytest.raises(ValidationError):
        EmailDraft(subject="s", body="b", recipient_email="bad", company=comp)


def test_email_template_and_message_defaults():
    t = EmailTemplate(
        name="tmpl",
        subject_template="Hi {name}",
        body_template="Body for {name}",
        required_variables=["name"],
    )
    assert t.tone == "professional"
    assert t.usage_count == 0

    m = Message(content="ok")
    assert isinstance(m.timestamp, datetime)

