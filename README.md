# VITAWALLET-TEST


## Descripción del Proyecto

Este repositorio contiene la prueba ténica para la empresa **VitaWallet**. El proyecto está desarrollado en **Python** y utiliza **Pytest** como *framework* principal para la ejecución de pruebas.

Está diseñado siguiendo un patrón de diseño **Page Object Model (POM)** para mejorar la mantenibilidad y la reutilización del código de prueba.

---

## Estructura del Proyecto

La estructura de carpetas refleja la organización del *framework* de pruebas:

* `VITAWALLET-TEST/`
    * `data/`: Contiene archivos con los datos de prueba (e.g., archivos CSV, JSON, o *fixtures* de datos).
    * `locators/`: Contiene los archivos con los **localizadores** (IDs, XPath, selectores CSS) de los elementos de la interfaz de usuario.
    * `pages/`: Contiene las clases que implementan el patrón **Page Object Model (POM)**. Cada archivo representa una "página" o componente del sistema bajo prueba.
    * `screenshots/`: Directorio donde se almacenan las **capturas de pantalla** tomadas durante la ejecución de las pruebas (por lo general, capturas de fallos).
    * `test/`: Contiene los **scripts de prueba** que definen los escenarios (*test cases*) utilizando las clases Page Object.
    * `conftest.py`: Archivo especial de Pytest que contiene *fixtures* compartidas y ganchos (*hooks*) de configuración para toda la *suite* de pruebas.
    * `requirements.txt`: Lista de todas las librerías y dependencias de Python necesarias para ejecutar el proyecto.

---

## Cómo Empezar

Sigue estos pasos para configurar y ejecutar las pruebas localmente.

### 1. Prerrequisitos

Asegúrate de tener instalado:

* **Python**.
* **Git** (para clonar el repositorio).

### 2. Instalación

1.  **Clona** el repositorio:
    ```bash
    git clone [https://aws.amazon.com/es/what-is/repo/](https://aws.amazon.com/es/what-is/repo/)
    cd VITAWALLET-TEST
    ```

2.  **Crea y activa un entorno virtual** (opcional, pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    # venv\Scripts\activate   # En Windows
    ```

3.  **Instala las dependencias** de Python:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Ejecución de las Pruebas

Para ejecutar todas las pruebas en el directorio `test/`:

```bash
pytest