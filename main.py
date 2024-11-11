from flask import Flask, jsonify, render_template_string, abort
from flasgger import Swagger
import random

app = Flask(__name__)

# Configuración de Swagger
swagger = Swagger(app)

# Definimos los sistemas y sus códigos correspondientes
systems = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

# Variable global para almacenar el sistema dañado
damaged_system = random.choice(list(systems.keys()))

# Primera Llamada: Retorna el sistema dañado
@app.route('/status', methods=['GET'])
def get_status():
    """
    Obtener el sistema dañado
    ---
    responses:
      200:
        description: Retorna el sistema dañado
        schema:
          type: object
          properties:
            damaged_system:
              type: string
              description: Sistema dañado
              example: "engines"
    """
    return jsonify({"damaged_system": damaged_system})

# Segunda Llamada: Retorna la página de reparación con el código adecuado
@app.route('/repair-bay', methods=['GET'])
def get_repair_bay():
    """
    Página de reparación con el código del sistema dañado
    ---
    responses:
      200:
        description: Página HTML con el código en el <div> con clase "anchor-point"
        content:
          text/html:
            schema:
              type: string
              example: "<div class='anchor-point'>ENG-04</div>"
    """
    system_code = systems.get(damaged_system, "UNKNOWN")
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{system_code}</div>
    </body>
    </html>
    """
    return render_template_string(html_content)

# Tercera Llamada: Retorna un código HTTP 418 (I'm a teapot)
@app.route('/teapot', methods=['POST'])
def post_teapot():
    """
    Retorna un código 418
    ---
    responses:
      418:
        description: I'm a teapot
    """
    return abort(418)

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
