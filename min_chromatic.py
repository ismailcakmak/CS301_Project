
class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_edge(self, source, destination):
        edge = Edge(source, destination)
        self.edges.append(edge)



global_result_list = []


def is_choice_valid(graph, temp_list):

    #if temp_list empty, means 
    if len(temp_list) == 0:
        return True
    
    print("Temp List : ", temp_list)
    print("Vertices:", len(graph.vertices))

    vertex = graph.vertices[len(temp_list)-1]
    choice = temp_list[-1]

    for edge in graph.edges:
        
        if edge.source == vertex:

            #if destination vertex is colored already
            destination_idx = graph.vertices.index(edge.destination)
            if  destination_idx < len(temp_list):

                #if this color is equal to choice, return False:
                if temp_list[destination_idx] == choice:
                    return False
                
        elif edge.destination == vertex:

            #if source vertex is colored already
            source_idx = graph.vertices.index(edge.source)
            if  source_idx < len(temp_list):

                #if this color is equal to choice, return False:
                if temp_list[source_idx] == choice:
                    return False
    
    return True



def backtrack_helper(graph, color_list, temp_list):
    
    global global_result_list

    #iterate over choices
    for choice in color_list:

        if len(global_result_list) > 0:
            return
        
        copy_temp_list = temp_list.copy()
        copy_temp_list.append(choice)

        if is_choice_valid(graph,copy_temp_list):

            #if condition is satisfied
            if(len(copy_temp_list) == len(graph.vertices)):
                print("girdi")
                global_result_list = copy_temp_list
                return
            
            backtrack_helper(graph, color_list, copy_temp_list)
            
            



def backtrack(k,graph):

    #k is the number of colors trying to color graph
    color_list = [i for i in range(k)]
    backtrack_helper(graph, color_list, [])



def brute_force_min_chromatic(graph):

    global global_result_list  # Add this line

    for i in range(len(graph.vertices)+1):
        global_result_list = []
        backtrack(i,graph)

        #if global_result_list is not empty, then backtrack algorithm found a way to color graph with k color
        if len(global_result_list) > 0:
            return i
        
    
def main():
    
    # Create a sample graph for testing
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_vertex('D')
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('A', 'D')
    g.add_edge('C', 'A')
    g.add_edge('B', 'D')


    # Test the brute-force algorithm
    min_chromatic = brute_force_min_chromatic(g)
    print("Min chromatic :", min_chromatic)
        


if __name__ == "__main__":
    main()
