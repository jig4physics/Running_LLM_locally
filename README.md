
# AI and Machine Learning Projects

This repository contains a collection of five projects showcasing different AI and machine learning technologies and frameworks. Each project focuses on a unique aspect of AI, such as natural language processing, text generation, or audio transcription.

---

## Projects Overview

### 1. **Llama_cpp: Basic Chat Completion**

   - **Description**: Utilizes the `llama_cpp` library to load a pre-trained Llama model and perform chat-based text generation.
   - **Key Features**:
     - Supports GPU acceleration and customizable parameters like context length and random seed.
   - **Script**: Demonstrates creating a conversational assistant for answering questions.

   **[Learn More](README_parallel.md)**

---

### 2. **Llama_cpp with Parallel Processing**

   - **Description**: Extends the first project by leveraging `ray` for parallel execution of multiple tasks using the Llama model.
   - **Key Features**:
     - Enables parallel chat completion tasks for improved efficiency.
   - **Script**: Handles multiple Llama chat completions simultaneously.

   **[Learn More](README_parallel.md)**

---

### 3. **Text Generation with Meta-Llama**

   - **Description**: Implements text generation using Hugging Face's `transformers` library with the `Meta-Llama-3-8B` model.
   - **Key Features**:
     - Supports mixed-precision computation (`bfloat16`) and automatic device mapping.
   - **Script**: Generates coherent responses to user prompts.

   **[Learn More](README_transformers.md)**

---

### 4. **Audio Transcription with Whisper**

   - **Description**: Transcribes audio into text using OpenAI's Whisper model.
   - **Key Features**:
     - Supports multiple Whisper model types.
     - Converts PyTorch tensors to NumPy arrays for compatibility.
   - **Script**: Includes a `Transcription` class for processing audio waveforms.

   **[Learn More](README_whisper.md)**

---

## Installation

### Prerequisites

- Python 3.8 or higher
- Additional libraries required for each project (listed in individual READMEs).

### General Setup

Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

Install necessary libraries:

```bash
pip install -r requirements.txt
```

---

## Usage

Each project has its own README file with detailed setup and execution instructions. Refer to the respective links provided above for specific guidance.

---

## Notes

- Ensure proper hardware (e.g., GPUs) for models requiring high computational resources.
- Some projects may require additional configurations, such as downloading pre-trained models.

---

## License

This repository is licensed under the MIT License. Please refer to the `LICENSE` file for details.
