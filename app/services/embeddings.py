from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embeddings(texts: list[str]):
    embeddings = model.encode(texts)

    return embeddings