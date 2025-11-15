from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# rota para página principal usando template
@app.route('/')
def index():
    # passamos variáveis para o template como kwargs
    return render_template('index.html', title='Página Inicial', user='Vinícius')

# outra rota que usa um template diferente
@app.route('/about')
def about():
    return render_template('about.html', title='Sobre')

# exemplo de servir um arquivo HTML estático (caso você tenha um .html direto em static)
@app.route('/manual')
def manual():
    return send_from_directory('static', 'manual.html')

if __name__ == '__main__':
    # debug True só para desenvolvimento
    app.run(debug=True, host='0.0.0.0', port=5000)
