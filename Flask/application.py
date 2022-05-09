from flask_mysqldb import MySQL
from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'codio'
app.config['MYSQL_DB'] = 'students'
mysql = MySQL(app)
sess = Session()

"""
@app.route('/')
def hello():
    return 'hello world'
@app.route('/index')
def index():
    query = "SELECT score from grades;"
    cursor = mysql.connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return render_template('index.html', scores=results)
"""
@app.route('/', methods=["GET", "POST"])
def select():
    if request.method == "GET":
        return render_template('select.html')
    if request.method == "POST":
        return redirect(url_for('results'))

@app.route('/results',methods=['GET', 'POST'])
def results():
    if request.method == "POST":
        course=request.form.get("course")
        print(course)
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT score,surname,forename FROM grades WHERE module_code = %s",(course,))
        score = cursor.fetchall()
        cursor.close()
        return render_template('results.html', results=score)

if __name__ == '__main__':
    app.run(host='0.0.0.0')