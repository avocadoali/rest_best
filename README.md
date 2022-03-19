# Restaurant Bestell Webseite



@app.route("/list" , methods=['GET', 'POST'])
def menu():
    if request.method =='GET':
        list = get_menu_all()
        len_list = len(list) + 1
        print("this ist the menu")
        print(list)
        return render_template("list-view.html",  menu_list=list)

    selection = request.form.to_dict()
    print("this is the cart")
    print(selection)

    menu = get_menu_all
#    print(menu)
#    for x in selection:
#        if selection[x] != '':
#            menu[x].append(selection[x])
#
    session["cart_selection"] = menu
    return "hello"

@app.route("/cart" , methods=['GET', 'POST'])
def cart():
    print("this is the cart")
    print(session["menu_selection"])
    return render_template("cart.html", list_cart = session["menu_selection"])
 
