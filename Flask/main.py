from flask import Flask
app = Flask("flaskapp")

@app.route("/")
def HelloFlask():
    return "Hello Flask"
if __name__ == "__main__":
    app.run(debug=True)