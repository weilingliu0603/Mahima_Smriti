import sqlite3
import flask

app = flask.Flask(__name__)

def get_db():
    db = sqlite3.connect('M&S_salon.db')
    db.row_factory = sqlite3.Row
    return db

@app.route('/')
def home():
    ##return flask.render_template('D:\COMPUTING 2020\coursemology\Pair Project\Database+Web+App+Example\templates\index.html')
    return flask.render_template('index.html')
    
@app.route('/addNewMember')
def addNewMember():
    ##return flask.render_template('D:\COMPUTING 2020\coursemology\Pair Project\Database+Web+App+Example\templates\index.html')
    return flask.render_template('addNewMember.html')
    
@app.route('/memberadded', methods=['POST']) ##new entry
def memberadded(): 
    n = flask.request.form['Name']
    p = flask.request.form['Gender']
    e = flask.request.form['Email']
    c = flask.request.form['Contact']
    a = flask.request.form['Address']
    db = get_db()
    db.execute('INSERT into MEMBER (Name, Gender, Email, Contact, Address) VALUES (?,?,?,?,?)',(n,p,e,c,a))
    db.commit()
    db.close()
    return flask.render_template('itemadded.html',n=n)

@app.route('/addTransaction')
def addTransaction():
    ##return flask.render_template('D:\COMPUTING 2020\coursemology\Pair Project\Database+Web+App+Example\templates\index.html')
    return flask.render_template('addTransaction.html')

@app.route('/transactionAdded', methods=['POST']) ##new entry
def transactionAdded(): 
    p = flask.request.form['MemberID']
    e = flask.request.form['Name']
    c = flask.request.form['Date']
    a = flask.request.form['TotalAmount']
    db = get_db()
    db.execute('INSERT into TRANSACTION (MemberID, Name, DateOfTransaction, TotalAmount) VALUES (?,?,?,?)',(p,e,c,a))
    db.commit()
    db.close()
    return flask.render_template('itemadded.html',n=e)
    
@app.route('/updateMember')    
def updateMember():
    return flask.render_template('index.html') #updateMember.html not coded yet
@app.route('/viewRevenue')
def viewRevenue():
    return flask.render_template('index.html') #viewRevenue.html not coded yet
@app.route('/DailyTransaction')
def DailyTransaction():
    return flask.render_template('index.html') #DailyTransaction.html not coded yet
@app.route('/tranHistory')
def tranHistory():
    return flask.render_template('index.html') #tranHistory.html not coded yet

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



