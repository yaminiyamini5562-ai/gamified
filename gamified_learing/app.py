from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lesson", methods=["POST"])
def lesson():
    mood = request.json["mood"]

    if mood == "happy":
        content = "🧠 Tough Quiz: Solve multiplication problems"
    elif mood == "sad":
        content = "🎮 Easy Game: Learn with cartoons"
    elif mood == "angry":
        content = "😌 Relax: Watch fun learning video"
    else:
        content = "📘 Normal Lesson: Addition basics"

    return jsonify({"lesson": content})

if __name__ == "__main__":
    app.run(debug=True)
