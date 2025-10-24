from flask import Flask, render_template, url_for, request, redirect, flash

app = Flask(__name__)
app.secret_key = '12345'  # 🔑 Necesario para usar flash()

@app.route('/inicioS', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form.get('email_login')
        contraseña = request.form.get('contraseña_login')

        if email == "test@correo.com" and contraseña == "1234":
            flash('¡Bienvenido! Has iniciado sesión correctamente.', 'success')
            return redirect(url_for('home')) 
        else:
            flash('Fallo al iniciar sesión. Verifica tu correo y contraseña.', 'danger')

    return render_template('login.html', title='Iniciar Sesión')

@app.route('/')
def home():
    return render_template('inicio.html')

@app.route('/animales-exoticos')
def animales_exoticos():
    contenido = "Esta es la parte en donde encontraras informacion acerca de los animales exoticos mas interesantes del mundo."
    return render_template('animales_exoticos.html', title='Animales Exóticos', content=contenido)

@app.route('/vehiculos-antiguos')
def vehiculos_antiguos():
    contenido = "Esta es la parte en donde encontraras informacion acerca de los vehiculos antiguos mas interesantes del mundo."
    return render_template('vehiculos_antiguos.html', title='Vehículos Antiguos', content=contenido)

@app.route('/maravillas-del-mundo')
def maravillas_del_mundo():
    contenido = "Esta es la parte en donde encontraras informacion acerca de las maravillas del mundo mas interesantes del mundo."
    return render_template('maravillas_del_mundo.html', title='Maravillas del Mundo', content=contenido)

@app.route('/acerca')
def acerca_():
    contenido = "Aqui econtraras infromacion personal acerca del creador de esta pagina web."

    return render_template('acerca_.html', title='Acerca de', content=contenido)







@app.route('/registroh', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
       
        correo = request.form.get('correo_registro')
        contraseña = request.form.get('contraseña_registro')
        confirmarContraseña = request.form.get('confirmarContraseña_registro')
        
        if contraseña != confirmarContraseña:
            flash('contraseña incorrecta', 'danger')
            return redirect(url_for('registro')) 
        
        
        if correo == "test@correo.com":
            flash('correo incorrecto', 'danger')
            return redirect(url_for('registro')) 
        
        
        else:
            flash('tu registro a sido exitoso', 'succes')

    return render_template('registro.html', title='Iniciar Sesión')
if __name__ == '__main__':
    app.run(debug=True)
