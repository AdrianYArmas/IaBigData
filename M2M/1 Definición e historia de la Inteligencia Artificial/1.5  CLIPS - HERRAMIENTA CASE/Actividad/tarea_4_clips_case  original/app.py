import os
import subprocess
from flask import Flask, render_template, send_file, request
from Traductor import process_xmi_file

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('uml.html')


@app.route('/process_xmi', methods=['POST'])
def process_xmi():
    xmi_file = request.files['xmi']
    if not xmi_file:
        return "No se envió ningún archivo XMI", 400

    input_file = 'static/temp/input.xmi'
    output_file = 'static/temp/output.clp'

    xmi_file.save(input_file)

    process_xmi_file(input_file, output_file)

    try:
        return send_file(output_file, as_attachment=True)
    except FileNotFoundError:
        return "Error al generar el archivo CLIPS", 500


@app.route('/process_clips_to_java', methods=['POST'])
def process_clips_to_java():
    xmi_file = request.files['xmi']
    if not xmi_file:
        return "No se envió ningún archivo XMI", 400

    input_file = 'static/temp/input.xmi'
    output_file = 'static/temp/output.clp'
    java_file = 'static/temp/output.java'

    xmi_file.save(input_file)

    process_xmi_file(input_file, output_file)

    try:
        subprocess.run(['python', 'clipsToJava.py', output_file], check=True)

        if os.path.exists(java_file):
            return send_file(java_file, as_attachment=True)

        else:
            return "Error: El archivo Java no fue generado.", 500

    except subprocess.CalledProcessError as e:
        return f"Error al ejecutar clipsToJava.py: {e}", 500

if __name__ == '__main__':
    app.run()
