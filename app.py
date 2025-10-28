from flask import Flask, render_template, url_for, request, redirect, flash, session

app = Flask(__name__)
app.secret_key = 'una_clave_secreta_muy_segura_y_larga' 

USERS = []
USERS.append({'nombre': 'Usuario', 'apellido': 'Prueba', 'email': 'test@correo.com', 'password': '1234'})

def login_required(f):
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            flash('Necesitas iniciar sesión para ver esta página.', 'warning')
            return redirect(url_for('login')) 
        kwargs['user_logged_in'] = True
        kwargs['user_nombre'] = session.get('user_nombre', 'Explorador')
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    decorated_function.__doc__ = f.__doc__
    return decorated_function

@app.route('/inicioS', methods=['GET', 'POST'])
def login():
    if 'user_email' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email_login = request.form.get('email_login')
        password_login = request.form.get('contraseña_login')
        
        user_found = None
        for user in USERS:
            if user['email'] == email_login and user['password'] == password_login:
                user_found = user
                break
        
        if user_found:
            session['user_email'] = user_found['email']
            session['user_nombre'] = user_found['nombre']
            flash(f"¡Bienvenido, {user_found['nombre']}! Has iniciado sesión correctamente.", 'success')
            return redirect(url_for('home'))
        else:
            flash('Fallo al iniciar sesión. Verifica tu correo y contraseña.', 'danger')
            return render_template('login.html', title='Iniciar Sesión') 

    return render_template('login.html', title='Iniciar Sesión')

@app.route('/logout')
def logout():
    session.pop('user_email', None)
    session.pop('user_nombre', None) 
    flash('Has cerrado sesión exitosamente.', 'info')
    return redirect(url_for('login')) 

@app.route('/')
@login_required
def home(user_logged_in, user_nombre):
    info = f"¡Hola {user_nombre}! Bienvenido a la página principal. (Sesión iniciada como: {session.get('user_email')})"
    return render_template('inicio.html', title='Inicio', info=info, user_logged_in=user_logged_in, user_nombre=user_nombre)

@app.route('/animales_exoticos')
@login_required 
def animales_exoticos(user_logged_in, user_nombre):
    contenido = "Esta es la parte en donde encontraras informacion acerca de los animales exoticos mas interesantes del mundo."
    return render_template('animales_exoticos.html', title='Animales Exóticos', content=contenido, user_logged_in=user_logged_in, user_nombre=user_nombre)

@app.route('/vehiculos-antiguos')
@login_required 
def vehiculos_antiguos(user_logged_in, user_nombre):
    contenido = "Esta es la parte en donde encontraras informacion acerca de los vehiculos antiguos mas interesantes del mundo."
    return render_template('vehiculos_antiguos.html', title='Vehículos Antiguos', content=contenido, user_logged_in=user_logged_in, user_nombre=user_nombre)

@app.route('/maravillas-del-mundo')
@login_required 
def maravillas_del_mundo(user_logged_in, user_nombre):
    contenido = "Esta es la parte en donde encontraras informacion acerca de las maravillas del mundo mas interesantes del mundo."
    return render_template('maravillas_del_mundo.html', title='Maravillas del Mundo', content=contenido, user_logged_in=user_logged_in, user_nombre=user_nombre)

@app.route('/acerca')
@login_required 
def acerca_(user_logged_in, user_nombre):
    contenido = "Aqui econtraras infromacion personal acerca del creador de esta pagina web."
    return render_template('acerca_.html', title='Acerca de', content=contenido, user_logged_in=user_logged_in, user_nombre=user_nombre)

@app.route('/registroh', methods=['GET', 'POST'])
def registro():
    if 'user_email' in session:
        return redirect(url_for('home'))

    error = None
    if request.method == 'POST':
        nombre = request.form.get('nombre_registro') or 'Anon'
        apellido = request.form.get('apellido_registro') or ''
        email = request.form.get('correo_registro') 
        password = request.form.get('contraseña_registro')
        confirmPassword = request.form.get('confirmarContraseña_registro')
        
        if not all([email, password, confirmPassword]):
            error = 'Todos los campos son obligatorios.'
            
        if error is None:
            for user in USERS:
                if user['email'] == email:
                    error = f'El correo electrónico "{email}" ya está registrado.'
                    break

        if error is None and password != confirmPassword:
            error = "La contraseña no coincide con la confirmación." 
        
        if error is not None:
            flash(error, 'danger')
            return redirect(url_for('registro')) 
        else:
            new_user = {
                'nombre': nombre,
                'apellido': apellido,
                'email': email,
                'password': password 
            }
            USERS.append(new_user) 
            flash('¡Tu registro ha sido exitoso! Ya puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))

    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
