from app.utils import get_model_path
from llama_cpp import Llama


def load_model():
    model_path = get_model_path()
    llm = Llama(
        model_path=model_path,
        n_ctx=2048,
        n_threads=8,
        n_gpu_layers=20,  # Adjust based on your GPU capability
        use_mlock=True
    )
    return llm

def query_model(model, prompt):
    output = model(prompt, max_tokens=200, stop=[";"])
    return output["choices"][0]["text"].strip()
