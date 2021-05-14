from flask import Flask, render_template,abort,request
import os
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
@app.route('/juegos/<int:num>')
def juego(num):
    game=num
    ind=0
    info=[]
    for i in datos:
        if i.get("id") == game:
            dic={"nombre":i.get("nombre"),"desarrollador":i.get("desarrollador"),"id":i.get("id"),"sistema":i.get("sistema"),"distribuidor":i.get("distribuidor"),"categoria":i.get("categoria"),"año":i.get("año")}
            info.append(dic)
            ind=1
    if ind == 0:
        abort(404)
    return render_template("juego.html",info=info)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port), debug=True)
