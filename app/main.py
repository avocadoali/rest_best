from flask import Flask, redirect, url_for, request, session,  render_template, jsonify
from datetime import timedelta

from fetch_data import delete_items, get_distinct_table, get_menu_all, get_order_of_table, get_overview_orders, handle_order_cart

## Start App on local host like this:

# python3 -m venv rest_best
# source rest_best/bin/activate
# pip install -r requirements.txt
# python3 -m flask run


app=Flask(__name__)
app.secret_key = "dis is a secret key"

@app.route('/')
def home_view():        
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():      
    if request.method == "POST":
        session.permanent = True
        tablenumber = request.form["tablenumber"]
        session["tablenumber"] = tablenumber
        return redirect(url_for("menu"))
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


@app.route("/menu" , methods=['GET', 'POST'])
def menu():
    if request.method =='GET':
        list = get_menu_all()
        return render_template("list-view.html",  menu_list=list)

    dict_cart = request.form.to_dict()
    menu = get_menu_all()

    new_menu =  {}
    dict_cart = { k:v for k, v in dict_cart.items() if v }
    del dict_cart['Submit']
    print(dict_cart)
    new_menu =  {}
    for x in dict_cart:
        print(x)
        i = int(x)
        new_menu[x] = [dict_cart[x], menu[i-1]]

    session["dict_cart"] = new_menu
    return redirect(url_for("cart"))

@app.route("/cart" , methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        table_id = session["tablenumber"]
        list_cart = session["dict_cart"]
        handle_order_cart(table_id, list_cart)
        return redirect(url_for("orders"))

    return render_template("cart.html", list_cart = session["dict_cart"])
 

@app.route("/orders" , methods=['GET', 'POST'])
def orders():
    table_id = session["tablenumber"]
    list = get_order_of_table(table_id)
    print(list)
    return render_template("orders.html",  menu_list=list)


@app.route("/overview" , methods=['GET', 'POST'])
def overview():
    if request.method == 'POST':
        og_list = get_overview_orders()
        dif_list = request.form.to_dict()
        delete_items(og_list,dif_list)

    list = get_overview_orders()
    print("")
    print("das ist return von get_overview_orders")
    print(list)
    return render_template("overview.html", menu_list= list)


@app.route("/pain" , methods=['GET', 'POST'])
def pain():
    print("nach test")
    return render_template("pain.html",  menu_list=list)