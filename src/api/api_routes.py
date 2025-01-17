import os

from fastapi import FastAPI, HTTPException

from src.models import QueryRequest, NumericQueryRequest
from src.pipeline import DataIngestion
from src.indexing import Indexing
from src.rag import RAGPipeline
from src.ranking import AnswerScoring

app = FastAPI()

data_ingestion = DataIngestion(json_file_path=os.path.join(os.getcwd(), "data", "Dataset.json"))
data_ingestion.load_data()
data_ingestion.preprocess_data()
documents = data_ingestion.get_data()

indexing = Indexing(index_name="company_reports", es_host="http://10.10.1.3:9200")
indexing.create_index()
indexing.index_documents(documents)

rag_pipeline = RAGPipeline()
answer_scoring = AnswerScoring()

@app.post("/query")
async def query(request: QueryRequest):
    search_results = indexing.search_documents(request.query)
    context = "\n".join([doc["_source"]["content"] for doc in search_results["hits"]["hits"]])
    if not context:
        raise HTTPException(status_code=404, detail="No documents found for the query")
    answer = rag_pipeline.generate_answer(context, request.query)
    return {"answer": answer}

@app.post("/numeric-query")
async def numeric_query(request: NumericQueryRequest):
    search_results = indexing.search_documents(request.query, request.numeric_filter)
    if not search_results["hits"]["hits"]:
        raise HTTPException(status_code=404, detail="No documents found matching the criteria")
    return search_results

@app.get("/health-check")
async def health_check():
    return {"status": "Service is running"}

