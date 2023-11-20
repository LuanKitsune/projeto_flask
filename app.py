from flask import Flask, render_template, request, redirect, url_for
 
app = Flask(__name__) 
 
@app.route('/') 
def home(): 
   return render_template('index.html') 

@app.route('/mitologia')
def mythology():
    return render_template('mythology.html')

@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':     
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        

        return redirect(url_for('sucesso'))

    return render_template('cadastro.html')
if __name__ == '__main__': 
 app.run(debug=True) 
