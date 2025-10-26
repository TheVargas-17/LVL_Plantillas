from flask import Flask, render_template, url_for, request, redirect, flash, session
# Se elimina la importación de 'wraps' para simplificar el código.

app = Flask(__name__)
# 🔑 Usamos una clave más segura para la sesión, esencial al usar 'session'
app.secret_key = 'una_clave_secreta_muy_segura_y_larga' 

# 💾 Estructura para almacenar usuarios en memoria (se pierden al reiniciar el servidor)
USERS = []

# --- Agregar un usuario de prueba (similar al que tenías antes) ---
USERS.append({'nombre': 'Usuario', 'apellido': 'Prueba', 'email': 'test@correo.com', 'password': '1234'})
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# DECORADOR PARA RESTRINGIR ACCESO
# ----------------------------------------------------------------
def login_required(f):
    """
    Decorador que redirige al login si no hay 'user_email' en la sesión.
    (Se ha simplificado eliminando @wraps(f))
    """
    def decorated_function(*args, **kwargs):
        if 'user_email' not in session:
            flash('Necesitas iniciar sesión para ver esta página.', 'warning')
            # Redirige a la función 'login' que corresponde a la ruta '/inicioS'
            return redirect(url_for('login')) 
        
        # Pasa los datos del usuario a la función decorada
        kwargs['user_logged_in'] = True
        kwargs['user_nombre'] = session.get('user_nombre', 'Explorador')
        return f(*args, **kwargs)
    
    # FIX: Estas dos líneas asignan el nombre y la documentación de la función original (f)
    # a la función envuelta (decorated_function) para que Flask la pueda registrar correctamente.
    decorated_function.__name__ = f.__name__
    decorated_function.__doc__ = f.__doc__
    
    return decorated_function

# ----------------------------------------------------------------
# RUTA ORIGINAL DE LOGIN: /inicioS
# ----------------------------------------------------------------
@app.route('/inicioS', methods=['GET', 'POST'])
def login():
    # Si el usuario ya está logueado, redirige a 'home'
    if 'user_email' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        # Se usaron los nombres de campo del código nuevo para la nueva lógica
        email_login = request.form.get('email_login')
        password_login = request.form.get('contraseña_login') # Usando el nombre del campo del formulario original
        
        user_found = None
        for user in USERS:
            # Revisa si el email y la contraseña coinciden
            if user['email'] == email_login and user['password'] == password_login:
                user_found = user
                break
        
        if user_found:
            # Inicia la sesión
            session['user_email'] = user_found['email']
            session['user_nombre'] = user_found['nombre']
            flash(f"¡Bienvenido, {user_found['nombre']}! Has iniciado sesión correctamente.", 'success')
            return redirect(url_for('home')) # Redirige a la ruta principal
        else:
            flash('Fallo al iniciar sesión. Verifica tu correo y contraseña.', 'danger')
            # Permite que el usuario intente de nuevo en el mismo formulario
            return render_template('login.html', title='Iniciar Sesión') 

    return render_template('login.html', title='Iniciar Sesión')

# ----------------------------------------------------------------
# NUEVA RUTA DE LOGOUT
# ----------------------------------------------------------------
@app.route('/logout')
def logout():
    session.pop('user_email', None)
    session.pop('user_nombre', None) 
    flash('Has cerrado sesión exitosamente.', 'info')
    # Redirige a la página de inicio de sesión
    return redirect(url_for('login')) 

# ----------------------------------------------------------------
# RUTA ORIGINAL DE HOME: /
# ----------------------------------------------------------------
@app.route('/')
@login_required # Solo accesible si hay sesión iniciada
def home(user_logged_in, user_nombre):
    info = f"¡Hola {user_nombre}! Bienvenido a la página principal. (Sesión iniciada como: {session.get('user_email')})"
    # Se pasa la información de sesión al template para personalizar la vista
    return render_template('inicio.html', 
                           title='Inicio', 
                           info=info, 
                           user_logged_in=user_logged_in, 
                           user_nombre=user_nombre)

# ----------------------------------------------------------------
# RUTAS DE CONTENIDO (se aplica login_required)
# ----------------------------------------------------------------
@app.route('/animales_exoticos')
@login_required 
def animales_exoticos(user_logged_in, user_nombre):
    contenido = "Esta es la parte en donde encontraras informacion acerca de los animales exoticos mas interesantes del mundo."
    return render_template('animales_exoticos.html', 
                           title='Animales Exóticos', 
                           content=contenido, 
                           user_logged_in=user_logged_in, 
                           user_nombre=user_nombre)

@app.route('/vehiculos-antiguos')
@login_required 
def vehiculos_antiguos(user_logged_in, user_nombre):
    contenido = "Esta es la parte en donde encontraras informacion acerca de los vehiculos antiguos mas interesantes del mundo."
    return render_template('vehiculos_antiguos.html', 
                           title='Vehículos Antiguos', 
                           content=contenido, 
                           user_logged_in=user_logged_in, 
                           user_nombre=user_nombre)

@app.route('/maravillas-del-mundo')
@login_required 
def maravillas_del_mundo(user_logged_in, user_nombre):
    contenido = "Esta es la parte en donde encontraras informacion acerca de las maravillas del mundo mas interesantes del mundo."
    return render_template('maravillas_del_mundo.html', 
                           title='Maravillas del Mundo', 
                           content=contenido, 
                           user_logged_in=user_logged_in, 
                           user_nombre=user_nombre)

@app.route('/acerca')
@login_required 
def acerca_(user_logged_in, user_nombre):
    contenido = "Aqui econtraras infromacion personal acerca del creador de esta pagina web."
    return render_template('acerca_.html', 
                           title='Acerca de', 
                           content=contenido, 
                           user_logged_in=user_logged_in, 
                           user_nombre=user_nombre)

# ----------------------------------------------------------------
# RUTA ORIGINAL DE REGISTRO: /registroh (con lógica mejorada del código nuevo)
# ----------------------------------------------------------------
@app.route('/registroh', methods=['GET', 'POST'])
def registro():
    if 'user_email' in session:
        return redirect(url_for('home'))

    error = None
    if request.method == 'POST':
        # Nota: El código nuevo usa campos 'nombre', 'apellido', 'contacto' y 'contrasena'. 
        # Asegúrate de que tu formulario 'registro.html' use estos nombres 
        # o ajústalos aquí si usa 'correo_registro' y 'contraseña_registro'.
        nombre = request.form.get('nombre_registro') or 'Anon'
        apellido = request.form.get('apellido_registro') or ''
        email = request.form.get('correo_registro') 
        password = request.form.get('contraseña_registro')
        confirmPassword = request.form.get('confirmarContraseña_registro')
        
        # Validaciones
        if not all([email, password, confirmPassword]):
            error = 'Todos los campos son obligatorios.'
            
        if error is None:
            # 1. Verificar si el correo ya existe
            for user in USERS:
                if user['email'] == email:
                    error = f'El correo electrónico "{email}" ya está registrado.'
                    break

        # 2. Verificar que las contraseñas coincidan
        if error is None and password != confirmPassword:
            error = "La contraseña no coincide con la confirmación." 
        
        if error is not None:
            flash(error, 'danger')
            return redirect(url_for('registro')) 
        else:
            # 3. Registrar nuevo usuario
            new_user = {
                'nombre': nombre,
                'apellido': apellido,
                'email': email,
                'password': password 
            }
            USERS.append(new_user) 
            flash('¡Tu registro ha sido exitoso! Ya puedes iniciar sesión.', 'success')
            return redirect(url_for('login')) # Redirige a la función de login (/inicioS)

    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)