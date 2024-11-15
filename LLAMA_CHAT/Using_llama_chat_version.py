from llama_cpp import Llama

llm = Llama(
      model_path="Lexi-Llama-3-8B-Uncensored_Q4_K_M.gguf",
      n_gpu_layers=8,
      verbose=False,
      chat_format="llama-2"
)
reply = llm.create_chat_completion(
messages = [
                  {
                        "role": "system", 
                        "content": "You are an assistant who perfectly describes topic."
                  },
                  {
                        "role": "user",
                        "content": "Describe Machine Learning."
                  }
      ]
)

print("\n")
print(f"Answer : {reply['choices'][0]['message']['content']}")
