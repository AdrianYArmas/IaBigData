import os
import logging
import clips

def generate_java(clips_file):
    if not os.path.exists(clips_file):
        raise FileNotFoundError(f"El archivo CLIPS '{clips_file}' no existe.")

    logging.basicConfig(level=logging.DEBUG, format='%(message)s', filename="static/temp/output.java", filemode='w')
    # Crear el entorno CLIPS
    env = clips.Environment()
    router = clips.LoggingRouter()
    env.add_router(router)
    # Cargar el archivo CLIPS
    env.load(clips_file)
    env.reset()
    env.run()

    return os.path.abspath("static/temp/output.java")

if __name__ == "__main__":
    clips_file = "static/temp/output.clp"

    try:
        java_file_path = generate_java(clips_file)
        print(f"Código Java generado en: {java_file_path}")
    except Exception as e:
        print(f"Error: {e}")