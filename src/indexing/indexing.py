from elasticsearch import Elasticsearch

class Indexing:
    def __init__(self, index_name, es_host="http://localhost:9200"):
        self.es = Elasticsearch(hosts=[es_host])
        self.index_name = index_name

    def create_index(self):
        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name)

    def index_documents(self, documents):
        for doc in documents:
            self.es.index(index=self.index_name, id=doc["document_id"], body=doc)

    def search_documents(self, query, numeric_filters=None):
        body = {
            "query": {
                "bool": {
                    "must": {"match": {"content": query}},
                    "filter": [
                        {"range": {"key_metrics.revenue": {"gte": numeric_filters.get("revenue", 0)}}} if numeric_filters else {}
                    ]
                }
            }
        }
        return self.es.search(index=self.index_name, body=body)