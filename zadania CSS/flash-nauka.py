from flask import Flask, render_template, request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/kontakt", methods=["GET","POST"])
def kontakt():
    if request.method=="POST":
        print(" dziękujemy za wiadomość")
        print(request.form)
        return redirect("/podziekowania")

    else:
        return render_template("kontakt.html") 

@app.route("/podziekowania")
def dziekujemy():
    return render_template("podziekowania.html")        