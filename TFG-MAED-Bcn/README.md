Predicción de Datos Energéticos de Barcelona
=============================================

Este proyecto realiza la predicción de datos energéticos de la ciudad de Barcelona utilizando modelos de machine learning y ofrece una interfaz visual mediante Streamlit, además de una API REST construida con Flask para consultas programáticas.

Contenido
---------

- app.py: Aplicación principal con interfaz Streamlit.
- app/api.py: API REST para consultas.
- requirements.txt: Dependencias del proyecto.
- installer.bat: Script para instalación automática de Python, entorno virtual y dependencias.
- ejecutable.bat: Script para lanzar la app y la API en segundo plano.
- venv/: Entorno virtual creado por el instalador (no incluido en el repositorio).

Tabla de Contenidos
-------------------

1. Instalación Manual  
2. Instalación Automática con installer.bat  
3. Ejecución de la Aplicación con ejecutable.bat  
4. Notas  

Instalación Manual
------------------

Para instalar y preparar el proyecto manualmente en un entorno Windows:

1. Instalar Python 3.11+  
   Descarga e instala Python desde https://www.python.org/downloads/release/python-3114/.  
   Durante la instalación, asegúrate de marcar la opción "Add Python to PATH".

2. Crear entorno virtual  
   Abre una consola en la carpeta raíz del proyecto y ejecuta:

```bash
python -m venv venv
```

3. Activar entorno virtual
```bash
venv\Scripts\activate
```

4. Instalar dependencias
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
Instalación Automática con installer.bat
El proyecto incluye un script installer.bat para facilitar la instalación automática en Windows. Este script:

Comprueba si Python 3.11 está instalado.

Si no está, descarga e instala Python silenciosamente.

Crea y activa un entorno virtual venv.

Instala todas las dependencias desde requirements.txt.

Uso:

Ejecuta el archivo installer.bat haciendo doble clic o desde la consola:

```bash
installer.bat
```

Sigue las instrucciones en pantalla. Al finalizar, tendrás el entorno listo para ejecutar la aplicación.

Ejecución de la Aplicación con ejecutable.bat
Para iniciar la aplicación Streamlit y la API Flask simultáneamente, puedes usar el script ejecutable.bat. Este script:

Activa el entorno virtual si existe.

Ejecuta app/api.py en segundo plano (API Flask).

Ejecuta app.py con Streamlit, mostrando sus logs.

Muestra mensajes informativos con los URLs para acceder a la app y la API.

Uso:

Ejecuta:
```bash
ejecutable.bat
```

Luego abre en tu navegador:

Interfaz Streamlit: http://localhost:8501

API Flask: http://127.0.0.1:5000

Para detener la aplicación, simplemente cierra la ventana de consola que se abrió.

Notas
Asegúrate de ejecutar los scripts .bat con permisos adecuados, especialmente para la instalación de Python.

En caso de problemas con el PATH, reinicia la consola o añade Python manualmente al PATH.

El proyecto está optimizado para Windows debido al uso de scripts .bat.
