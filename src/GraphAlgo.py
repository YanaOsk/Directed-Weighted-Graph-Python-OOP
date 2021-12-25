import math
import queue


from typing import List

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.NodeData import Node
from src.DiGraph import DiGraph
import json
from itertools import permutations


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = DiGraph):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        zur's implementation
        :return:
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:

        try:
            with open(file_name, "r") as f:
                graph = DiGraph()
                dict = json.load(f)
                for k in dict['Nodes']:
                    if len(k) == 1:
                        node = Node(k['id'])
                    else:
                        n = (k['pos'].split(","))
                        node = Node(k['id'], (float(n[0]), float(n[1])), float(n[2]))
                    graph.add_node(node.id, node.pos)
                for e in dict['Edges']:
                    src = e['src']
                    dest = e['dest']
                    weight = e['w']
                    graph.add_edge(src, dest, weight)
                self.graph = graph
        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        """
       zur's implementation
       """
        def save_to_json(self, file_name: str) -> bool:
            try:
                with open(file_name, 'w') as out_file:
                    json.dump(self.graph.as_dict, out_file, indent = 4)
            except IOError as e:
                print(e)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        temp = queue.LifoQueue()
        weight = math.inf

        if self.graph.get_all_v().get(id1) is not None and self.graph.get_all_v().get(id2) is not None:
            if id1 == id2:
                path.append(self.graph.get_all_v().get(id1))
                return (self.graph.get_all_v().get(id2).weight, path)

            self.dijkstra(self.graph.get_all_v().get(id1))
            graph1 = self.graph
            if self.graph.get_all_v().get(id2).weight == math.inf:
                return (self.graph.get_all_v().get(id2).weight , path)
            destNode = self.graph.get_all_v().get(id2)
            try:
                while self.graph.get_all_v().get(id1) != destNode:
                    temp.put(destNode)
                    destNode = self.graph.get_all_v().get(int(destNode.info))
                temp.put(self.graph.get_all_v().get(id1))
                weight = self.graph.get_all_v().get(id2).weight
            except ValueError as e:
                print(e)
                return (None , None)
            except Exception as e:
                print(e)
                return (None , None)
            while not temp.empty():
                path.append(temp.get())

        return (weight, path)

    def dijkstra(self, srcNode: Node = Node):
        neighborQueue = queue.PriorityQueue()
        for i in self.graph.get_all_v().values():
            i.weight = math.inf
            i.tag = -1
            i.info = ""

        if self.graph.get_all_v().get(srcNode.id) is not None:
            self.graph.get_all_v().get(srcNode.id).weight = 0
        self.graph.get_all_v().get(srcNode.id).info = "" + str(srcNode.id)
        self.graph.get_all_v().get(srcNode.id).tag = 1
        neighborQueue.put(self.graph.get_all_v().get(srcNode.id))
        while not neighborQueue.empty():
            currentVertex = neighborQueue.get()
            for j in self.graph.all_out_edges_of_node(currentVertex.id).keys():
                # print("currentVertex.weight")
                # print(currentVertex.weight)
                # print("self.graph.all_out_edges_of_node(currentVertex.id).get(j)")
                # print(self.graph.all_out_edges_of_node(currentVertex.id).get(j))

                tempWeight = currentVertex.weight + self.graph.all_out_edges_of_node(currentVertex.id).get(j)
                if self.graph.vertices.get(j).tag < 0 or tempWeight < self.graph.vertices.get(j).weight:
                    self.graph.vertices.get(j).info = "" + str(currentVertex.id)
                    self.graph.vertices.get(j).weight = tempWeight
                    self.graph.vertices.get(j).tag = 1
                    neighborQueue.put(self.graph.vertices.get(j))

        return 0

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        if len(node_lst) == 0:
            return None
        if len(node_lst) == 1:

            return node_lst, 0
        try:
            matrix = self.floydWarshall(self.graph)
            min_path = math.inf
            car_way = None
            next_permutation = permutations(node_lst)

            for i in list(next_permutation):
                current_path_weight = 0
                k = i[0]
                for j in i:

                        current_path_weight += matrix[k][j]
                        if k != j:
                            k = j

                current_path_weight += matrix[i[len(node_lst)-1]][i[0]]
                if current_path_weight < min_path:
                    min_path = current_path_weight
                    car_way = i

        except Exception as e:
            print(e)

        path = []
        if car_way == None:
            path = None
        else:
            for a in range(len(car_way)):
                path.append(car_way[a])
        return (path , min_path)

    def centerPoint(self) -> (int, float):
        matrix = self.floydWarshall(self.graph)

        maxPath = []

        for i in range(self.graph.v_size()):
            maxPath.append(0)
            for j in range(self.graph.v_size()):
                if matrix[i][j] > maxPath[i]:
                    maxPath[i] = matrix[i][j]


        min = math.inf
        id = -1
        for i in range(len(maxPath)):
            if maxPath[i] == min:
                secondMaxid = 0
                secondMaxi = 0
                for j in range(len(matrix)):
                    if matrix[j][id] > secondMaxid and matrix[j][id] < min:
                        secondMaxid = matrix[j][id]
                    if matrix[j][i] > secondMaxi and matrix[j][i] < min:
                        secondMaxi = matrix[j][i]

                if secondMaxid > secondMaxi:
                    id = i

            if maxPath[i] < min:
                min = maxPath[i]
                id = i
        return self.graph.get_all_v().get(id)

    def floydWarshall(self, a: DiGraph = DiGraph):
        matrix = []

        for i in range(a.numOfVertices):
            matrix.append([])
            for j in range(a.numOfVertices):
                matrix[i].append(math.inf)

        for k in a.get_all_v():
            matrix[k][k] = 0

        for i in range(a.numOfVertices):
            for j in range(a.numOfVertices):
                if a.all_out_edges_of_node(i).__contains__(j):
                    matrix[i][j] = a.all_out_edges_of_node(i).get(j)
        for i in range(a.v_size()):
            for j in range(a.v_size()):
                for k in range(a.v_size()):
                    if matrix[j][k] > matrix[j][i] + matrix[i][k]:
                        matrix[j][k] = matrix[j][i] + matrix[i][k]
        return matrix

    def plot_graph(self) -> None:
        """
        zur's implementation
        :return:
        """


    def __str__(self):
        return f"{self.graph}"

    def __repr__(self):
        return f"{self.graph}"

# if __name__ == '__main__':
#     graph = GraphAlgo()
#     graph.load_from_json("A0.json")
#     graph.centerPoint()
