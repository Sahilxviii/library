from flask import *
import dbfun as db

app= Flask(__name__)

#signup page

@app.route("/")
def signup():
    return render_template("signup.html")

@app.route("/savedata", methods=["POST"])
def savefun():
        email = request.form["email"]
        psd =   request.form["password"]
        cpsd =  request.form["cpwd"]
        un =    request.form["uname"]
        role =  request.form["role"]

        id = db.email_check(email)
        if id:
            return "try another email"

        if psd == cpsd :
            t = (email, psd, un, role)
            db.insert_fun(t)
            return redirect("/login")
        else :
            return "wrong confirm password"

# Login page 
@app.route("/login")
def login():
    return render_template("login.html")

# data access 
@app.route("/access", methods=["POST"])
def access():
    email = request.form["email"]
    psd = request.form["password"]
    t = (email,psd)
    a = db.access(t)
    if a:
        if a[1] == "student":
            return redirect ("/student") #student page

        elif a[1] == "admin":
            return redirect ("/admin")   #Admin page
    else:
        return "wrong login credentials"

#Student page 
@app.route("/student")
def student():
    data = db.library()
    return render_template("student.html", res = data)

#Admin page
@app.route("/admin")
def admin():
    data = db.library()
    return render_template("admin.html", res = data )

# add a book (Admin only)
@app.route("/add_book")
def add_book():
    return render_template("add_book.html")

@app.route("/add", methods=["POST"])
def add():
    bk_name   = request.form["book_name"]
    auth_name = request.form["auth_name"]
    pub_name  = request.form["pub_name"] 
    pages     = request.form["no_pages"]
    price     = request.form["price"]
    t = (bk_name, auth_name, pub_name, pages, price)
    db.add_book(t)
    return redirect("/admin")

# Edit a book  (Admin only)
@app.route("/edit/<int:id>")
def edit(id):
    data = db.fetch_spec(id)
    return render_template("edit.html", res = data)
    
@app.route("/update/<int:id>", methods=["POST"])
def update(id):

    bk_name   = request.form["N_bk_name"]
    auth_name = request.form["N_Auth_name"]
    pub_name  = request.form["N_pub_name"]
    pages     = request.form["N_pages"]
    price     = request.form["N_price"]

    t = (bk_name, auth_name, pub_name, pages, price, id)
    db.update(t)
    return redirect("/admin")

# Delete a Book (Admin only)
@app.route("/delete/<int:id>/")
def delete_fun(id):
    db.delete(id)
    return redirect("/admin")

if(__name__=="__main__"):
    app.run(debug=True)