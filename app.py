

from flask  import Flask, render_template,url_for,request,redirect,flash


app = Flask(__name__)


@app.route('/inicioSE')
def index():
    """Ruta de inicio. Redirige a login."""
    return redirect(url_for('inicioSesion'))

@app.route('/inicioS', methods=['GET', 'POST'])
def inicioSesion():
    """Ruta para la página de Inicio de Sesión."""
    if request.method == 'POST':
        email = request.form.get('email_inicioSesion')
        contraseña = request.form.get('contraseña_inicioSesion')

        if email == "test@correo.com" and contraseña == "1234":
            flash('¡Bienvenido! Has iniciado sesión correctamente.', 'success')
            return redirect(url_for('inicio'))
        else:
            flash('Fallo al iniciar sesión. Verifica tu correo y contraseña.', 'danger')

    return render_template('inicioSesion.html', title='Iniciar Sesión')

        
        
        
        
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



        
        
        
        









if __name__ == '__main__':
    app.run(debug=True)
   