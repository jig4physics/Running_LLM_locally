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
            # n_threads=8,  
            # seed=1337, # Uncomment to set a specific seed
            n_ctx=2048, # Uncomment to increase the context window
            chat_format="gemma"
      )
      
    # reply = llm(
    #     "Q: Name the planets in the solar system? A:",
    #     stop=["\n"],
    # )

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
    print(f"Answer of Task: {taskID}  : {reply['choices'][0]['message']['content']}")
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")




if __name__ == "__main__":
      futures = [runLLM.remote(i) for i in range(2)]
      results = ray.get(futures) 
      # print(results)
