
#1️⃣ Challenge 1: Basic Graph Foundation 🛠️

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    def get_vertex_count(self):
        return len(self.adjacency_list)
    def has_vertex(self, vertex):
        return vertex in self.adjacency_list
    
def test_1_1():
    graph = Graph()
    record_test("1.1.1 Empty graph initialization", graph.get_vertex_count() == 0)
    graph.adjacency_list = {"Lima": [], "Cusco": []}
    record_test("1.1.2 Vertex counting", graph.get_vertex_count() == 2)
    record_test("1.1.3 Vertex existence check", graph.has_vertex("Lima") == True)
    empty_graph = Graph()
    record_test("1.1.4 Empty graph edge case", empty_graph.has_vertex("Lima") == False)
    record_test("1.1.5 Type validation", isinstance(graph.get_vertices(), list))
test_1_1()

for r in test_results:
    print(r)



#2️⃣ Challenge 2: Adding Vertices and Basic Structure 🏗️

test_results = []
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")
class Graph:
    def __init__(self):
        self.adjacency_list = {}
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    def get_vertices(self):
        return list(self.adjacency_list.keys())
    def get_vertex_count(self):
        return len(self.adjacency_list)
    def has_vertex(self, vertex):
        return vertex in self.adjacency_list

def test_1_2():
    graph = Graph()
    
    graph.add_vertex("Lima")
    record_test("1.2.1 Single vertex addition", graph.has_vertex("Lima"))

    graph.add_vertex("Cusco")
    graph.add_vertex("Arequipa")
    record_test("1.2.2 Multiple vertex addition", graph.get_vertex_count() == 3)

    initial_count = graph.get_vertex_count()
    graph.add_vertex("Lima") 
    record_test("1.2.3 Duplicate prevention", graph.get_vertex_count() == initial_count)
    
    lima_neighbors = graph.adjacency_list.get("Lima", [])
    record_test("1.2.4 Vertex isolation", len(lima_neighbors) == 0)

    graph.add_vertex("Trujillo")
    record_test("1.2.5 Graph size tracking", "Trujillo" in graph.get_vertices())
test_1_2()

for r in test_results:
    print(r)
