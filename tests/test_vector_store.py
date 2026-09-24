from app.services.embeddings import create_embeddings
from app.services.vector_store import create_index, search_index


def test_faiss_search():
    texts = [
        "Employees receive 20 annual leave days per year.",
        "Employees receive 10 sick leave days per year.",
        "Employees can work from home up to 2 days per week.",
    ]

    embeddings = create_embeddings(texts)

    index = create_index(embeddings)

    query = "How many annual leave days do I get?"

    query_embedding = create_embeddings([query])[0]

    distances, indices = search_index(
        index,
        query_embedding,
        top_k=2
    )

    assert len(indices[0]) == 2
    assert indices[0][0] == 0   