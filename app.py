from flask import Flask, render_template,abort,request
import json
with open("MSX.json") as fichero:
    datos=json.load(fichero)
app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")

@app.route('/listajuegos',methods=['POST'])
def listajuegos():
    cad=request.form.get("cadena")
    juegos=[]
    for i in datos:
        juego=str(i.get("nombre"))
        if juego.lower()[0:len(cad)] == cad.lower():
            dic={"nombre":i.get("nombre"),"desarrollador":i.get("desarrollador"),"id":i.get("id")}
            juegos.append(dic)
    return render_template("listajuegos.html",juegos=juegos)
app.run('0.0.0.0',5000, debug=True)
