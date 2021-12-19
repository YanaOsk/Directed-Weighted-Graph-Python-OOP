import collections
import math
import queue
from _ast import List
from collections import deque

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from NodeData import Node
from DiGraph import DiGraph
import json


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = DiGraph):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        """
        zur's implementation
        :return:
        """

    def load_from_json(self, file_name: str) -> bool:
        graph = DiGraph()
        try:
            with open(file_name, "r+") as f:
                dict = json.load(f)
                for k in dict["Nodes"]:
                    n = Node(k["pos"].split(","))
                    node = Node(n['id'], (float(n[0]), float(n[1])), float(n[2]))
                    graph.add_node(node.id, node.pos)
                for e in dict["Edges"]:
                    src = e["src"]
                    dest = e["dest"]
                    weight = e["w"]
                    graph.add_edge(src, dest, weight)
                self.graph = graph
        except IOError as e:
            print(e)

    def save_to_json(self, file_name: str) -> bool:
        """
       zur's implementation
       """

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        temp = queue.LifoQueue()
        if self.graph.get_all_v().get(id1) is not None and self.graph.get_all_v().get(id2) is not None:
            if id1 == id2:
                path.append(self.graph.get_all_v().get(id1))
                return path
            self.dijkstra(self.graph.get_all_v().get(id1))
            if self.graph.get_all_v().get(id2).weight == math.inf:
                return None
            destNode = self.graph.get_all_v().get(id2)
            try:
                while self.graph.get_all_v().get(id1) != destNode:
                    temp.append(destNode)
                    destNode = self.graph.get_all_v().get(int(destNode.info))
                temp.append(self.graph.get_all_v().get(id1))
            except ValueError as e:
                print(e)
                return None
            except Exception as e:
                print(e)
                return None
            while not temp.empty():
                path.append(temp.get())
        return path

    def dijkstra(self, srcNode: Node = Node):
        neighborQueue = collections.deque
        for i in self.graph.get_all_v().values():
            i.weight(math.inf)
            i.tag(-1)
            i.info("")
        if self.graph.get_all_v().get(srcNode) is not None:
            srcNode.weight(0)
            srcNode.info("" + srcNode.id)
            srcNode.tag(1)
            neighborQueue.appendleft(srcNode)
        while not neighborQueue.empty():
            if neighborQueue.__getitem__() is not None:
                currentVertex = neighborQueue.pop()
                if currentVertex is not None:
                    for j in self.graph.all_out_edges_of_node(currentVertex.id).keys():
                        dstVertex = self.graph.vertices.get(j)
                        tempWeight = currentVertex.weight + self.graph.vertices.get(currentVertex.id).outEdges.get(j)
                        if dstVertex.tag < 0 or tempWeight < dstVertex.weight:
                            neighborQueue.appendleft(dstVertex)
                            dstVertex.info("" + currentVertex.id)
                            dstVertex.weight(tempWeight)
                            dstVertex.tag(1)

        return 0

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        zur's implementation
        :param node_lst:
        :return:
        """

    def centerPoint(self) -> (int, float):
        matrix = self.floydWarshall(self.graph)
        mat_1 = matrix[0]
        mat_2 = matrix[1]
        maxPath = []
        for i in range(mat_1):
            for j in range(mat_2):
                if matrix[i][j] > maxPath[i]:
                    maxPath[i] = matrix[i][j]
        min = math.inf
        id = -1
        for i in range(maxPath):
            if maxPath[i] == min:
                secondMaxid = 0
                secondMaxi = 0
                for j in range(matrix):
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
        matrix = [[], []]
        mat_1 = matrix[0]
        mat_2 = matrix[1]
        for i in range(mat_1):
            for j in range(mat_2):
                mat_1[i].append(math.inf)
                mat_2[j].append(math.inf)
        for k in self.graph.get_all_v():
            mat_1[k.id].append(0)
            mat_2[k.id].append(0)
        for src in self.graph.all_in_edges_of_node():
            mat_1[src.id].append(src.weight)
        for dest in self.graph.all_out_edges_of_node():
            mat_2[dest.id].append(dest.weight)
        for i in self.graph.v_size():
            for j in self.graph.e_size():
                for k in self.graph.v_size():
                    if matrix[j][k] > matrix[j][i] + matrix[i][k]:
                        matrix[j][k] = matrix[j][i] + matrix[i][k]
        return matrix

    def plot_graph(self) -> None:
        """
        zur's implementation
        :return:
        """
