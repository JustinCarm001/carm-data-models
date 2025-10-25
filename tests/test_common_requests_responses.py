from datetime import datetime

from carm_data_models.common import Status, ServiceMetrics, ErrorResponse
from carm_data_models.company import Company
from carm_data_models.email import EmailDraft
from carm_data_models.requests import ResearchRequest, ScrapeRequest, DraftRequest, OrchestrationRequest
from carm_data_models.responses import ResearchResponse, ScrapeResponse, DraftResponse, OrchestrationResponse


def test_status_enum_and_metrics_error_models():
    assert Status.PENDING.value == "pending"
    m = ServiceMetrics(duration_seconds=1.2)
    assert m.duration_seconds == 1.2
    e = ErrorResponse(error="boom")
    assert e.error == "boom" and isinstance(e.timestamp, datetime)


def test_request_models_constraints():
    r = ResearchRequest(criteria="web", max_results=5)
    assert r.max_results == 5

    s = ScrapeRequest(companies=[{"name": "A"}], sources=["website"]) 
    assert s.timeout_seconds == 30

    d = DraftRequest(companies=[{"name": "A"}], sender_company={"name": "Carm Visuals"})
    assert d.tone == "professional"

    o = OrchestrationRequest(task_type="research_and_draft", criteria="x", max_companies=3, sender_company_id=1, user_id=2)
    assert o.max_companies == 3


def test_response_models_nested_types():
    c = Company(name="Acme")
    rr = ResearchResponse(companies=[c], total_found=1, sources_used=["web"], duration_seconds=0.1, metrics=None)
    assert rr.total_found == 1

    sr = ScrapeResponse(scraped_data=[{"name": "Acme"}], successful_scrapes=1, failed_scrapes=0, duration_seconds=0.2, metrics=None)
    assert sr.successful_scrapes == 1

    draft = EmailDraft(subject="s", body="b", recipient_email="x@y.com", company=c)
    dr = DraftResponse(drafts=[draft], total_generated=1, duration_seconds=0.3, metrics=None)
    assert dr.total_generated == 1

    orr = OrchestrationResponse(task_id="t1", status="pending", total_duration_seconds=1.2)
    assert orr.status == "pending"

