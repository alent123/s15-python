test_results = []  # Lista donde se almacenan los resultados de las pruebas

def record_test(test_name, condition):  # Función para registrar el nombre del test y si pasó o no
    emoji = "✅" if condition else "❌"  # Si la condición es verdadera, se pone un check, si no, una X
    test_results.append(f"{emoji} {test_name}")  # Se agrega el resultado formateado a la lista

class Graph:  # Definición de la clase Graph
    def __init__(self):  # Constructor de la clase
        self.adjacency_list = {}  # Inicializa el grafo como un diccionario vacío (lista de adyacencia)

    def add_vertex(self, vertex):  # Método para agregar un vértice
        if vertex not in self.adjacency_list:  # Verifica si el vértice ya existe
            self.adjacency_list[vertex] = []  # Si no existe, lo agrega con una lista vacía de vecinos

    def add_edge(self, vertex1, vertex2):  # Método para agregar una arista entre dos vértices
        self.add_vertex(vertex1)  # Asegura que vertex1 esté en el grafo
        self.add_vertex(vertex2)  # Asegura que vertex2 esté en el grafo
        if vertex2 not in self.adjacency_list[vertex1]:  # Si vertex2 no es vecino de vertex1
            self.adjacency_list[vertex1].append(vertex2)  # Agrega vertex2 como vecino de vertex1
        if vertex1 not in self.adjacency_list[vertex2]:  # Si vertex1 no es vecino de vertex2
            self.adjacency_list[vertex2].append(vertex1)  # Agrega vertex1 como vecino de vertex2

    def find_path(self, start_vertex, end_vertex):  # Método para encontrar un camino entre dos vértices usando BFS
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:  # Verifica si ambos vértices existen
            return []  # Si no existen, no hay camino posible

        if start_vertex == end_vertex:  # Caso especial: el inicio es igual al final
            return [start_vertex]  # Devuelve el vértice como camino

        visited = set()  # Conjunto para guardar los vértices ya visitados
        queue = [[start_vertex]]  # Cola de rutas, comenzando con una lista que contiene solo el inicio

        while queue:  # Mientras haya rutas por explorar
            path = queue.pop(0)  # Toma la primera ruta de la cola
            vertex = path[-1]  # Obtiene el último vértice de esa ruta

            if vertex == end_vertex:  # Si ya llegamos al destino
                return path  # Devolvemos el camino encontrado

            if vertex not in visited:  # Si aún no hemos visitado ese vértice
                visited.add(vertex)  # Lo marcamos como visitado

                for neighbor in self.adjacency_list[vertex]:  # Recorremos los vecinos del vértice actual
                    new_path = list(path)  # Copiamos la ruta actual
                    new_path.append(neighbor)  # Agregamos el vecino a la nueva ruta
                    queue.append(new_path)  # Agregamos la nueva ruta a la cola

        return []  # Si no encontramos un camino, retornamos lista vacía

    def is_connected(self, vertex1, vertex2):  # Método para verificar si dos vértices están conectados
        return len(self.find_path(vertex1, vertex2)) > 0  # Si el camino encontrado no es vacío, están conectados

    def has_vertex(self, vertex):  # Método para verificar si un vértice existe en el grafo
        return vertex in self.adjacency_list  # Retorna True si el vértice está en la lista de adyacencia

def test_1_4():  # Función que ejecuta las pruebas del Challenge 4
    graph = Graph()  # Crea una instancia del grafo

    graph.add_edge("Lima", "Cusco")  # Agrega una arista entre Lima y Cusco
    graph.add_edge("Cusco", "Arequipa")  # Agrega una arista entre Cusco y Arequipa
    graph.add_vertex("Trujillo")  # Agrega un vértice aislado (sin conexiones)

    path = graph.find_path("Lima", "Cusco")  # Busca un camino directo entre Lima y Cusco
    record_test("1.4.1 Direct connection path", path == ["Lima", "Cusco"])  # Verifica si el camino directo es correcto

    path = graph.find_path("Lima", "Arequipa")  # Busca un camino entre Lima y Arequipa (pasando por Cusco)
    is_valid_path = len(path) == 3 and path[0] == "Lima" and path[-1] == "Arequipa"  # Verifica que sea una ruta válida
    record_test("1.4.2 Indirect connection path", is_valid_path)  # Registra el resultado

    path = graph.find_path("Lima", "Trujillo")  # Intenta encontrar un camino entre Lima y Trujillo (no conectado)
    record_test("1.4.3 No path case", path == [])  # Verifica que no se encontró camino (lo esperado)

    path = graph.find_path("Lima", "Lima")  # Busca un camino de Lima a Lima
    record_test("1.4.4 Self path", path == ["Lima"])  # Verifica que se retorna a sí mismo

    connected = graph.is_connected("Lima", "Arequipa")  # Verifica si Lima está conectado con Arequipa
    not_connected = graph.is_connected("Lima", "Trujillo")  # Verifica si Lima está conectado con Trujillo (no debería)
    record_test("1.4.5 Connectivity check", connected and not not_connected)  # Verifica que se detecten bien ambas conexiones

test_1_4()  # Llama a la función que ejecuta todas las pruebas

for r in test_results:  # Itera sobre cada resultado de prueba
    print(r)  # Imprime cada resultado en consola