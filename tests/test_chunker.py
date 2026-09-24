from app.services.chunker import create_chunks


def test_create_chunks():
    text = "A" * 1200

    chunks = create_chunks(
        text,
        chunk_size=500,
        overlap=50
    )

    assert len(chunks) == 3
    assert len(chunks[0]) == 500
    assert len(chunks[1]) == 500
    assert len(chunks[2]) == 300