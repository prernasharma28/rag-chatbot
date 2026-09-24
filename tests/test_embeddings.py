from app.services.embeddings import create_embeddings


def test_create_embeddings():
    texts = [
        "How many annual leave days do I get?",
        "Employees receive 20 annual leave days per year."
    ]

    embeddings = create_embeddings(texts)

    assert len(embeddings) == 2
    assert len(embeddings[0]) == 384
    assert len(embeddings[1]) == 384