"""
JUEGO: ADIVINA EL NÚMERO
"""

class JuegoAdivinaNumero:
    """Capa Lógica: Contiene el algoritmo de búsqueda binaria"""
    
    def __init__(self):
        self.numero_minimo = 0
        self.numero_maximo = 0
        self.intentos = 0
        self.limite_inferior = 0
        self.limite_superior = 0
        self.historial_intentos = []
    
    def configurar_rango(self, minimo, maximo):
        """Configura el rango de números para el juego"""
        if minimo >= maximo:
            raise ValueError("El número mínimo debe ser menor que el máximo")
        
        self.numero_minimo = minimo
        self.numero_maximo = maximo
        self.limite_inferior = minimo
        self.limite_superior = maximo
        self.intentos = 0
        self.historial_intentos = []
    
    def calcular_suposicion(self):
        """Implementa búsqueda binaria para adivinar el número"""
        if self.limite_inferior > self.limite_superior:
            raise ValueError("Rango inválido: posible trampa detectada")
        
        suposicion = (self.limite_inferior + self.limite_superior) // 2
        self.intentos += 1
        self.historial_intentos.append(suposicion)
        return suposicion
    
    def procesar_respuesta(self, respuesta, suposicion):
        """Ajusta los límites según la respuesta del usuario"""
        if respuesta == "alto":
            self.limite_inferior = suposicion + 1
        elif respuesta == "bajo":
            self.limite_superior = suposicion - 1
        elif respuesta == "correcto":
            return True
        else:
            raise ValueError("Respuesta inválida")
        
        return False
    
    def obtener_estadisticas(self):
        """Retorna las estadísticas del juego"""
        return {
            "intentos": self.intentos,
            "rango": f"{self.numero_minimo} - {self.numero_maximo}",
            "historial": self.historial_intentos
        }


class InterfazUsuario:
    """Capa de Presentación: Maneja la interacción con el usuario"""
    
    def __init__(self):
        self.juego = JuegoAdivinaNumero()
    
    def mostrar_bienvenida(self):
        """Muestra el mensaje de bienvenida"""
        print("=" * 50)
        print("  BIENVENIDO AL JUEGO: ADIVINA EL NÚMERO")
        print("  La computadora adivinará tu número")
        print("=" * 50)
        print()
    
    def solicitar_rango(self):
        """Solicita al usuario el rango de números"""
        while True:
            try:
                print("Configura el rango de números:")
                minimo = int(input("Ingresa el número mínimo: "))
                maximo = int(input("Ingresa el número máximo: "))
                
                self.juego.configurar_rango(minimo, maximo)
                print(f"\n✓ Rango configurado: {minimo} a {maximo}")
                return True
            
            except ValueError as e:
                print(f"\n✗ Error: {e}")
                print("Por favor, intenta nuevamente.\n")
    
    def solicitar_numero_secreto(self):
        """Pide al usuario que piense un número"""
        print(f"\nPiensa en un número entre {self.juego.numero_minimo} y {self.juego.numero_maximo}")
        input("Presiona ENTER cuando estés listo...")
        print()
    
    def realizar_intento(self):
        """Realiza un intento de adivinanza"""
        try:
            suposicion = self.juego.calcular_suposicion()
            print(f"\nIntento #{self.juego.intentos}")
            print(f"¿Tu número es {suposicion}?")
            print("\nOpciones:")
            print("  1) Es correcto")
            print("  2) Mi número es más alto")
            print("  3) Mi número es más bajo")
            
            while True:
                opcion = input("\nTu respuesta (1/2/3): ").strip()
                
                if opcion == "1":
                    return self.juego.procesar_respuesta("correcto", suposicion)
                elif opcion == "2":
                    self.juego.procesar_respuesta("alto", suposicion)
                    print(f"→ Ajustando búsqueda... el número es mayor que {suposicion}")
                    return False
                elif opcion == "3":
                    self.juego.procesar_respuesta("bajo", suposicion)
                    print(f"→ Ajustando búsqueda... el número es menor que {suposicion}")
                    return False
                else:
                    print("✗ Opción inválida. Ingresa 1, 2 o 3.")
        
        except ValueError as e:
            print(f"\n✗ Error detectado: {e}")
            print("¡Parece que algo no está bien! ¿Cambiaste de número?")
            return None
    
    def mostrar_estadisticas(self):
        """Muestra las estadísticas finales del juego"""
        stats = self.juego.obtener_estadisticas()
        
        print("\n" + "=" * 50)
        print("  ESTADÍSTICAS DEL JUEGO")
        print("=" * 50)
        print(f"✓ ¡Número encontrado en {stats['intentos']} intentos!")
        print(f"✓ Rango: {stats['rango']}")
        print(f"✓ Intentos realizados: {stats['historial']}")
        print("=" * 50)
    
    def preguntar_jugar_nuevamente(self):
        """Pregunta si el usuario desea jugar de nuevo"""
        while True:
            respuesta = input("\n¿Deseas jugar nuevamente? (S/N): ").strip().upper()
            if respuesta in ["S", "N"]:
                return respuesta == "S"
            print("✗ Por favor, ingresa S o N")
    
    def ejecutar_juego(self):
        """Ciclo principal del juego"""
        self.mostrar_bienvenida()
        
        jugar = True
        while jugar:
            # Configuración
            self.solicitar_rango()
            self.solicitar_numero_secreto()
            
            # Ciclo de adivinanza
            encontrado = False
            while not encontrado:
                resultado = self.realizar_intento()
                
                if resultado is None:  # Error detectado
                    break
                elif resultado:  # Número encontrado
                    encontrado = True
                    self.mostrar_estadisticas()
            
            # Preguntar si desea continuar
            jugar = self.preguntar_jugar_nuevamente()
        
        print("\n¡Gracias por jugar!\n")


def main():
    """Función principal"""
    interfaz = InterfazUsuario()
    interfaz.ejecutar_juego()


if __name__ == "__main__":

    main()
