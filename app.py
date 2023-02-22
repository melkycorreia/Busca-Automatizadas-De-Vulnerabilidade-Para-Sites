from flask import Flask, render_template, request, redirect, url_for
from database import create_table, add_result, get_all_results, get_result_by_id

app = Flask(__name__)
create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
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
def show_all_results():
    results = get_all_results()
    return render_template('result.html', results=results)

@app.route('/results/<int:result_id>')
def show_result(result_id):
    result = get_result_by_id(result_id)
    return render_template('result.html', results=[result])

if __name__ == '__main__':
    app.run(debug=True)

