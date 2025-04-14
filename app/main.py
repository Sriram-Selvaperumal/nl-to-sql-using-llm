from flask import Flask, render_template, request
from app.model_runner import load_model, query_model
from app.utils import build_prompt

app = Flask(__name__, template_folder="templates")


llm = load_model()

@app.route("/", methods=["GET", "POST"])
def home():
    sql_query = ""
    if request.method == "POST":
        user_input = request.form.get("query")
        if user_input:
            prompt = build_prompt(user_input)
            sql_query = query_model(llm, prompt)
    return render_template("index.html", result=sql_query)

if __name__ == "__main__":
    app.run(debug=True)
