from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')

def me():
    return render_template("me.html")

@app.route('/login')

def login():
    return render_template("login.html")

@app.route('/dashboard',methods=['POST', 'GET'])

def dashboard():
    if request.method=="POST":
        if request.form["email"]=="medicare@gmail.com" and request.form["password"]=="IamRetailer":
            print(request.form["email"])
            print(request.form["password"])
            return render_template("dashboard.html",email_id=request.form["email"])
        else:
            return render_template("me.html")



if __name__=='__main__':
    app.debug=True
    app.run()
