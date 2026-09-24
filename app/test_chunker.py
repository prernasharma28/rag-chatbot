from services.document_loader import extract_text_from_pdf
from services.chunker import create_chunks


pdf_path = "data/documents/company_policy.pdf"

text = extract_text_from_pdf(pdf_path)

chunks = create_chunks(
    text,
    chunk_size=500,
    overlap=50
)

print(f"Total chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)