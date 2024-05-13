import networkx as nx
import matplotlib.pyplot as plt

def cargar_rutas(archivo):
    """
    Carga las rutas desde un archivo y construye un grafo NetworkX.
    
    Args:
        archivo (str): Ruta del archivo que contiene las rutas.
    
    Returns:
        G (networkx.Graph): Grafo que representa las rutas cargadas.
    """
    G = nx.Graph()
    with open(archivo, 'r') as f:
        for linea in f:
            origen, destino, costo = linea.strip().split(',')
            G.add_edge(origen.strip(), destino.strip(), weight=int(costo))
    return G

def encontrar_destinos(G, origen):
    """
    Encuentra los destinos posibles desde una estación de origen.
    
    Args:
        G (networkx.Graph): Grafo que representa las rutas.
        origen (str): Estación de origen.
    
    Returns:
        destinos (list): Lista de destinos posibles desde la estación de origen.
    """
    destinos = list(G.neighbors(origen))
    return destinos

def dijkstra(G, origen):
    """
    Calcula las rutas más cortas desde una estación de origen utilizando el algoritmo de Dijkstra.
    
    Args:
        G (networkx.Graph): Grafo que representa las rutas.
        origen (str): Estación de origen.
    
    Returns:
        rutas (dict): Diccionario que asigna cada destino a la ruta más corta desde el origen.
        costos (dict): Diccionario que asigna cada destino al costo de la ruta más corta desde el origen.
    """
    rutas = nx.single_source_dijkstra_path(G, origen)
    costos = nx.single_source_dijkstra_path_length(G, origen)
    return rutas, costos

def dibujar_mapa(G, origen):
    """
    Dibuja un mapa de destinos desde una estación de origen.
    
    Args:
        G (networkx.Graph): Grafo que representa las rutas.
        origen (str): Estación de origen.
    """
    pos = nx.spring_layout(G)  # Calcula las posiciones de los nodos utilizando un layout de resorte
    nx.draw(G, pos, with_labels=True)  # Dibuja el grafo con etiquetas de nodos
    nx.draw_networkx_nodes(G, pos, nodelist=[origen], node_color='r')  # Resalta el nodo de origen en rojo
    plt.title(f"Mapa de destinos desde {origen}")  # Agrega un título al mapa
    plt.show()  # Muestra el mapa

def main():
    archivo_rutas = 'rutas.txt'
    G = cargar_rutas(archivo_rutas)
    origen = input("Ingrese la estación de salida: ")
    print(f"\nDestinos posibles desde {origen}:")
    destinos = encontrar_destinos(G, origen)
    for destino in destinos:
        print(destino)
    print(f"\nMejores rutas desde {origen}:")
    rutas, costos = dijkstra(G, origen)
    for destino, ruta in rutas.items():
        costo = costos[destino]
        print(f"Destino: {destino}, Ruta: {' -> '.join(ruta)}, Costo: {costo}")
    dibujar_mapa(G, origen)

# Punto de entrada del programa
main()