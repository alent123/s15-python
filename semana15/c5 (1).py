test_results = []  # Lista donde se almacenan los resultados de cada prueba

def record_test(test_name, condition):  # Función que registra si cada test pasó o no
    emoji = "✅" if condition else "❌"  # Asigna ✅ si es verdadero o ❌ si es falso
    test_results.append(f"{emoji} {test_name}")  # Agrega el resultado formateado a la lista de pruebas

class Graph:  # Definición de la clase Graph
    def __init__(self):  # Constructor de la clase
        self.adjacency_list = {}  # Inicializa la lista de adyacencia como un diccionario vacío

    def add_vertex(self, vertex):  # Método para agregar un vértice al grafo
        if vertex not in self.adjacency_list:  # Verifica si ya existe
            self.adjacency_list[vertex] = []  # Si no, lo agrega con una lista vacía de vecinos

    def add_edge(self, vertex1, vertex2):  # Método para agregar una arista entre dos vértices
        self.add_vertex(vertex1)  # Asegura que vertex1 existe
        self.add_vertex(vertex2)  # Asegura que vertex2 existe
        if vertex2 not in self.adjacency_list[vertex1]:  # Si vertex2 no está conectado aún
            self.adjacency_list[vertex1].append(vertex2)  # Conecta vertex1 con vertex2
        if vertex1 not in self.adjacency_list[vertex2]:  # Si vertex1 no está conectado aún
            self.adjacency_list[vertex2].append(vertex1)  # Conecta vertex2 con vertex1

    def get_degree(self, vertex):  # Retorna el número de conexiones de un vértice
        if vertex in self.adjacency_list:  # Verifica si el vértice existe
            return len(self.adjacency_list[vertex])  # Retorna la cantidad de vecinos
        return 0  # Si no existe, retorna 0

    def find_all_paths(self, start_vertex, end_vertex, max_length=None):  # Encuentra todos los caminos entre dos vértices
        def dfs(current, end, path):  # Función auxiliar recursiva DFS
            if current == end:  # Si llegamos al destino
                paths.append(path)  # Guardamos el camino actual
                return
            if max_length is not None and len(path) > max_length:  # Si se supera la longitud máxima
                return  # No continuamos
            for neighbor in self.adjacency_list.get(current, []):  # Recorre vecinos del nodo actual
                if neighbor not in path:  # Evita ciclos
                    dfs(neighbor, end, path + [neighbor])  # Llama recursivamente con el nuevo camino

        paths = []  # Lista para guardar todos los caminos encontrados
        if start_vertex in self.adjacency_list and end_vertex in self.adjacency_list:  # Verifica que ambos vértices existan
            dfs(start_vertex, end_vertex, [start_vertex])  # Inicia búsqueda desde el vértice inicial
        return paths  # Devuelve todos los caminos encontrados

    def get_connected_components(self):  # Encuentra componentes conexos del grafo
        visited = set()  # Conjunto para registrar vértices ya visitados
        components = []  # Lista de componentes encontrados

        def dfs(vertex, component):  # Función auxiliar DFS para explorar un componente
            visited.add(vertex)  # Marca el vértice como visitado
            component.append(vertex)  # Agrega el vértice al componente actual
            for neighbor in self.adjacency_list.get(vertex, []):  # Recorre vecinos
                if neighbor not in visited:  # Si aún no ha sido visitado
                    dfs(neighbor, component)  # Continúa DFS recursivamente

        for vertex in self.adjacency_list:  # Recorre todos los vértices del grafo
            if vertex not in visited:  # Si no ha sido visitado
                component = []  # Nuevo componente
                dfs(vertex, component)  # Explora desde ese vértice
                components.append(component)  # Agrega el componente a la lista
        return components  # Retorna todos los componentes conexos

def test_1_5():  # Función que ejecuta los tests del Challenge 5
    graph = Graph()  # Crea una nueva instancia del grafo

    graph.add_edge("Lima", "Cusco")  # Agrega arista entre Lima y Cusco
    graph.add_edge("Lima", "Arequipa")  # Agrega arista entre Lima y Arequipa
    graph.add_edge("Cusco", "Arequipa")  # Agrega arista entre Cusco y Arequipa
    graph.add_edge("Trujillo", "Piura")  # Agrega arista entre Trujillo y Piura (componente separado)

    lima_degree = graph.get_degree("Lima")  # Obtiene el grado (conexiones) de Lima
    record_test("1.5.1 Degree calculation", lima_degree == 2)  # Verifica si Lima tiene 2 conexiones

    paths = graph.find_all_paths("Lima", "Arequipa", max_length=3)  # Busca todos los caminos entre Lima y Arequipa con máx 3 pasos
    has_multiple_paths = len(paths) >= 2  # Verifica si hay más de un camino
    record_test("1.5.2 Multiple paths finding", has_multiple_paths)  # Registra si encontró múltiples caminos

    components = graph.get_connected_components()  # Obtiene los componentes conexos del grafo
    has_two_components = len(components) == 2  # Verifica si hay exactamente 2 componentes
    record_test("1.5.3 Connected components", has_two_components)  # Registra el resultado

    empty_graph = Graph()  # Crea un nuevo grafo vacío
    empty_components = empty_graph.get_connected_components()  # Busca componentes en el grafo vacío
    record_test("1.5.4 Empty graph analysis", empty_components == [])  # Verifica que no haya componentes

    degree = graph.get_degree("NonExistent")  # Intenta obtener el grado de un vértice que no existe
    record_test("1.5.5 Non-existent vertex handling", degree == 0 or degree is None)  # Verifica que se maneje bien ese caso

test_1_5()  # Llama a la función que ejecuta las pruebas

for r in test_results:  # Recorre los resultados de los tests
    print(r)  # Imprime cada resultado