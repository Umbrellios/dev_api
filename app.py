from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [{
                    'id':'0',
                    'nome': 'Braulio',
                    'habilidades':['PHP','Python','Flask']
                    },
                   {
                    'id':'1',
                    'nome':'Santos',
                    'habilidades':['HTML','Java']}
                   ]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': 'Desenvolvedor e ID {} não existe'.format(id)}
        except Exception:
            mensagem = 'Erro Desconhecido'
            response = {'status':'erro', 'mensagem':mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

#lista todos os desenvolvedores e inclui um novo desenvolvedor
@app.route('/dev/', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)