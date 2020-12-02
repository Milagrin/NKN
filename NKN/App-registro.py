from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_NKN'
mysql = MySQL(app)

#Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/add_user_view')
def add_user_view():
    return render_template('login.html')

@app.route('/add_user', methods = ['POST'])
def add_user():
    if request.method == 'POST':
        rut = request.form['rut']
        nombre = request.form['nombre']
        gmail = request.form['gmail']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        cur = mysql.connection.cursor()

        cur.execute("""
            INSERT INTO registro_sesion (rut, nombre_completo,gmail,nombre_usuario,contrasena) VALUES(%s, %s, %s, %s, SHA2(%s, 512))
        """, (rut, nombre,gmail,usuario,contrasena))

        mysql.connection.commit()
        return redirect(url_for('login'))

@app.route('/verifyLogin', methods = ['POST'])
def verifyLogin():
    if request.method == 'POST':
        gmail = request.form['gmail']
        contrasena = request.form['contrasena']
        cur = mysql.connection.cursor()

        cur.execute("""
            SELECT gmail FROM registro_sesion WHERE gmail = %s AND contrasena = SHA2(%s, 512)
        """, (gmail, contrasena))

        cur.fetchall()

        verify = cur.fetchall()

        if verify == None:
            flash('Datos incorrectos')
            return(redirect(url_for('/')))
        else:
            return redirect(url_for('static, filename = index_trabajadores.html'))

        

if __name__ == '__main__':
    app.run(port=3004,debug=True)