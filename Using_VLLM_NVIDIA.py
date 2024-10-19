from vllm import LLM, SamplingParams

model = LLM(
    "nm-testing/OpenHermes-2.5-Mistral-7B-pruned50", 
    sparsity="sparse_w16a16",
    device="cpu"
)
prompt = "How to make banana bread?"
formatted_prompt =  f"<|im_start|>user\n{prompt}<|im_end|>\n<|im_start|>assistant"

sampling_params = SamplingParams(max_tokens=100)
outputs = model.generate(formatted_prompt, sampling_params=sampling_params)
print(outputs[0].outputs[0].text)