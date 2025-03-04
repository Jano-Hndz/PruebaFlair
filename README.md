# Simulación de Infección en un Edificio

## Descripción
Este proyecto simula la propagación de una infección (zombies) dentro de un edificio con múltiples pisos y habitaciones. La infección comienza en una habitación aleatoria y se propaga a lo largo del tiempo bajo ciertas reglas establecidas.

## Reglas de Propagación
1. **Inicio de la infección**: Un solo zombie aparece aleatoriamente en una habitación del edificio al inicio de la simulación.
2. **Propagación horizontal**: Si una habitación está infectada, puede contagiar a sus habitaciones adyacentes en el mismo piso.
3. **Propagación vertical**:
   - Cuando todas las habitaciones de un piso están infectadas, el siguiente turno se propaga la infección a una habitación del piso superior e inferior.
   - Las habitaciones infectadas en el nuevo piso no contagian a sus habitaciones adyacentes inmediatamente al infectarse, solo se propagan en los turnos siguientes.
4. **Estado de los sensores**: Cada habitación tiene un sensor que cambia su estado de "normal" a "alert" cuando hay un zombie presente.

## Estructura del Código
- **`Sensor`**: Representa el sensor de cada habitación, cambiando de estado cuando hay zombies.
- **`Room`**: Representa una habitación, que puede contener zombies y está equipada con un sensor.
- **`Floor`**: Representa un piso con múltiples habitaciones y maneja la propagación dentro del mismo piso.
- **`Building`**: Representa el edificio compuesto por varios pisos.
- **`Simulation`**: Controla la lógica de propagación de la infección y el flujo de la simulación.
- **`main()`**: Interfaz de usuario para interactuar con la simulación desde la terminal.

## Funcionalidades
- **Configurar edificio**: Permite definir el número de pisos y habitaciones por piso.
- **Mostrar estado del edificio**: Muestra el estado actual de cada habitación.
- **Avanzar la simulación**: Ejecuta un turno de propagación de la infección.
- **Salir**: Finaliza la simulación.

## Cómo Ejecutar
1. Guarda el código en un archivo `zombie_simulation.py`.
2. Ejecuta el siguiente comando en la terminal:
   ```sh
   python zombie_simulation.py
   ```
3. Sigue las opciones del menú para interactuar con la simulación.

## Consideraciones
- Al inicio, solo se genera un zombie en una habitación aleatoria del edificio, y la infección comienza a propagarse en el siguiente turno.
- La infección de los zombies ocurre por expansión, siguiendo las reglas establecidas en cada turno.
- La infección solo se propaga entre habitaciones adyacentes dentro del mismo piso.
- La propagación entre pisos ocurre solo cuando un piso está completamente infectado.
- Se garantiza que la infección en un nuevo piso no afecta de inmediato a sus habitaciones adyacentes.
- Se utiliza un sistema de turnos para controlar la propagación de manera gradual.


