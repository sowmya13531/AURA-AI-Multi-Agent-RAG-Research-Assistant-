from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid


class VectorStore:
    def __init__(self, collection_name="aura_collection", dimension=384):
        self.client = QdrantClient(":memory:")
        self.collection_name = collection_name
        self.dimension = dimension

        self._create_collection()

    def _create_collection(self):
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=self.dimension,
                distance=Distance.COSINE,
            ),
        )

    def add_embeddings(self, embeddings, chunks):
        points = []

        for vector, chunk in zip(embeddings, chunks):
            points.append(
                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=vector.tolist(),
                    payload={"text": chunk},
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def search(self, query_embedding, top_k=5):

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_embedding.tolist(),
            limit=top_k,
        )

        return [point.payload["text"] for point in results.points]