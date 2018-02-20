import dataset 

from flask import Flask, render_template

app = Flask('noticias')

def conexao():
    return dataset.connect('sqlite:///noticias.db')

@app.route('/')
def index():
    titulo = 'Notícias - Vanilton'
    tabela_noticias = conexao()['noticias']
    noticias = [
        'Noticia 1', 'Noticia 2', 'Noticia 3'
    ]
    return render_template('index.html', titulo=titulo, noticias=tabela_noticias )


@app.route('/noticias/<int:noticia_id>')
def noticia_detalhe(noticia_id):
    tabela_noticias = conexao()['noticias']
    noticia = tabela_noticias.find_one(id=noticia_id)
    return render_template('detalhe_noticia.html', noticia=noticia)

    

app.config['DEBUG'] = True
app.run()