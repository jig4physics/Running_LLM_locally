
# Llama Model Chatbot

This project demonstrates how to use the `llama_cpp` library to interact with a large language model (LLM) for conversational AI tasks. The example uses the `Lexi-Llama-3-8B-Uncensored_Q4_K_M.gguf` model to generate responses to user queries.

## Features

- Easy-to-use conversational AI setup.
- Customizable model path and parameters.
- Supports multi-GPU layers for improved performance.

---

## Installation

To set up and run this project, follow these steps:

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

### Install Required Libraries

Use the following command to install the `llama_cpp` library:

```bash
pip install llama-cpp-python
```

---

## Usage

1. **Download the Model**

   - Download the model file `Lexi-Llama-3-8B-Uncensored_Q4_K_M.gguf` and place it in the desired directory.

2. **Configure the Script**

   Update the `model_path` in the script to the path where your model file is located.

3. **Run the Script**

   Save the script below as `chatbot.py`:

   ```python
   from llama_cpp import Llama

   # Load the model
   llm = Llama(
       model_path="Lexi-Llama-3-8B-Uncensored_Q4_K_M.gguf",
       n_gpu_layers=8,
       verbose=False,
       chat_format="llama-2"
   )

   # Create a chat completion
   reply = llm.create_chat_completion(
       messages=[
           {"role": "system", "content": "You are an assistant who perfectly describes topics."},
           {"role": "user", "content": "Describe Machine Learning."}
       ]
   )

   # Print the response
   print("\n")
   print(f"Answer : {reply['choices'][0]['message']['content']}")
   ```

4. **Execute the Script**

   Run the script in your terminal:

   ```bash
   python chatbot.py
   ```

5. **Output**

   The script generates a detailed description of Machine Learning as a response.

---

## Configuration Parameters

You can modify the parameters in the `Llama` initialization:

- **`model_path`**: Path to the model file.
- **`n_gpu_layers`**: Number of layers offloaded to the GPU for faster inference.
- **`verbose`**: Set to `True` for detailed logs during model loading and inference.
- **`chat_format`**: Specify the chat format (e.g., `llama-2`).

---

## License

This project is licensed under the MIT License. Please refer to the `LICENSE` file for details.