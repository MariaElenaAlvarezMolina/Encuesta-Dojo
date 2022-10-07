from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

app.secret_key = "llave secreta"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def proceso():

    session['nombre'] = request.form['nombre']
    session['dojos'] = request.form['dojos']
    session['lenguaje'] = request.form['lenguaje']
    session['comentario'] = request.form['comentario']

    return redirect('/result')

@app.route('/result')
def info():
    return render_template('info.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)