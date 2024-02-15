from flask import Flask,render_template,request
app = Flask("flaskapp")

@app.route("/")
def HelloFlask():
    return "Hello Flask"
@app.route("/about")
def About():
    return render_template('About.html')

@app.route("/watch",methods =['GET'])
def Watch():
    return render_template('watch.html')

@app.route("/submit",methods =['POST'])
def Submit():
    username = request.form["username"]
    return render_template("submit.html",username=username)

if __name__ == "__main__":
    app.run(debug=True)