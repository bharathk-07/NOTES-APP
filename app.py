from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

notes = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title")
        text = request.form.get("note")

        if title and text:
            now = datetime.now().strftime("%d %b %Y - %I:%M %p")
            notes.append({
                "title": title,
                "text": text,
                "time": now
            })

        return redirect("/")

    return render_template("index.html", notes=notes)


# DELETE
@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(notes):
        notes.pop(index)
    return redirect("/")


# ✏️ EDIT
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if request.method == "POST":
        notes[index]["title"] = request.form.get("title")
        notes[index]["text"] = request.form.get("note")
        notes[index]["time"] = datetime.now().strftime("%d %b %Y - %I:%M %p")
        return redirect("/")

    return render_template("edit.html", note=notes[index], index=index)


if __name__ == "__main__":
    app.run(debug=True)