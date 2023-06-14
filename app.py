from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

tarefas = []

#Rota da Página Inicial
@app.route('/')
def index():
    return render_template('paginas/index.html')

#Rota para listar todas as Tarefas
@app.route('/lista')
def lista():
    return render_template('paginas/lista.html', tarefas=tarefas)

#Rota para Adicionar Tarefas
@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        tarefa = {'id': len(tarefas), 'nome': nome}
        tarefas.append(tarefa)
        return redirect('lista')
    else:
        return render_template('paginas/adicionar.html')

#Rota para escolher qual Tarefa Editar
@app.route('/editar')
def editarLista():
    return render_template('paginas/editar_lista.html', tarefas=tarefas)  

#Rota para editar a Tarefa Específica
@app.route('/editar/<int:id>', methods=['GET','POST'])
def editarTarefa(id):
    tarefa = next((tarefa for tarefa in tarefas if tarefa['id'] == id), None)

    if tarefa:
        if request.method in ['POST', 'PUT']:
        # Verifica se o campo oculto method contém o valor PUT
            if request.form.get('method') == 'PUT':
                tarefa['nome'] = request.form['nome']
                return redirect('/editar')
        return render_template('paginas/editar.html', tarefa=tarefa)
    return 'Tarefa não encontrada'

#Rota para escolher qual Tarefa Excluir
@app.route('/excluir')
def excluirLista():
    return render_template('paginas/excluir_lista.html', tarefas=tarefas)  

#Rota para excluir a Tarefa Específica
@app.route('/excluir/<int:id>', methods=['POST'])
def excluirTarefa(id):
    
    if len(tarefas) != 0:
    # Verifica se o campo oculto method contém o valor DELETE
      if request.form['method'] == 'DELETE':
        del tarefas[id]
        return redirect('/excluir')
        
    else:
        return redirect('/excluir')

if __name__ == '__main__':
    app.run(debug=True)