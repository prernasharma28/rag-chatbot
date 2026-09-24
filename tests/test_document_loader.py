from app.services.document_loader import extract_text_from_pdf


def test_extract_text_from_pdf():
    pdf_path = "data/documents/company_policy.pdf"

    text = extract_text_from_pdf(pdf_path)

    assert text
    assert "Annual Leave" in text
    assert "20 days" in text