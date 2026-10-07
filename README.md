<div align="center">

# 🧠 NexaVault AI

### Private AI Knowledge, Powered Locally.

Transform documents into an intelligent, searchable knowledge environment.

<br>

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_AI-000000?style=for-the-badge)](https://ollama.com/)
[![Qwen](https://img.shields.io/badge/Qwen2.5-3B-00A67E?style=for-the-badge)](https://ollama.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-5B21B6?style=for-the-badge)](https://www.trychroma.com/)
[![RAG](https://img.shields.io/badge/RAG-Retrieval--Augmented_Generation-F97316?style=for-the-badge)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)
[![License](https://img.shields.io/badge/License-MIT-F5C518?style=for-the-badge)](LICENSE)

<br>

**Upload → Index → Ask → Retrieve → Understand**

</div>

---

# 📌 Overview

**NexaVault AI** is a local-first AI knowledge assistant designed to help users interact with their documents through natural language.

Instead of manually opening files, searching through folders, checking emails, reviewing reports, or looking through presentations, users can upload their documents to NexaVault AI and ask questions about the information they contain.

The application combines:

- Document processing
- Semantic search
- Vector databases
- Retrieval-Augmented Generation (RAG)
- Local language models
- OCR
- Conversational AI

into a single application.

The result is a searchable knowledge environment where users can interact with organizational information using natural language.

---

# 🎯 The Idea

Organizations accumulate enormous amounts of information.

That information can be spread across:

- PDF reports
- Word documents
- Excel spreadsheets
- PowerPoint presentations
- Emails
- Policies
- Manuals
- Meeting documents
- Technical documentation
- Scanned documents
- Images
- CSV files

Traditional document search often requires users to know exactly where information is stored.

NexaVault AI changes the interaction model.

Instead of asking:

> "Which file contains this information?"

users can ask:

> **"What are the major risks identified in the project?"**

The system searches the knowledge base, retrieves relevant content, and generates a response using a locally hosted AI model.

---

# ⚡ Why NexaVault AI?

NexaVault AI focuses on one simple principle:

> **Your knowledge should be easier to access without giving up control of your data.**

### Core principles

| Principle            | Description                                             |
| -------------------- | ------------------------------------------------------- |
| 🔒 Local-first       | AI inference can run directly on your machine           |
| 📚 Knowledge-centric | Documents become a searchable knowledge base            |
| 🔍 Semantic          | Search is based on meaning, not only keywords           |
| 🤖 AI-powered        | Local LLM generates natural-language answers            |
| 📑 Source-aware      | Responses can be grounded in retrieved document content |
| 🧩 Modular           | Processing and application services are separated       |
| ⚡ Practical         | Designed for real-world document workflows              |

---

# 🏗️ How It Works

NexaVault AI follows a Retrieval-Augmented Generation architecture.

```text
                  ┌─────────────────────┐
                  │       Documents     │
                  │ PDF DOCX PPTX XLSX  │
                  │ TXT CSV EML MSG     │
                  │ PNG JPG JPEG        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Document Extraction │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Text Cleaning       │
                  │ & Processing        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Document Chunking   │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Embedding Model     │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │     ChromaDB        │
                  │   Vector Database   │
                  └──────────┬──────────┘
                             │
                      User Question
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Semantic Retrieval  │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Relevant Context    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Ollama + Qwen2.5    │
                  │     Local LLM       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │    AI Response      │
                  │ + Supporting Source │
                  └─────────────────────┘
```

````

---

# 🔄 Knowledge Pipeline

When documents are uploaded, NexaVault AI processes them through several stages.

### 1. Ingestion

The application accepts supported document formats.

### 2. Extraction

Text and relevant content are extracted from the files.

### 3. Processing

Extracted information is cleaned and prepared for indexing.

### 4. Chunking

Large documents are divided into smaller semantic sections.

### 5. Embeddings

Document chunks are converted into numerical vector representations.

### 6. Indexing

The vectors are stored in ChromaDB.

### 7. Retrieval

When a user asks a question, the system searches for the most relevant document chunks.

### 8. Generation

The retrieved context is supplied to the local language model.

### 9. Response

The assistant generates a natural-language response grounded in the retrieved information.

---

# 🤖 AI Assistant

The AI Assistant provides a conversational interface for interacting with indexed knowledge.

Users can ask questions naturally without needing to know:

- The exact document name
- The exact wording
- The location of the file
- The page number
- The terminology used by the document author

### Example

A document may contain:

```text
Application availability remained within acceptable
service-level requirements during the reporting period.
```

A user could ask:

```text
Is the application healthy?
```

The semantic retrieval layer can identify the relationship between the question and the document content.

---

# 💬 Example Questions

After building a knowledge base, users can ask questions such as:

```text
What are the main risks in the project?
Summarize the latest project report.
What is the employee leave policy?
Which document discusses the deployment process?
What were the major findings of the report?
Who approved this requirement?
Which actions are still outstanding?
Explain the maintenance procedure.
What are the main compliance requirements?
Summarize the document in simple language.
```

---

# 📂 Supported File Formats

NexaVault AI supports a range of commonly used enterprise and organizational formats.

| Category         | Supported Formats |
| ---------------- | ----------------- |
| 📄 Documents     | PDF, DOCX         |
| 📊 Spreadsheets  | XLSX, CSV         |
| 📽 Presentations | PPTX              |
| 📝 Text          | TXT               |
| 📧 Email         | EML, MSG          |
| 🖼 Images        | PNG, JPG, JPEG    |

_Image documents can be processed using OCR when applicable._

---

# 🔍 Semantic Search

Traditional search depends heavily on matching exact words. NexaVault AI uses semantic representations to search according to the meaning of content.

### Traditional keyword search

```text
Question: "Is the system healthy?"
Search: "healthy"
```

_If the document never uses the word `healthy`, a basic keyword search may fail._

### Semantic retrieval

```text
Question: "Is the system healthy?"
       ↓
Meaning representation
       ↓
Find related content
       ↓
"Application availability remained within acceptable service levels."
       ↓
Relevant context retrieved
```

_This makes information discovery more flexible when different people use different terminology._

---

# 📑 Source-Aware Responses

NexaVault AI is designed around retrieval before generation. The assistant first searches the indexed knowledge base and then uses relevant document content as context for the response.

This provides several advantages:

- Better grounding
- Easier verification
- Greater transparency
- Reduced dependence on model memory
- Better connection between answers and source documents

The goal is not simply to generate an answer. The goal is to generate an answer based on the organization's own knowledge.

---

# ⚙️ Administration

NexaVault AI includes an administration interface for managing the knowledge base. Administrators can work with the document ingestion pipeline and monitor the state of the knowledge base.

Typical operations include:

- 📤 **Upload Documents:** Add documents to the application.
- 🧠 **Build Knowledge Base:** Process documents, generate embeddings, and create the searchable vector index.
- 🔄 **Rebuild Index:** Reprocess the knowledge base when required.
- 📊 **Monitor Status:** Review knowledge-base information and processing status.
- 📁 **Manage Knowledge:** Maintain the collection of documents used by the assistant.

---

# 🧠 Local AI

NexaVault AI uses **Ollama** as the local model runtime.

The default language model is:

```text
Qwen2.5:3B
```

The model can run locally instead of requiring a cloud-hosted AI API for the core assistant workflow. This architecture is particularly useful for environments where organizations want greater control over their data and AI infrastructure.

---

# 🔐 Privacy & Data Control

NexaVault AI is designed with a local-first philosophy. The core application can operate using your local machine's resources (Documents, Knowledge Base, Vector Database, Embedding Model, and Local LLM) rather than depending on a remote AI service for the main RAG workflow.

> **Important:** Local deployment does not automatically make a system secure. For production use, organizations should additionally consider authentication, authorization, file permissions, encryption, network security, secure backups, access logging, data retention, and operating-system security. NexaVault AI provides a local-first technical foundation, while production security should be configured according to the deployment environment.

---

# 🌍 Potential Use Cases

NexaVault AI is intentionally designed as a general-purpose knowledge platform. It can be adapted for different departments and industries.

### 🏢 Corporate Knowledge

Search policies, procedures, internal documentation, reports, meeting records, and operational guides.

> _Example: "What is the company's remote-work policy?"_

### 📋 Project Management

Search project charters, requirements, risk registers, status reports, meeting minutes, UAT documentation, and deployment guides.

> _Example: "What are the highest project risks?"_

### 👥 Human Resources

Search employee handbooks, leave policies, benefits, HR procedures, travel policies, and workplace guidelines.

> _Example: "How many days of leave are employees entitled to?"_

### 🏥 Healthcare Operations

Search operational procedures, clinical documentation, guidelines, equipment manuals, and quality documentation.

> _Example: "What is the patient discharge procedure?"_
> _(Note: Healthcare deployments should use appropriate governance, access controls, privacy protections, and professional review.)_

### 💰 Finance & Compliance

Search compliance policies, audit reports, KYC procedures, AML documentation, fraud policies, and financial procedures.

> _Example: "What controls are required for high-risk transactions?"_

### 🏭 Manufacturing

Search maintenance manuals, SOPs, quality documentation, equipment guides, safety procedures, and troubleshooting documentation.

> _Example: "What maintenance procedure applies to this machine?"_

### ⚖️ Legal & Compliance

Search contracts, agreements, policies, compliance documents, and regulatory documentation.

> _Example: "What are the payment terms in the contract?"_

### 🎓 Education & Research

Search course materials, research documents, training manuals, institutional policies, and technical documentation.

> _Example: "Summarize the main concepts covered in this material."_

---

# 🛠 Technology Stack

NexaVault AI is built using a modular Python-based technology stack.

| Layer           | Technology                     | Role                             |
| --------------- | ------------------------------ | -------------------------------- |
| Programming     | Python                         | Core application                 |
| Interface       | Streamlit                      | Web application                  |
| AI Runtime      | Ollama                         | Local model execution            |
| Language Model  | Qwen2.5 3B                     | Response generation              |
| Vector Database | ChromaDB                       | Semantic vector storage          |
| Embeddings      | Sentence Transformers          | Semantic representations         |
| RAG             | Retrieval-Augmented Generation | Knowledge-grounded answers       |
| Text Processing | LangChain                      | Document chunking and processing |
| PDF             | PyMuPDF                        | PDF extraction                   |
| Word            | python-docx                    | DOCX processing                  |
| PowerPoint      | python-pptx                    | PPTX processing                  |
| Spreadsheet     | Pandas / OpenPyXL              | XLSX and CSV processing          |
| OCR             | Tesseract / Pillow             | Image text extraction            |
| Version Control | Git                            | Source control                   |
| Repository      | GitHub                         | Project hosting                  |

---

# 🧩 Project Architecture

The project separates the user interface from the underlying processing services.

```text
NexaVault-AI/
│
├── app.py
│
├── components/
│   ├── sidebar.py
│   ├── chat_ui.py
│   ├── admin_dashboard.py
│   └── footer.py
│
├── services/
│   ├── document_loader/
│   │   ├── ...
│   │
│   ├── vector_store_service.py
│   └── ...
│
├── Images/
│   └── ...
│
├── requirements.txt
├── README.md
├── install.md
└── LICENSE
```

### Application Layer

The Streamlit application provides the user-facing interface.

### Component Layer

Reusable UI components provide navigation, chat interface, administration, and footer elements.

### Service Layer

Backend services handle document extraction, processing, embedding, vector storage, retrieval, and AI interaction. This separation helps keep the project maintainable and makes future extensions easier.

---

# 📦 Installation

## Requirements

Before installing NexaVault AI, make sure you have:

- Python 3.11+
- Git
- Ollama
- Tesseract OCR
- Internet access for initial package/model installation

## 1. Clone the Repository

```bash
git clone https://github.com/Sayed-jibril/NexaVault-AI.git
cd NexaVault-AI
```

## 2. Create a Virtual Environment

```bash
python -m venv .venv
```

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

## 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Install the Local Model

Make sure Ollama is installed, then run:

```bash
ollama pull qwen2.5:3b
```

Verify installation:

```bash
ollama list
```

## 5. Start the Application

```bash
python -m streamlit run app.py
```

Then open your browser to: `http://localhost:8501`

> For detailed setup instructions, see the **[Installation Guide](install.md)**.

---

# 🚀 Quick Start

For an already configured machine:

```bash
git clone https://github.com/Sayed-jibril/NexaVault-AI.git
cd NexaVault-AI
python -m venv .venv
source .venv/bin/activate  # Use .venv\Scripts\activate on Windows
pip install -r requirements.txt
ollama pull qwen2.5:3b
python -m streamlit run app.py
```

Open: `http://localhost:8501`

---

# 🖥️ Typical User Workflow

```text
       START
         │
         ▼
   Open NexaVault AI
         │
         ▼
   Administration
         │
         ▼
   Upload Documents
         │
         ▼
 Build Knowledge Base
         │
         ▼
 Knowledge Base Ready
         │
         ▼
    AI Assistant
         │
         ▼
    Ask Question
         │
         ▼
 Semantic Retrieval
         │
         ▼
   Local AI Model
         │
         ▼
    AI Response
```

---

# 🧪 Development

For development, create an isolated environment:

```bash
python -m venv .venv
source .venv/bin/activate  # Use .venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m streamlit run app.py
```

---

# 🛠️ Troubleshooting

### Python is not recognized

Run `python --version`. If Python is unavailable, install Python 3.11 or newer and ensure it is added to your system PATH.

### Streamlit is not recognized

Use `python -m streamlit run app.py` instead of `streamlit run app.py`.

### Ollama is unavailable

Check `ollama --version`. Then verify the model with `ollama list`. If the model is missing, run `ollama pull qwen2.5:3b`.

### Tesseract is unavailable

Check `tesseract --version`. Make sure Tesseract is installed and available through your system PATH.

### A Python module is missing

Activate the virtual environment and run `pip install -r requirements.txt`. If a specific package is missing, install that dependency as required by the error message.

### The application cannot connect to Ollama

Make sure Ollama is running. Depending on your operating system, Ollama may already be running in the background. Otherwise, run `ollama serve` and then restart NexaVault AI.

### Knowledge Base is empty

Make sure you:

1. Upload documents.
2. Build the Knowledge Base.
3. Wait for processing to finish.
4. Confirm that the Knowledge Base is ready.
5. Return to the AI Assistant.

---

# 🧭 Roadmap

NexaVault AI is designed to evolve into a broader local enterprise knowledge platform. Potential future improvements include:

- [ ] User authentication
- [ ] Role-based access control
- [ ] Multiple knowledge bases
- [ ] Department-based knowledge spaces
- [ ] Document preview
- [ ] Advanced source navigation
- [ ] Conversation export & history
- [ ] Hybrid keyword + semantic search
- [ ] Retrieval reranking & evaluation
- [ ] Multilingual document support
- [ ] Multiple local model support & selection interface
- [ ] Knowledge-base analytics
- [ ] Document version management
- [ ] API access
- [ ] Docker deployment
- [ ] Enterprise deployment configuration

---

# 🤝 Contributing

Contributions are welcome! If you would like to improve NexaVault AI:

1. **Fork the repository** via the GitHub **Fork** button.
2. **Create a feature branch:** `git checkout -b feature/your-feature`
3. **Make your changes:** Keep changes focused and modular.
4. **Test the application:** Make sure the application starts correctly and existing functionality remains operational.
5. **Commit your changes:** `git commit -m "Add your feature"`
6. **Push the branch:** `git push origin feature/your-feature`
7. **Open a Pull Request:** Describe what changed, why it changed, how it was tested, and any limitations or future work.

---

# 📜 License

NexaVault AI is released under the **MIT License**. See the [`LICENSE`](LICENSE) file for the complete license text.

---

# 👨‍💻 Developer

## Mohammed Siad Jibril

NexaVault AI is developed by **Mohammed Siad Jibril**, with a focus on Artificial Intelligence, Data Science, intelligent applications, automation, and practical AI systems.

### GitHub

**[https://github.com/Sayed-jibril](https://github.com/Sayed-jibril)**

---

# 🌟 Support the Project

If NexaVault AI is useful to you:

- ⭐ **Star the repository**
- 🐛 **Report issues**
- 💡 **Suggest improvements**
- 🤝 **Contribute features**
- 📢 **Share the project**

Every contribution helps improve the project.

---

<div align="center">

# 🧠 NexaVault AI

### Private AI Knowledge, Powered Locally.

**Documents → Knowledge → Retrieval → AI**

Built with:
**Python • Streamlit • Ollama • Qwen2.5 • ChromaDB • RAG**

<br>

Developed by **Mohammed Siad Jibril**

<br>

⭐ **Star the repository if you find it useful.**

</div>
```

### Next Steps for You:

1. **Create the Repository:** Go to GitHub and create a new public repository named exactly `NexaVault-AI` under your `Sayed-jibril` account.
2. **Replace the README:** Copy the entire block above and paste it into your new `README.md` file.
3. **Update Code Identity:** As mentioned, ensure you search and replace any lingering references to the old project name or previous author in `app.py`, `components/`, `services/`, and any other files to maintain a consistent, professional brand identity for **NexaVault AI**.
````
