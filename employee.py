from flask import *
from EMP import *
import mysql.connector

f=Flask(__name__)

conn=mysql.connector.connect(host='localhost', user='root', password='', database='rakshita_db')
cursor=conn.cursor()

@f.route('/')
def index():
    return render_template("home.html")

@f.route('/register')
def register_emp():
    return render_template("register.html")

@f.route('/master')
def master():
    return render_template("master.html")

@f.route('/addEmp',methods=['POST'])
def add_emp():
    id=request.form['id']
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    cont=request.form['cont']
    dept=request.form['dept']
    t=(id,name,email,password,cont,dept)
    addEmp(t)
    return render_template('login.html')

@f.route('/login')
def login_emp():
    return render_template("login.html")
@f.route("/login_validation", methods=['POST'])
def login():
    id = request.form.get("id")
    password = request.form.get("password")
    cursor.execute(""" SELECT * FROM `empf` WHERE `id` LIKE '{}' AND `password` LIKE '{}'"""
                   .format(id,password))
    emps=cursor.fetchall()
    if len(emps)>0:
        return render_template('master.html')
    else:
        return render_template('login.html',login="Enter Valid ID and Password")
    
@f.route('/getlist')
def get_list():
    el=getEmpList()
    return render_template('emplist.html',elist=el)

@f.route('/deleteEmp')
def delete_emp():
    id=request.args.get("id")
    deleteEmp(id)
    return redirect('/getlist')

@f.route('/editEmp')
def edit_emp():
    id=request.args.get("id")
    e=getEmpById(id)
    return render_template("updateemp.html",emp=e)

@f.route('/updateEmp',methods=['POST'])
def update_emp():
    id=request.form['id']
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    cont=request.form['cont']
    dept=request.form['dept']
    t=(name,email,password,cont,dept,id)
    updateEmp(t)
    return redirect('/getlist')

        

if __name__=='__main__':

    f.run(debug=True)
