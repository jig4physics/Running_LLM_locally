
# README

## Project Overview
This project demonstrates how to use the `llama_index` library to build a document indexing and querying system. It includes implementations for both simple (non-persistent) and persistent embeddings storage. The code leverages OpenAI's API for processing queries and generating answers from indexed documents.

---

## Features
- **Simple Querying**: Quickly index documents and query without persistence.
- **Persistent Storage**: Save and load embeddings for reuse across sessions.
- **Custom Query Engine**: Perform customized queries using the indexed data.

---

## Prerequisites
- Python 3.7+
- Required Python packages (install using `pip install -r requirements.txt`):
  - `llama-index`
  - `python-dotenv`
- An OpenAI API Key:
  - Store it in a `.env` file with the variable name `OPENAI_API_KEY`.

Example `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Project Structure
- **`data/`**: Directory containing documents to index.
- **`storage/`**: Directory for storing persistent embeddings (created dynamically).
- **Main script**: Contains functions for indexing and querying documents.

---

## How to Use

### Step 1: Set Up Your Environment
1. Clone the repository and navigate to the directory.
2. Install the required dependencies:
   ```bash
   ./install.sh
   ```
3. Create a `.env` file and add your OpenAI API key.

### Step 2: Running the Code
#### Option 1: Simple Querying (Without Persistence)
1. Uncomment the `simple()` function in the `__main__` section.
2. Run the script:
   ```bash
   python main.py
   ```

#### Option 2: Persistent Embeddings
1. **Create Embeddings**:
   - Uncomment the `createEmbedding()` function in the `__main__` section and run the script.
   - This will process the documents and store the embeddings in the `storage/` directory.
2. **Load and Query**:
   - Uncomment the `loadEmbedding()` and `fireQuery(index, query)` functions in the `__main__` section.
   - Modify the `query` variable to your desired question and run the script.
   - Example query:
     ```python
     answer = fireQuery(index, "Who is the host?")
     print(answer)
     ```

---

## Notes
- Ensure the `data/` directory contains text files or documents to index before running the script.
- Modify the query text in the `fireQuery()` function as needed for different questions.
- The `persist_dir` used in `loadEmbedding()` must match the directory used in `createEmbedding()`.

---

## Troubleshooting
- **Missing OpenAI API Key**: Ensure you have a `.env` file with the correct key.
- **Empty Results**: Verify that the `data/` directory contains documents and the embeddings have been created properly.
- **Installation Issues**: Ensure all dependencies are installed correctly and compatible with your Python version.

---
