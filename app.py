from flask  import Flask, render_template

app = Flask(__name__)



@app.route('/inicio')
def inicio():
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
    return render_template('acerca.html', title='Acerca de', content=contenido)

if __name__ == '__main__':
    app.run(debug=True)