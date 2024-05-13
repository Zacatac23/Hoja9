import networkx as nx
import matplotlib.pyplot as plt

def cargar_rutas(archivo):
    G = nx.Graph()
    with open(archivo, 'r') as f:
        for linea in f:
            origen, destino, costo = linea.strip().split(',')
            G.add_edge(origen.strip(), destino.strip(), weight=int(costo))
    return G

def encontrar_destinos(G, origen):
    destinos = list(G.neighbors(origen))
    return destinos

def dijkstra(G, origen):
    rutas = nx.single_source_dijkstra_path(G, origen)
    costos = nx.single_source_dijkstra_path_length(G, origen)
    return rutas, costos

def dibujar_mapa(G, origen):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    nx.draw_networkx_nodes(G, pos, nodelist=[origen], node_color='r')
    plt.title(f"Mapa de destinos desde {origen}")
    plt.show()

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

main()