# Análisis de Frecuencia de Letras en Archivos de Texto

Este script realiza un análisis de frecuencia de letras (a-z) en un archivo de texto plano, ignorando tildes y distinciones entre mayúsculas y minúsculas. El resultado se muestra en consola y se guarda en un archivo .hist.

# Características:

- Normaliza el texto eliminando tildes (á -> a, ñ -> n, etc.).

- Convierte todo el contenido a minúsculas.

- Cuenta únicamente letras del alfabeto (a-z).

- Ordena las letras por frecuencia de aparición (de mayor a menor).

- Guarda el historial en un archivo .hist para posteriores análisis.

# Aplicaciones potenciales:

- Análisis estadísticos.

- Validación y detección de errores en textos.

- Análisis básico de patrones de texto en entornos de seguridad o criptografía.


## 🚀 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/pedro-millan/contador_caracteres_latinos.git
   cd contador_caracteres_latinos

2. Crea y activa un entorno virtual:
   python3 -m venv venv
   source venv/bin/activate

3. Instala las dependencias:
   pip install -r requirements.txt

## 🧪 Tests

Este proyecto incluye pruebas unitarias con pytest.

Para ejecutarlas desde la raíz del proyecto:
	pytest -q

## 📂 Estructura del proyecto

contador_caracteres/
├── src/
│   └── main_contador.py
├── tests/
│   └── test_contador.py
├── requirements.txt
├── pytest.ini
└── README.md

