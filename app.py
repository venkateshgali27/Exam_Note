
from flask import Flask, render_template, request
import mysql.connector
import os 

app = Flask(__name__,static_folder='static',template_folder='template')
en_config=os.getenv("PROD_APP_SETTINGS","config.DevelopmentConfig")

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Venkatesh@91',
    'database': 'mydatabase'
}
from jinja2 import Environment, FileSystemLoader

# Specify the template directory explicitly
template_dir = '/path/to/template'
env = Environment(loader=FileSystemLoader(template_dir))

# Now you can render your template
template = env.get_template('H login page.html')
@app.route('/')
def index():
    return render_template('Home page.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    insert_query = "INSERT INTO userdetails (name, email) VALUES (%s, %s)"
    values = (name, email)
    cursor.execute(insert_query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return 'Data Submitted successfully, go to previous page!'

@app.route('/About us')
def about_page():
    return render_template('About us.html')

@app.route('/Contact us')
def menu_page():
    return render_template('Contact us.html')

@app.route('/Log in page')
def Login_page():
    return render_template('Log in page.html')

@app.route('/Home page')
def Home_page():
    return render_template('Home page.html')

@app.route('/Instruction page')
def Inst_page():
    return render_template('Instruction page.html')

@app.route('/Other Important Instructions page')
def Othimpinst_page():
    return render_template('Other Important Instructions page.html')

@app.route('/Exam paper')
def Exampaper_page():
    return render_template('Exam paper.html')

@app.route('/H Login page')
def Hlogin_page():
    return render_template('H login page.html')

@app.route('/H Instruction page')
def HInst_page():
    return render_template('H Instruction page.html')


@app.route('/H Other Important Instructions page')
def Hothimpinst_page():
    return render_template('H Other Important Instructions page.html')


@app.route('/Hexaware paper')
def Hpaper_page():
    return render_template('Hexaware paper.html')

if __name__ == '__main__':
    app.run(debug=True)
