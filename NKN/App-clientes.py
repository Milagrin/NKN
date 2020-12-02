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
def clientes_index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente')
    datos = cur.fetchall()
    return render_template('clientes.html', clientes = datos)

@app.route('/agregar_cliente', methods = ['POST'])
def agregar_cliente():
    if request.method == 'POST':
        rut = request.form['Rut']
        nombre = request.form['Nombre']
        apellidos = request.form['Apellidos']
        email = request.form['Email']
        fono = request.form['Fono']
        fecha_nac = request.form['FechaNac']
        sexo = request.form['Sexo']
        direccion = request.form['Direccion']
        pais = request.form['Pais']
        region = request.form['Region']
        ciudad = request.form['Ciudad']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO cliente (rut, nombre_completo, apellidos, email, fono, fecha_nac, sexo, direccion, pais, region, ciudad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
        (rut,nombre,apellidos,email,fono,fecha_nac,sexo,direccion,pais,region,ciudad))
        mysql.connection.commit()
        flash('Usted ha sido registrado en nuestras bases de datos')
        return redirect(url_for('clientes_index'))


if __name__ == '__main__':
    app.run(port=3000,debug=True)