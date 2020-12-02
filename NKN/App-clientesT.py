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
def clientes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente')
    datos = cur.fetchall()
    return render_template('clientes_trabajadores.html', clientes = datos)


@app.route('/edit_cliente/<string:rut>')
def get_cliente(rut):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cliente WHERE rut =%s', (rut))
    dato = cur.fetchall()
    return render_template('update-cliente.html', clientes = dato[0])

@app.route('/update/<string:rut>', methods = ['POST'])
def update_clientes(rut):
    if request.method == 'POST':
        rut1 = request.form['Rut']
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
        cur.execute("""
            UPDATE cliente 
            SET rut = %s,
                nombre_completo = %s,
                apellidos = %s,
                email = %s,
                fono = %s,
                fecha_nac = %s,
                sexo = %s,
                direccion = %s,
                pais = %s,
                region = %s,
                ciudad = %s
            WHERE rut = %s
        """, (rut1,nombre,apellidos,email,fono,fecha_nac,sexo,direccion,pais,region,ciudad, rut))
        mysql.connection.commit()
        flash ('Cliente actualizado correctamente')
        return redirect(url_for('clientes'))

@app.route('/delete_cliente/<string:rut>')
def delete_cliente(rut):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM cliente WHERE rut = {0}'.format(rut))
    mysql.connection.commit()
    flash('Cliente eliminado correctamente')
    return redirect(url_for('clientes'))

if __name__ == '__main__':
    app.run(port=3001,debug=True)