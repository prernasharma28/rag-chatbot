from services.document_loader import extract_text_from_pdf


pdf_path = "data/documents/company_policy.pdf"

text = extract_text_from_pdf(pdf_path)

print(text)