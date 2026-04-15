# 🎰 CasinoCaliente

## 📌 Descripción del proyecto

CasinoCaliente es una aplicación desarrollada en Python que simula el funcionamiento de un casino digital.
El usuario puede acceder a diferentes juegos de azar desde un menú principal y apostar dinero virtual en cada uno de ellos.

El objetivo del proyecto es aplicar conceptos fundamentales de programación en Python como:

* Estructuras de control
* Funciones
* Modularización
* Generación de números aleatorios
* Organización de proyectos

---

## 🎮 Juegos disponibles (MVP)

* 🃏 Blackjack
* 🎡 Ruleta
* 🎰 Tragamonedas
* 🎲 Craps

Cada juego está implementado como un módulo independiente, lo que permite escalar fácilmente el proyecto.

---

## 🧱 Estructura del proyecto

```
CasinoCaliente/
│
├── main.py                # Punto de entrada del programa (menú principal)
│
├── games/                # Contiene todos los juegos del casino
│   ├── __init__.py
│   ├── blackjack.py
│   ├── ruleta.py
│   ├── tragamonedas.py
│   └── craps.py
│
├── core/                 # Lógica central del sistema
│   ├── player.py         # Gestión del jugador
│   └── wallet.py         # Sistema de dinero/apuestas
│
├── utils/                # Utilidades y funciones auxiliares
│   ├── __init__.py
│   └── random_utils.py
│
├── requirements.txt      # Dependencias del proyecto
├── pyproject.toml        # Configuración del proyecto
└── README.md             # Documentación
```

---

## ⚙️ Cómo funciona el sistema

1. El usuario ejecuta el programa (`main.py`)
2. Se muestra un menú con los juegos disponibles
3. El usuario selecciona un juego
4. Se ejecuta la lógica del juego correspondiente
5. El sistema actualiza el dinero del jugador según el resultado
6. El usuario puede seguir jugando o salir

---

## ▶️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```
git clone https://github.com/TU_USUARIO/CasinoCaliente.git
cd CasinoCaliente
```

---

### 2. (Opcional) Crear entorno virtual

```
python -m venv venv
```

Activar en Windows:

```
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```
pip install -r requirements.txt
```

---

### 4. Ejecutar el proyecto

```
python main.py
```

---

## 👥 Trabajo en equipo

* Cada desarrollador puede trabajar en un juego diferente
* Se recomienda mantener una estructura modular
* Usar Git para control de versiones:

  ```
  git add .
  git commit -m "mensaje"
  git push
  ```

---

## 🚀 Posibles mejoras futuras

* Interfaz gráfica (Tkinter / PyGame)
* Guardado de partidas
* Sistema de usuarios
* Base de datos
* Sonidos y animaciones
* Estadísticas del jugador

---

## 🧠 Objetivo académico

Este proyecto está diseñado para:

* Aprender a estructurar proyectos en Python
* Aplicar buenas prácticas de programación
* Simular un sistema real con múltiples funcionalidades

---

## 📄 Licencia

Proyecto académico sin fines comerciales.
