from flask import Flask, render_template, request, redirect, url_for
from database import create_table, add_result, get_all_results, get_result_by_id
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

app = Flask(__name__)
app.secret_key = 'a-random-secret-key'
create_table()

# Função para autenticar o usuário
def check_auth(username, password):
    # Substituir por um método seguro de armazenamento e recuperação de informações de autenticação
    users = {
        'admin': generate_password_hash('adminpassword')
    }
    if username in users and check_password_hash(users.get(username), password):
        return True
    return False

# Decorador de autenticação para proteger as rotas que requerem autenticação
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/auth')
def auth():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return 'Falha na autenticação', 401
    return redirect(url_for('show_all_results'))

@app.route('/')
@requires_auth
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
@requires_auth
def result():
    url = request.form['url']
    seo = request.form['seo']
    vulnerability = request.form['vulnerability']
    storage = request.form['storage']
    spam = request.form['spam']
    traffic = request.form['traffic']

    add_result(url, seo, vulnerability, storage, spam, traffic)

    return redirect(url_for('show_all_results'))

@app.route('/results')
@requires_auth
def show_all_results():
    results = get_all_results()
    return render_template('result.html', results=results)

@app.route('/results/<int:result_id>')
@requires_auth
def show_result(result_id):
    result = get_result_by_id(result_id)
    return render_template('result.html', results=[result])

if __name__ == '__main__':
    app.run(debug=True)
