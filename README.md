# Project Architecture and Configuration Guide

## Architecture Overview
The project is designed to process, index, and query a dataset of company reports using a modular and scalable architecture. Below is an overview of the architecture:

### Project Structure
```
project_root/
|-- data
    |-- Datasert.json
|-- src
    |-- api
        |-- __init__.py
        |-- api_routes.py
    |-- pipeline
        |-- __init__.py
        |-- data_ingestion.py
    |-- indexing
        |-- __init__.py
        |-- indexing.py
    |-- rag
        |-- __init__.py
        |-- rag_pipeline.py
    |-- ranking
        |-- __init__.py
        |-- answer_ranking.py
|-- main.py
|-- requirements.txt
|-- README.md
```

### Core Modules

1. **Data Preparation and Ingestion (`data_ingestion.py`)**
   - **Responsibilities**:
     - Load JSON data.
     - Clean and preprocess numerical and textual data.
     - Extract key numerical features (e.g., revenue, profit).
   - **Key Classes**: `DataIngestion`

2. **Document Indexing and Retrieval (`indexing.py`)**
   - **Responsibilities**:
     - Index documents using Elasticsearch.
     - Perform semantic and keyword-based searches.
     - Apply numerical filters for queries.
   - **Key Classes**: `Indexing`

3. **Retrieval-Augmented Generation (RAG) Pipeline (`rag_pipeline.py`)**
   - **Responsibilities**:
     - Use a pre-trained LLM to generate answers based on retrieved documents.
     - Combine semantic context with user queries for coherent responses.
   - **Key Classes**: `RAGPipeline`

4. **Answer Scoring and Ranking (`answer_ranking.py`)**
   - **Responsibilities**:
     - Rank generated answers based on relevance and numerical accuracy.
     - Implement custom scoring algorithms for better results.
   - **Key Classes**: `AnswerScoring`

5. **API Layer (`api.py`)**
   - **Responsibilities**:
     - Provide REST API endpoints for querying the system.
     - Support query and numeric query functionalities.
     - Expose a health-check endpoint.
   - **Framework**: FastAPI


## Configuration Guide

### 1. Prerequisites
- Python 3.10+
- ElasticSearch Server configured

### 2. Install Python Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Verify Elasticsearch Setup
Test if Elasticsearch is running:
```bash
curl http://HOST_IP:PORT
```
You should see a response with cluster information.

### 4. Configure and Run the Application

#### 4.1. Initialize the Dataset
Ensure your dataset is in the `dataset.json` file and structured as follows:
```json
[
  {
    "document_id": "doc_9988",
    "title": "Sample Title",
    "company": "Company Name",
    "date": "2024-02-26",
    "topics": ["finance", "strategy"],
    "content": "...",
    "conclusion": "..."
  }
]
```

#### 4.2. Start the Application
Run the application using the CLI:
```bash
python main.py --host 0.0.0.0 --port 8000
```

#### 4.3. Access the API
- Test Endpoints:
  - `/query`: Accepts a query and retrieves relevant answers.
  - `/numeric-query`: Supports queries with numerical filters.
  - `/health-check`: Checks the service status.

### 5. Testing the Integration
- Verify that the `/health-check` endpoint returns `{"status": "Service is running"}`.
- Test queries using `/query` and `/numeric-query` endpoints via Swagger UI or Postman.

### 6. Optional: Customize Elasticsearch Configuration
- Modify the `index_name` in `indexing.py` as needed.
- Adjust Elasticsearch settings in `docker-compose.yml` for production environments (e.g., enable security).


