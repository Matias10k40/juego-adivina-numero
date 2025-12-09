# Juego: Adivina el Número

## Descripción
Juego interactivo donde la computadora adivina el número que estás pensando usando búsqueda binaria.

**Universidad:** Universidad Internacional del Ecuador  
**Materia:** Lógica de Programación  
**Autores:** Jorge Aguilar, Matías Quinteros

## Cómo funciona
1. Configuras un rango de números (ejemplo: 1 a 100)
2. Piensas un número secreto
3. La computadora hace preguntas
4. Tú respondes si es correcto, más alto o más bajo
5. ¡La computadora adivina tu número!

## Cómo ejecutar el juego

### Requisitos
- Python 3.6 o superior

### Pasos
1. Descarga el archivo `juego_adivina_numero.py`
2. Abre un cmd
3. Ve a la carpeta donde descargaste el archivo:
```
   cd Downloads
```
4. Ejecuta el juego:
```
   python juego_adivina_numero.py
```

## Ejemplo de uso
```
Configura el rango de números:
Ingresa el número mínimo: 1
Ingresa el número máximo: 100

Piensa en un número entre 1 y 100
Presiona ENTER cuando estés listo...

Intento #1
¿Tu número es 50?
Tu respuesta (1/2/3): 2

Intento #2
¿Tu número es 75?
...
```

## Arquitectura
El proyecto usa arquitectura en capas:
- **Capa de Presentación:** InterfazUsuario
- **Capa Lógica:** JuegoAdivinaNumero (Búsqueda Binaria)
- **Capa de Datos:** Historial y estadísticas

## Eficiencia
- Rango 1-100: máximo 7 intentos
- Rango 1-1000: máximo 10 intentos
- Complejidad: O(log n)
