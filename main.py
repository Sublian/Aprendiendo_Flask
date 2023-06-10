from flask import Flask, redirect, url_for, render_template
#creamos instancia de flask
app = Flask(__name__)

@app.route('/')
def index():
    #pasando una variable
    #encabezado = "Encabezado desde Flask"
    #pasando un diccionario
    datos={'titulo': 'Pagina principal', 
           'encabezado': 'Bienvenido a mi pagina de prueba'}
    return render_template('index.html', dato=datos)
#    return "Hola desde tu servidor Flask, recibiendo datos"
@app.route('/acerca')
def acerca():
    datos={'titulo': 'Pagina Acerca', 
           'encabezado': 'Aqui hablare sobre mi '}
    #return "<h1>Acerca de mi</h1>"
    return render_template('acerca.html',dato=datos)

#recibiendo parametros
@app.route('/saludame')
@app.route('/saludame/<string:nombre>')
@app.route('/saludame/<string:nombre>/<int:edad>')
def saludame(nombre='Luis', edad=None):
    if edad !=None :        
        return f"Saludos, <h3>{nombre}</h3>, tienes {edad}"
    return f"Como estas, <h3>{nombre}</h3>"

@app.route('/suma')
@app.route('/suma/<int:num1>/<int:num2>')
def suma(num1=None, num2=None):
    if num1==None and num2==None:
        return "Bienvenidos al modulo de suma!"
    return f"La sumatoria es: {num1+num2}"

#redireccionamiento
@app.route('/redirecciona')
@app.route('/redirecciona/<string:sitio>')
def redirecciona(sitio=None):
    if sitio is not None:
        return redirect(url_for('index'))
    return redirect(url_for('acerca'))
    

if __name__ == '__main__':
    app.run(debug=True, port=5000)