
# Banana Bread Recipe Generation with vLLM

This project showcases the usage of the `vLLM` library to generate text responses based on prompts. It uses the `OpenHermes-2.5-Mistral-7B-pruned50` model configured for sparsity optimization.

## Features

- Supports sparse model inference for efficient computation.
- Customizable text generation through sampling parameters.
- Compatible with both CPU and GPU.

---

## Installation

### Prerequisites

Ensure you have Python 3.8 or higher installed.

### Install Required Libraries

Install the necessary libraries using pip:

```bash
pip install vllm
```

---

## Usage

1. **Save the Script**

   Save the script below as `vllm_banana_bread.py`:

   ```python
   from vllm import LLM, SamplingParams

   # Initialize the model
   model = LLM(
       "nm-testing/OpenHermes-2.5-Mistral-7B-pruned50", 
       sparsity="sparse_w16a16",
       device="cpu"  # Change to "cuda" for GPU
   )

   # Define the prompt
   prompt = "How to make banana bread?"
   formatted_prompt = f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant"

   # Configure sampling parameters
   sampling_params = SamplingParams(max_tokens=100)

   # Generate text
   outputs = model.generate(formatted_prompt, sampling_params=sampling_params)
   print(outputs[0].outputs[0].text)
   ```

2. **Run the Script**

   Execute the script:

   ```bash
   python vllm_banana_bread.py
   ```

3. **Output**

   The model will generate a detailed recipe for making banana bread.

---

## Configuration Options

- **`sparsity`**: Set to `"sparse_w16a16"` for sparsity optimization.
- **`device`**: Specify `"cpu"` or `"cuda"` depending on the available hardware.
- **`max_tokens`**: Define the maximum number of tokens to generate.

---

## Notes

- Ensure the `nm-testing/OpenHermes-2.5-Mistral-7B-pruned50` model is downloaded or accessible.
- The script supports both sparse and dense model configurations.

---

## License

This project is licensed under the MIT License. Refer to the `LICENSE` file for details.