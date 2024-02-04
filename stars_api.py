from flask import Flask, jsonify, request
from data import data

#Crie dois endpoints:
app= Flask(__name__) 

# 1) para exibir os dados de todas as estrelas


@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success",

    }), 200


# 2) para exibir os dados de uma estrela especificda na rota

@app.route("/star")
def planet():
    name= request.args.get("name")
    stars_data= next(item for item in data if item["name"]== name)
    return jsonify({
        "data": stars_data,
        "message": "success"
    }), 200


if __name__ == "__main__":
    app.run()
