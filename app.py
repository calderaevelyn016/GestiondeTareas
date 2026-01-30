from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "clave_secreta"

tareas = [
    {
        "id": 1,
        "titulo": "Aprender Flask",
        "descripcion": "Backend con Python",
        "completada": True,
        "fecha": datetime.now()
    },
    {
        "id": 2,
        "titulo": "Practicar Bootstrap",
        "descripcion": "Frontend responsive",
        "completada": False,
        "fecha": datetime.now()
    },
    {
        "id": 3,
        "titulo": "Desplegar aplicación",
        "descripcion": "",
        "completada": False,
        "fecha": datetime.now()
    }
]

@app.route("/")
def index():
    total = len(tareas)
    completadas = len([t for t in tareas if t["completada"]])
    pendientes = total - completadas
    return render_template(
        "index.html",
        tareas=tareas,
        total=total,
        completadas=completadas,
        pendientes=pendientes
    )

@app.route("/agregar", methods=["POST"])
def agregar():
    titulo = request.form.get("titulo")

    if not titulo:
        flash("El título es obligatorio", "danger")
        return redirect(url_for("index"))

    descripcion = request.form.get("descripcion", "")

    nueva_tarea = {
        "id": tareas[-1]["id"] + 1 if tareas else 1,
        "titulo": titulo,
        "descripcion": descripcion,
        "completada": False,
        "fecha": datetime.now()
    }

    tareas.append(nueva_tarea)
    flash("Tarea agregada correctamente", "success")
    return redirect(url_for("index"))

@app.route("/completar/<int:id>")
def completar(id):
    for tarea in tareas:
        if tarea["id"] == id:
            tarea["completada"] = not tarea["completada"]
            flash("Estado de la tarea actualizado", "info")
            break
    return redirect(url_for("index"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    global tareas
    tareas = [t for  t in tareas if t["id"] != id]
    flash("Tarea eliminada correctamente", "warning")
    return redirect(url_for("index"))

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("error.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
