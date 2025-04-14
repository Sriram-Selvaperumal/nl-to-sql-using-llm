import os

def get_model_path():
    return os.path.join(
        "C:\\Users\\srira\\OneDrive\\Desktop\\unilang-sql-converter\\models",
        "mistral-7b-v0.1.Q4_K_M.gguf"
    )

def build_prompt(user_input):
    return f"Convert the following query to SQL: {user_input}"
