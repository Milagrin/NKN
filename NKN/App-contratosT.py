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
    cur.execute('SELECT * FROM contrato')
    datos = cur.fetchall()
    return render_template('contratos_trabajadores.html', contrato = datos)

@app.route('/edit_contrato/<string:Rut>')
def get_contrato(Rut):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contrato WHERE rut_propietario = %s',(Rut))
    datos = cur.fetchall()
    return render_template('update-contratos.html', contrato = datos[0])
    
@app.route('/update/<string:rut>', methods = ['POST'])
def update_contratos(rut):
    if request.method == 'POST':
        rut1 = request.form['Rut']
        nombre = request.form['Nombre']
        fechaI = request.form['FechaI']
        fechaT = request.form['FechaT']
        tipoC = request.form['tipoContrato']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contrato
            SET rut_propietario = %s,
                nombre_propietario = %s,
                fecha_inicio = %s,
                fecha_termino = %s,
                tipo_contrato = %s
                WHERE rut_propietario = %s
        """, (rut1,nombre,fechaI,fechaT,tipoC,rut))
        mysql.connection.commit()
        flash('Contrato actualizado correctamente')
        return redirect(url_for('contratos_index'))

@app.route('/delete_contrato/<string:rut>')
def delete_contrato(rut):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contrato WHERE rut_propietario = {0}'.format(rut))
    mysql.connection.commit()
    flash('Contrato eliminado correctamente')
    return redirect(url_for('contratos_index'))

if __name__ == '__main__':
    app.run(port=3003,debug=True)