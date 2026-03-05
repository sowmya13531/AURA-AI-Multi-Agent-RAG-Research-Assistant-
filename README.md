# 📚 AURA – Multi-Agent Retrieval Augmented Research Assistant

### Autonomous Research Understanding & Report Generation using RAG + Local LLM ollama via Gemma:2-b- Qdrant VectorStore
## 🌟 Project Overview
**AURA (Autonomous Unified Research Assistant)** is a modular multi-agent AI system designed to assist in academic research workflows using Retrieval-Augmented Generation (RAG) and a local Large Language Model (LLM) along with Qdrant vectorstore.

The system allows users to upload research papers (PDF format), semantically analyze their content, and generate structured research outputs including:

* Research planning
* Literature review analysis
* Hypothesis generation
* Experimental ideas
* Full structured research report

AURA integrates document retrieval, vector search, multi-agent reasoning, and local LLM inference Gemma:2-b and Qdrant Vector Store into one cohesive research automation pipeline.


# 🎯 Purpose of the Project

Modern research workflows require:

* Reading large volumes of papers
* Extracting relevant context
* Identifying gaps
* Designing experiments
* Writing structured reports

This process is time-consuming and cognitively demanding.

**AURA was built to automate and structure this workflow using AI.**

The goal is not just answering questions — but performing structured research reasoning through an autonomous multi-agent architecture.

# DEMO
![App Demo](demo_aura/Screenshot%20(240).png)
![App Demo](demo_aura/Screenshot%20(241).png)
![App Demo](demo_aura/Screenshot%20(242).png)
![App Demo](demo_aura/Screenshot%20(243).png)

# 🧠 What Makes AURA Special

Unlike basic chatbot or PDF-QA systems, AURA includes:

### ✅ Multi-Agent Architecture

Instead of a single prompt, the system uses specialized AI agents:

* Planner Agent
* Literature Analysis Agent
* Hypothesis Agent
* Writer Agent

Each agent has a dedicated responsibility.

### ✅ Retrieval-Augmented Generation (RAG)

AURA does not hallucinate blindly.

It:

1. Converts document text into embeddings
2. Stores them in a vector database
3. Retrieves relevant context
4. Generates responses grounded in document content


### ✅ Local LLM Execution(gemma:2-b via Ollama)

* Runs using Ollama
* No external API dependency
* Privacy-friendly
* Fully offline capable

### ✅ Vector Database Integration

Uses Qdrant to:

* Store semantic embeddings
* Perform similarity search
* Retrieve relevant research context

### ✅ Modular Engineering Design

The system is structured into separate components:

* LLM interface
* Embedding layer
* Vector store
* Retrieval pipeline
* Agent modules
* Streamlit interface

This makes it scalable and production-ready.

# 🏗️ System Architecture (Conceptual Flow)

```
bash
PDF Upload
↓
Text Extraction
↓
Text Chunking
↓
Embedding Generation (SentenceTransformers)
↓
Vector Storage (Qdrant)
↓
User Question
↓
Context Retrieval (Semantic Search)
↓
Planner Agent
↓
Literature Agent
↓
Hypothesis Agent
↓
Writer Agent
↓
Final Research Report
```

# ⚙️ Technologies Used

* Python
* Streamlit (UI)
* Qdrant (Vector Database)
* SentenceTransformers (BGE embeddings)
* Ollama (Local LLM)- Gemma:2-b
* Multi-Agent Prompt Engineering

# 🧩 Step-by-Step Workflow Explanation (Theoretical)

## 1️⃣ Document Parsing

The system extracts text from uploaded research PDFs.


## 2️⃣ Semantic Chunking

The document is divided into smaller text segments to improve retrieval quality.


## 3️⃣ Embedding Generation

Each chunk is converted into a dense vector representation using transformer-based embeddings.

These embeddings capture semantic meaning.


## 4️⃣ Vector Storage

Embeddings are stored inside Qdrant, a high-performance vector database.

This allows similarity-based retrieval instead of keyword matching.


## 5️⃣ Context Retrieval

When a user asks a research question:

* The question is embedded
* Compared against stored vectors
* Top relevant chunks are retrieved


## 6️⃣ Multi-Agent Research Reasoning

### 🔹 Planner Agent

Breaks the research question into structured sub-questions.

### 🔹 Literature Agent

Analyzes retrieved content and extracts:

* Key findings
* Methods
* Limitations
* Research gaps

### 🔹 Hypothesis Agent

Generates:

* Research hypotheses
* Experimental ideas
* Evaluation suggestions

### 🔹 Writer Agent

Compiles all reasoning into a structured academic-style research report.


# 🚀 Installation & Setup Guide (From Scratch)

## 🔹 1. Clone the Repository

```bash
git clone https://github.com/sowmya13531/AURA-AI-Multi-Agent-RAG-Research-Assistant-.git
cd AURA-AI-Multi-Agent-RAG-Research-Assistant-
```


## 🔹 2. Create Virtual Environment

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```


## 🔹 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements file is missing:

```bash
pip install streamlit qdrant-client sentence-transformers pypdf ollama
```

---

## 🔹 4. Install Ollama

Download from:
[https://ollama.com](https://ollama.com)

Then pull a lightweight model:

```bash
ollama pull tinyllama
```

OR

```bash
ollama pull gemma:2b
```
I used gemma:2-b

## 🔹 5. Run the Application

```bash
streamlit run app.py
```

Then open browser at:

```
http://localhost:xxxx
```


# 🧪 How to Use

1. Upload a research paper (PDF)
2. Wait for indexing
3. Enter a research question
4. View:

   * Research plan
   * Literature analysis
   * Hypothesis
   * Full research report

# 📈 Key Engineering Highlights

* Avoided vector database locking issues
* Optimized memory usage for local LLM
* Implemented Streamlit caching
* Built modular multi-agent reasoning pipeline
* Designed production-style project structure

# 🔮 Future Improvements

* PDF export of generated reports
* Multi-document support
* Persistent vector storage
* Cloud LLM integration
* Evaluation metrics dashboard
* Research memory tracking


# 👩‍💻 Author

**Sowmya Kanithi**
AI Machine Learning | Gen AI | NLP Enthusiast
Focused on building scalable AI systems and multi-agent architectures.
