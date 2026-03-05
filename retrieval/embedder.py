from sentence_transformers import SentenceTransformer
import numpy as np

# Load model once (global, avoids reloading in every function call)
try:
    model = SentenceTransformer("BAAI/bge-small-en-v1.5")
except Exception as e:
    model = None
    print(f"Embedding model loading failed: {e}")


def create_embeddings(text_chunks):
    """
    Create embeddings for list of text chunks.
    Returns numpy array of embeddings.
    """

    if model is None:
        raise RuntimeError("Embedding model is not loaded properly.")

    if not text_chunks:
        return np.array([])

    try:
        embeddings = model.encode(
            text_chunks,
            convert_to_numpy=True,
            normalize_embeddings=True
        )
        return embeddings

    except Exception as e:
        raise RuntimeError(f"Embedding creation failed: {str(e)}")