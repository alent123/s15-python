test_results = []  # Lista para guardar los resultados de las pruebas

def record_test(test_name, condition):  # Función para registrar los resultados de cada test
    emoji = "✅" if condition else "❌"  # Muestra un check si es verdadero, una X si es falso
    test_results.append(f"{emoji} {test_name}")  # Agrega el resultado a la lista de tests

class Graph:  # Definición de la clase Graph
    def __init__(self):  # Método constructor que se ejecuta al crear un nuevo objeto
        self.adjacency_list = {}  # Diccionario que representa la lista de adyacencia del grafo

    def add_vertex(self, vertex):  # Método para agregar un vértice al grafo
        if vertex not in self.adjacency_list:  # Si el vértice no existe en la lista de adyacencia
            self.adjacency_list[vertex] = []  # Se agrega el vértice con una lista vacía de vecinos

    def add_edge(self, vertex1, vertex2):  # Método para agregar una arista entre dos vértices
        self.add_vertex(vertex1)  # Asegura que vertex1 esté en el grafo
        self.add_vertex(vertex2)  # Asegura que vertex2 esté en el grafo
        if vertex2 not in self.adjacency_list[vertex1]:  # Si vertex2 no está ya conectado a vertex1
            self.adjacency_list[vertex1].append(vertex2)  # Se agrega la conexión desde vertex1 a vertex2
        if vertex1 not in self.adjacency_list[vertex2]:  # Si vertex1 no está ya conectado a vertex2
            self.adjacency_list[vertex2].append(vertex1)  # Se agrega la conexión desde vertex2 a vertex1

    def has_edge(self, vertex1, vertex2):  # Verifica si hay una arista entre vertex1 y vertex2
        return vertex2 in self.adjacency_list.get(vertex1, [])  # Retorna True si vertex2 está en la lista de vertex1

    def get_neighbors(self, vertex):  # Retorna la lista de vecinos de un vértice
        return self.adjacency_list.get(vertex, [])  # Devuelve la lista de adyacencia del vértice, o [] si no existe

    def has_vertex(self, vertex):  # ✅ Método agregado para verificar si un vértice existe en el grafo
        return vertex in self.adjacency_list  # Retorna True si el vértice está en el grafo

def test_1_3():  # Función que contiene las pruebas para el Challenge 3
    graph = Graph()  # Crea una nueva instancia del grafo

    graph.add_vertex("Lima")  # Agrega el vértice "Lima"
    graph.add_vertex("Cusco")  # Agrega el vértice "Cusco"
    graph.add_edge("Lima", "Cusco")  # Crea una arista entre "Lima" y "Cusco"
    record_test("1.3.1 Basic edge creation", graph.has_edge("Lima", "Cusco"))  # Verifica si la conexión fue creada

    record_test("1.3.2 Bidirectional connection", graph.has_edge("Cusco", "Lima"))  # Verifica si la conexión es bidireccional

    graph.add_edge("Arequipa", "Trujillo")  # Agrega arista entre dos vértices que aún no existen (se crean automáticamente)
    has_both = graph.has_vertex("Arequipa") and graph.has_vertex("Trujillo")  # Verifica si ambos fueron creados
    record_test("1.3.3 Auto vertex creation", has_both)  # Registra si ambos vértices fueron agregados correctamente

    initial_neighbors = len(graph.get_neighbors("Lima"))  # Obtiene la cantidad de vecinos de "Lima" antes de repetir conexión
    graph.add_edge("Lima", "Cusco")  # Intenta agregar la misma arista otra vez
    final_neighbors = len(graph.get_neighbors("Lima"))  # Obtiene la cantidad de vecinos después
    record_test("1.3.4 Duplicate edge prevention", initial_neighbors == final_neighbors)  # Verifica que no se duplicó la conexión

    lima_neighbors = graph.get_neighbors("Lima")  # Obtiene los vecinos de "Lima"
    record_test("1.3.5 Connection verification", "Cusco" in lima_neighbors)  # Verifica que "Cusco" esté conectado a "Lima"

test_1_3()  # Ejecuta todas las pruebas del Challenge 3

for r in test_results:  # Itera sobre cada resultado de test
    print(r)  # Imprime el resultado del test (con su respectivo emoji)