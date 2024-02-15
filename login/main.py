from flask import Flask,render_template,request
app = Flask("flaskapp")


db = ["admin_admin","qwerty_password"]
@app.route("/")
def Main():
    return render_template('main.html')

@app.route("/login",methods =['POST'])
def Login():
    login = request.form["login"]
    password = request.form["password"]
    isValid = login+"_"+password in db
    return render_template("login.html",isValid=isValid)





if __name__ == "__main__":
    app.run(debug=True)