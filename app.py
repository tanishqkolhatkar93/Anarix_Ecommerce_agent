from flask import Flask, request, render_template
from query_engine import handle_query

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer, gemini_query = handle_query(question)
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
