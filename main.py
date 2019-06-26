from flask import Flask,render_template,request,redirect,url_for,flash
from dbconnect import connection,MySQLdb
app=Flask(__name__)
app.config['SECRET_KEY']='672d71e37b0b1164c3fa5613c6892902'
@app.route("/")
@app.route("/view")
def view():
    c,conn=connection()
    c.execute("SELECT * FROM employee")
    data=c.fetchall()
    return render_template("home.html",data=data)

@app.route("/add_emp",methods=['GET','POST'])
def add_emp():
    if request.method=='POST':
        name=request.form['name']
        desig=request.form['desig']
        address=request.form['address']
        phone=request.form['phone']
        c,conn=connection()
        c.execute("INSERT INTO employee(name,desig,address,phone) VALUES(%s,%s,%s,%s)",[name,desig,address,phone])
        conn.commit()
        flash(f'Employee added successfully!','success')
    return render_template("add_emp.html")

@app.route("/delete")
def delete():
    phone=request.args.get('phone')
    print(phone)
    c,conn=connection()
    c.execute("DELETE FROM employee WHERE phone=%s",[phone])
    conn.commit()
    flash(f'Record Deleted successfully!','success')
    return redirect(url_for('view'))

@app.route("/search",methods=['GET','POST'])
def search():
    if request.method=='POST':
        search=request.form['search']
        c,conn=connection()
        c.execute("SELECT * FROM employee WHERE phone=%s OR name=%s OR desig=%s",(search,search,search))
        data=c.fetchall()
        print(data)
    return render_template("search.html",data=data)

if __name__=='__main__':
    app.run(debug=True)
