# =========================================================
# PROGRAMACIÓN TRADICIONAL
# Objetivo: Calcular el promedio semanal de temperaturas
# =========================================================

# 1. Función para la entrada de datos (temperaturas)
def obtener_temperaturas_diarias():
    """
    Solicita al usuario las 7 temperaturas diarias de la semana.
    Retorna una lista con las temperaturas (float).
    """
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    print("\n--- Ingreso de Temperaturas Diarias ---")
    for i in range(7):
        while True:
            try:
                # Se pide la temperatura para el día actual y se valida que sea un número
                temp = float(input(f"Ingrese la temperatura del {dias[i]} (en °C): "))
                temperaturas.append(temp)
                break # Sale del bucle while si la entrada es válida
            except ValueError:
                print("⚠️ Entrada no válida. Por favor, ingrese un número.")

    return temperaturas

# 2. Función para el cálculo del promedio semanal
def calcular_promedio_semanal(temps):
    """
    Calcula el promedio de una lista de temperaturas.
    Retorna el promedio (float).
    """
    # Verificamos que la lista no esté vacía para evitar división por cero
    if not temps:
        return 0.0
    
    # La suma de todos los elementos dividida por el número de elementos
    suma_total = sum(temps)
    promedio = suma_total / len(temps)
    
    return promedio

# Bloque principal para ejecutar la lógica tradicional
if __name__ == "__main__":
    print("--- INICIO: Programación Tradicional ---")
    
    # Obtener las temperaturas
    temperaturas_semana = obtener_temperaturas_diarias()
    
    # Calcular el promedio
    promedio_clima = calcular_promedio_semanal(temperaturas_semana)
    
    # Mostrar el resultado
    print(f"\n✅ Temperaturas registradas: {temperaturas_semana}")
    print(f"✅ El promedio semanal del clima es: **{promedio_clima:.2f}°C**")
    print("--- FIN: Programación Tradicional ---\n")