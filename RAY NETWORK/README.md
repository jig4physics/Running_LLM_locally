
# Parallel Llama Model Execution with Ray

This project demonstrates how to run multiple instances of the `llama_cpp` library in parallel using the `ray` library. The script initializes tasks that interact with a large language model (LLM) to generate responses for specific prompts.

## Features

- Parallelized task execution with Ray.
- Customizable model configuration.
- GPU acceleration support for faster inference.

---

## Installation

### Prerequisites

Ensure you have Python 3.8 or higher installed on your system.

### Install Required Libraries

Install the necessary libraries using pip:

```bash
pip install llama-cpp-python ray
```

---

## Usage

1. **Download the Model**

   Download the `gemma-1.1-2b-it.Q4_K_M.gguf` model file and place it in the `models/` directory.

2. **Configure the Script**

   Update the `model_path` in the script to point to the correct model file location.

3. **Run the Script**

   Save the script below as `parallel_llama.py`:

   ```python
   from llama_cpp import Llama
   import multiprocessing
   import time
   import json
   import ray

   ray.init()

   @ray.remote(num_gpus=1)
   def runLLM(taskID):
       print(f"*** Start {taskID} ***")
       start_time = time.time()

       llm = Llama(
           model_path="models/gemma-1.1-2b-it.Q4_K_M.gguf",
           n_gpu_layers=8, # Uncomment to use GPU acceleration
           verbose=False,
           n_ctx=2048, # Set the context window size
           chat_format="gemma"
       )

       reply = llm.create_chat_completion(
           messages=[
               {"role": "system", "content": "You are an assistant who perfectly describes topics."},
               {"role": "user", "content": "Describe Machine Learning."}
           ]
       )

       print(f"Answer of Task {taskID}: {reply['choices'][0]['message']['content']}")
       end_time = time.time()
       execution_time = end_time - start_time
       print(f"Execution time: {execution_time} seconds")

   if __name__ == "__main__":
       futures = [runLLM.remote(i) for i in range(2)]
       results = ray.get(futures)
   ```

4. **Execute the Script**

   Run the script in your terminal:

   ```bash
   python parallel_llama.py
   ```

5. **Output**

   The script will execute two tasks in parallel, each generating a response for the prompt.

---

## Configuration Options

- **`model_path`**: Specify the path to the model file.
- **`n_gpu_layers`**: Set the number of layers to offload to the GPU for improved performance.
- **`n_ctx`**: Set the context window size.
- **`chat_format`**: Specify the chat format (e.g., `gemma`).

---

## License

This project is licensed under the MIT License. Please refer to the `LICENSE` file for details.