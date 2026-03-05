import streamlit as st
import os

from retrieval.pdf_parser import extract_text_from_pdf
from retrieval.embedder import create_embeddings
from retrieval.vector_store import VectorStore
from retrieval.rag_pipeline import retrieve_context

from agents.planner_agent import plan_research
from agents.literature_agent import analyze_literature
from agents.hypothesis_agent import generate_hypothesis
from agents.writer_agent import write_report


# -------------------------------
# Streamlit Config
# -------------------------------
st.set_page_config(page_title="AURA Research Assistant", layout="wide")
st.title("📚 AURA - AI Research Assistant")


# -------------------------------
# Simple Text Chunking Function
# -------------------------------
def split_text(text, chunk_size=800, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


# -------------------------------
# Cache Vector Store
# -------------------------------
@st.cache_resource
def get_vector_store():
    return VectorStore(dimension=384)


vector_store = get_vector_store()


# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader("Upload a Research Paper (PDF)", type=["pdf"])

if uploaded_file:

    save_dir = "data/uploaded_papers"
    os.makedirs(save_dir, exist_ok=True)

    file_path = os.path.join(save_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("PDF uploaded successfully ✅")

    # Extract Text
    text = extract_text_from_pdf(file_path)

    if "⚠️" in text or "❌" in text:
        st.error(text)
        st.stop()

    # Chunk Text
    chunks = split_text(text)

    # Create Embeddings
    embeddings = create_embeddings(chunks)

    # Store embeddings only once per session
    if "indexed" not in st.session_state:
        vector_store.add_embeddings(embeddings, chunks)
        st.session_state.indexed = True
        st.success("Document indexed successfully 🚀")


# -------------------------------
# Research Question Section
# -------------------------------
st.subheader("🔎 Ask a Research Question")
question = st.text_input("Enter your research question:")

if question and "indexed" in st.session_state:

    with st.spinner("Running Multi-Agent Research Pipeline..."):

        # Step 1: Planner
        plan = plan_research(question)

        # Step 2: Retrieve Context
        context = retrieve_context(question, vector_store)

        # Step 3: Literature Analysis
        analysis = analyze_literature(context, question)

        # Step 4: Hypothesis Generation
        hypothesis = generate_hypothesis(analysis)

        # Step 5: Final Report
        report = write_report(question, analysis, hypothesis)

    st.markdown("## 🧩 Research Plan")
    st.write(plan)

    st.markdown("## 📖 Literature Analysis")
    st.write(analysis)

    st.markdown("## 🧪 Hypothesis & Research Ideas")
    st.write(hypothesis)

    st.markdown("## 📝 Final Research Report")
    st.write(report)


elif question and "indexed" not in st.session_state:
    st.warning("Please upload and index a PDF first.")