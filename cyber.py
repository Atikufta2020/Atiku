from flask import Flask, render_template, request, redirect
from db import mydb, mycursor


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        city = request.form['city']
        gender = request.form['gender']
        sql = 'INSERT INTO user (name, dob, email, phone, address, city, gender ) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        val = (name, dob, email, phone, address, city, gender)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/')
    
    
@app.route('/sub') 
def sub(): 
    return render_template('items.html')  

#@app.route('/items')
#def item():
    #mycursor.execute("SELECT * FROM book")
    #book = mycursor.fetchall()
    #return render_template('items.html', book = book)



if __name__ == '__main__':
    app.run(debug=True)