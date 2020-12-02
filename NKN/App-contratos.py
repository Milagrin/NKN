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
def contratos_index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contrato")
    datos = cur.fetchall()
    return render_template('contratos.html', contratos = datos)

@app.route('/agregar_contrato', methods = ['POST'])
def agregar_contrato():
    if request.method == 'POST':
        rut = request.form['Rut']
        nombre = request.form['Nombre']
        fechaI = request.form['FechaI']
        fechaT = request.form['FechaT']
        tipoC = request.form['tipoContrato']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contrato (rut_propietario, nombre_propietario, fecha_inicio, fecha_termino, tipo_contrato) VALUES (%s,%s,%s,%s,%s)", (rut,nombre,fechaI,fechaT,tipoC))
        mysql.connection.commit()
        flash('Su registro de nuevo contrato a sido enviado a nuestros trabajadores')
        return redirect(url_for('contratos_index'))


if __name__ == '__main__':
    app.run(port=3002,debug=True)