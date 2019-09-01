from flask import Flask,render_template,request
import random
import sqlite3

app = Flask(__name__)

DATABASE='mydb.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/details')
def details():
    return render_template('Details.html')

@app.route('/addrec')
def addrec():
    random_number=random.randint(600001,899999)
    refno= random_number
    name= request.args.get ('name')
    email= request.args.get ('email')
    consignment_no = request.args.get('cn')
    date = request.args.get('date')
    product_name = request.args.get('pn')
    nature_of_complaint = request.args.get('noc')
    db=connect_db()
    sql = "insert into crform(refno,name, email,invoice_no, invoice_date,product_name,nature_of_complaint) values(?,?,?,?,?,?,?)"
    db.execute(sql,[refno,name,email,consignment_no,date,product_name,nature_of_complaint])#
    db.commit()
    db.close()
    return render_template('Details.html', name=name,email=email,cn=consignment_no,date=date,pn=product_name,noc=nature_of_complaint,refno=random_number)#

@app.route('/registrationform')
def registrationform():
    return render_template('RegistrationForm.html')

@app.route('/retrieveform')
def retrieveform():
    return render_template('RetrieveForm.html')

@app.route('/showdetails')
def showdetails():
    print('successfully done')
    db=connect_db()
    cur = db.cursor()
    refno = request.args.get('Enter Reference number')
    cur.execute("select name,email,invoice_no,invoice_date,product_name,nature_of_complaint,status from crform where refno="+str(refno))
    rows = cur.fetchall()
    return render_template('Result.html',rows= rows)

@app.route('/result')
def result():
    print('hi there i am printed')
    return render_template('Result.html')


if __name__=='__main__':
    app.run(debug=True)

