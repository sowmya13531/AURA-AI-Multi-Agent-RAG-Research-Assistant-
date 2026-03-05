from retrieval.embedder import create_embeddings


def retrieve_context(query: str, vector_store, top_k: int = 5) -> str:
    """
    Retrieve relevant context from vector store using query.
    """

    if not query.strip():
        return "⚠️ Empty query provided."

    # Create embedding for query
    query_embedding = create_embeddings([query])

    if query_embedding.size == 0:
        return "⚠️ Failed to generate query embedding."

    # Search vector store
    results = vector_store.search(query_embedding[0], top_k=top_k)

    if not results:
        return "⚠️ No relevant context found."

    return "\n\n".join(results)