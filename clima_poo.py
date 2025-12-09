# =========================================================
# PROGRAMACIÓN ORIENTADA a OBJETOS (POO)
# Objetivo: Calcular el promedio semanal de temperaturas
# =========================================================

class ClimaSemanal:
    """
    Representa la información del clima para una semana,
    incluyendo las temperaturas diarias y el cálculo del promedio.
    Aplica encapsulamiento al usar un atributo 'privado' (_temperaturas).
    """
    
    def __init__(self):
        """Constructor: Inicializa la lista de temperaturas."""
        # Aplicación de encapsulamiento: Usamos un guion bajo (_) 
        # para indicar que _temperaturas es un atributo interno de la clase.
        self._temperaturas = [] 

    def ingresar_temperaturas(self):
        """
        Método para la entrada de datos. 
        Solicita al usuario las 7 temperaturas diarias y las almacena.
        """
        self._temperaturas = [] # Asegura que la lista esté vacía antes de ingresar
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        
        print("\n--- Ingreso de Temperaturas Diarias (POO) ---")
        for i in range(7):
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dias[i]} (en °C): "))
                    self._temperaturas.append(temp)
                    break 
                except ValueError:
                    print("⚠️ Entrada no válida. Por favor, ingrese un número.")

    def calcular_promedio_semanal(self):
        """
        Método para calcular el promedio de las temperaturas almacenadas.
        Retorna el promedio (float).
        """
        temps = self._temperaturas
        
        # Verificamos que se hayan ingresado datos
        if not temps:
            return 0.0
        
        suma_total = sum(temps)
        promedio = suma_total / len(temps)
        
        return promedio

    def mostrar_resultado(self):
        """
        Método que muestra las temperaturas registradas y el promedio.
        """
        promedio = self.calcular_promedio_semanal()
        
        print(f"\n✅ Temperaturas registradas (POO): {self._temperaturas}")
        print(f"✅ El promedio semanal del clima (POO) es: **{promedio:.2f}°C**")


# Bloque principal para ejecutar la lógica de POO
if __name__ == "__main__":
    print("--- INICIO: Programación Orientada a Objetos ---")
    
    # 1. Creamos un Objeto/Instancia de la clase ClimaSemanal
    clima = ClimaSemanal()
    
    # 2. Utilizamos los métodos del objeto
    clima.ingresar_temperaturas()
    clima.mostrar_resultado()
    
    print("--- FIN: Programación Orientada a Objetos ---\n")