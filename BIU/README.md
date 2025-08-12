# smartRAGent

**smartRAGent** es un sistema RAG (Retrieval-Augmented Generation) diseñado para ayudar con la documentación interna de **Desic**.  
Utiliza un motor de búsqueda semántica y un modelo de lenguaje para responder preguntas basadas en la documentación interna.

---

## 📑 Tabla de Contenido

- [📂 Estructura del proyecto](#-estructura-del-proyecto)
- [📋 Prerrequisitos](#-prerrequisitos)
- [🚀 Instalación](#-instalación)
- [⚙️ Configuración](#️-configuración)
- [📄 Documentos fuente](#-documentos-fuente)
- [▶️ Ejecución](#️-ejecución)
- [🔄 Diagrama de flujo](#-diagrama-de-flujo)
- [📌 Notas](#-notas)
- [📜 Licencia](#-licencia)

---

## 📂 Estructura del proyecto

```
SMARTRAGENT_LOCAL/
│
├── logs/                       # Archivos de logs de la aplicación
├── sql/                        # Scripts SQL o base de datos
├── src/
│   ├── backend/                # Lógica de negocio y procesamiento de datos
│   │   ├── faiss_index_global/
│   │   ├── faiss_index_normativas/
│   │   ├── chat_db.py
│   │   ├── embedding_model.pkl
│   │   ├── main.py
│   │   ├── model_handler.py
│   │   ├── preprocesar_pdfs.py
│   │   └── __init__.py
│   │
│   ├── frontend/               # Interfaz de usuario
│   │   ├── .streamlit/
│   │   ├── components/
│   │   ├── img/
│   │   ├── app.py
│   │   └── __init__.py
│
├── static_sources/             # Recursos estáticos
│   └── data/
│   └── Documents/              # Carpeta con PDFs que serán procesados
├── config.py                   # Configuración del proyecto
├── config.yaml                 # Configuración YAML
├── launcher.py                 # Script de inicio
├── run_app.py                  # Script principal de ejecución
├── setup.py                    # Instalación del proyecto
├── requirements.txt            # Dependencias de Python
└── README.md
```

---

## 📋 Prerrequisitos

Antes de instalar y ejecutar **smartRAGent**, asegúrate de contar con:

- **Python** 3.9 o superior  
- **pip** actualizado (`pip install --upgrade pip`)  
- **Git** para clonar el repositorio  
- Sistema operativo compatible: **Windows**, **Linux** o **macOS**  
- Acceso a internet para instalar dependencias  

---

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
   git clone tengo_que _cambiar_la_ruta.git
   cd smartRAGent
```

2. **Instalar dependencias**
```bash
   pip install --upgrade pip
   pip install -r requirements.txt
```

---

## ⚙️ Configuración

El proyecto utiliza un archivo `config.yaml` para parámetros como rutas de datos, modelos, imágenes y opciones de conexión.  
Asegúrate de configurarlo antes de ejecutar la aplicación.

Ejemplo:
```yaml
database_path:    "sql/chat_history.db"
faiss_index_path: "src/backend/faiss_index_global"
embedding_model:  "src/backend/embedding_model.pkl"
documents_path:   "static_sources/data/Documents"
```

---

## 📄 Documentos fuente

Los PDFs que se desean indexar deben colocarse en:

```bash
   static_sources/data/Documents
```
El script preprocesar_pdfs.py tomará los archivos de esa carpeta, extraerá su contenido y lo transformará en embeddings que serán almacenados en el índice FAISS para su posterior uso.

---

## ▶️ Ejecución

1. **Preprocesar documentos PDF**  
Este paso construye el índice FAISS a partir de la documentación interna.

```bash
   python src/backend/preprocesar_pdfs.py
```

2. **Iniciar el backend**
```bash
   python src/backend/main.py
```

3. **Iniciar el frontend (Streamlit)**
```bash
   streamlit run src/frontend/app.py
```

4. **O ejecutar todo con el lanzador**
```bash
   python launcher.py
```

---

## 🔄 flowchart TD
```mermaid
    A[📂 PDFs en static_sources/data/Documents] --> B[🛠 preprocesar_pdfs.py]
    B --> C[✂️ Extracción de texto]
    C --> D[🧠 Generación de embeddings]
    D --> E[💾 Almacenamiento en índice FAISS]
    E --> F[🤖 Backend recibe pregunta]
    F --> G[🔍 Recuperación de documentos relevantes]
    G --> H[📝 Respuesta generada por el modelo LLM]
```

![Flujo de SmartRAGent](static_sources/img/flow_smartRAGent.png)

---

## 📌 Notas

- **smartRAGent** utiliza FAISS para búsquedas semánticas y un modelo de embeddings (`embedding_model.pkl`).
- Los PDFs a indexar deben colocarse en static_sources/data/Documents antes de ejecutar preprocesar_pdfs.py.
- El sistema está optimizado para entornos internos de Desic.

---

## 📜 Licencia

Este proyecto es de uso interno de **Desic** y no debe compartirse fuera de la organización.
