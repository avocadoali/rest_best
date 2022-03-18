from flask import Flask, redirect, url_for, request, session,  render_template, jsonify
from datetime import timedelta


from fetch_data import test

## Start App on local host like this:

# python3 -m venv rest_best
# source rest_best/bin/activate
# pip install -r requirements.txt
# python3 -m flask run


app=Flask(__name__)
app.secret_key = "dis is a secret key"
def home_view():        
    return render_template('index.html')

@app.route('/')
def home_view():        
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():      
    if request.method == "POST":
        session.permanent = True
        tablenumber = request.form["tablenumber"]
        session["tablenumber"] = tablenumber
        return redirect(url_for("table"))
    else:
        return render_template("login.html")

@app.route("/table")
def table():
    if "tablenumber" in session:
        tb = session["tablenumber"]
        return f"<h1> {tb}</h1>"
    else:
        return redirect(url_for ("login"))

@app.route("/logout")
def logout():
    session.pop("tablenumber", None)
    return redirect(url_for("login"))


@app.route("/pain" , methods=['GET', 'POST'])
def pain():
    output = test()
    print("nach test")
    return jsonify(output)




