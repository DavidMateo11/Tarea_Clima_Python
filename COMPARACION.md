# Comparación entre Programación Tradicional (Funcional) y POO

## 1. Programación Tradicional (`clima_tradicional.py`):
* **Estructura:** El código está organizado en **funciones independientes** (`obtener_temperaturas_diarias`, `calcular_promedio_semanal`).
* **Concepto clave:** La lógica y los datos están separados. Las funciones reciben los datos como argumentos externos.
* **Ventaja:** Sencillez y claridad para tareas pequeñas y cálculos directos.

## 2. Programación Orientada a Objetos (POO) (`clima_poo.py`):
* **Estructura:** El código está organizado alrededor de una **clase** (`ClimaSemanal`) que crea **objetos**.
* **Concepto clave:** Se agrupan los **datos** (`_temperaturas`) y la **lógica** que opera sobre esos datos (`ingresar_temperaturas`, `calcular_promedio_semanal`) en una sola entidad (el objeto).
* **Conceptos de POO aplicados:** **Encapsulamiento**, al manejar la lista de temperaturas (`self._temperaturas`) de forma interna, solo accesible mediante los métodos de la clase.
* **Ventaja:** Mayor orden, modularidad y facilidad de mantenimiento y reutilización para proyectos grandes.