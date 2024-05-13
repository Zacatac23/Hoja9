# Gestor de Rutas

Este programa es un gestor de rutas que utiliza el algoritmo de Dijkstra para encontrar las rutas más cortas entre diferentes estaciones. Utiliza la biblioteca NetworkX para representar las rutas como un grafo y calcular las rutas más cortas.

## Instalación

Para ejecutar este programa, asegúrate de tener Python instalado en tu sistema. También necesitarás instalar la biblioteca NetworkX. Puedes instalarlo usando pip:


## Uso

1. **Ejecución del programa:**

    Para ejecutar el programa, simplemente ejecuta el archivo `gestor_rutas.py` en tu terminal o entorno de Python preferido.

    ```
    python gestor_rutas.py
    ```

2. **Interacción con el programa:**

    El programa te pedirá que ingreses la estación de salida. Después de ingresar la estación de salida, te mostrará los destinos posibles desde esa estación y las mejores rutas desde la estación de salida utilizando el algoritmo de Dijkstra.

3. **Formato del archivo de rutas:**

    El programa espera que las rutas estén en un archivo de texto con el siguiente formato:

    ```
    Origen, Destino, Costo
    ```

    Donde:
    - `Origen` es la estación de salida.
    - `Destino` es la estación de llegada.
    - `Costo` es el costo asociado con esa ruta.

## Ejemplo de archivo de rutas

Aquí tienes un ejemplo de cómo podría ser un archivo de rutas (`rutas.txt`):

