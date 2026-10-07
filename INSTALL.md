# 🚀 NexaVault AI — Installation Guide

Welcome to **NexaVault AI**.

NexaVault AI is a private, locally hosted knowledge assistant that allows you to turn your documents into a searchable AI knowledge base.

Instead of manually searching through PDFs, Word files, spreadsheets, presentations, emails, and images, you can upload your documents and ask questions in natural language.

The application uses local AI through **Ollama**, meaning your documents can remain on your own machine.

---

## 📌 What You Will Install

NexaVault AI uses the following components:

| Component             | Purpose                              |
| --------------------- | ------------------------------------ |
| Python                | Runs the application and AI services |
| Streamlit             | Web interface                        |
| Ollama                | Local AI inference                   |
| Qwen2.5 3B            | Local language model                 |
| ChromaDB              | Vector database                      |
| Sentence Transformers | Document embeddings                  |
| LangChain             | Document processing and chunking     |
| Tesseract OCR         | Text extraction from images          |
| Git                   | Download and manage the project      |

---

# 1. 📋 Requirements

Before installing NexaVault AI, make sure your computer has:

- Python **3.11 or newer**
- Git
- Ollama
- Tesseract OCR
- Internet connection for the initial installation
- At least several GB of available storage

### Supported operating systems

- Windows 10 / 11
- macOS
- Linux

---

# 2. 📥 Download the Project

Open **Command Prompt**, PowerShell, or Terminal.

Clone the repository:

```bash
git clone https://github.com/Sayed-jibril/NexaVault-AI.git
```
