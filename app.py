from flask import Flask,render_template,request,redirect,url_for,flash
import sqlite3 as sql


app=Flask(__name__)
app.secret_key="admin123"

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        username1=request.form.get("uname")
        password1=request.form.get("pword")
        conn=sql.connect("log.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("select * from user where username=?and password=?",(username1,password1))
        data=cur.fetchone()
        if data is not None:
            return redirect(url_for('dashboard'))
        else:
            flash ("Invalid username and password")
    return render_template("login.html")
    

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        username=request.form.get("uname")
        password=request.form.get("pword")
        conn=sql.connect("log.db")
        cur=conn.cursor()
        cur.execute("insert into user (username,password) values (?,?)",(username,password))
        conn.commit()
        flash("Successfully Registered")
        return redirect(url_for('home'))
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    flash("Loggedout successfully")
    return render_template("dashboard.html")



if __name__=="__main__":
    app.run(debug=True)