import copy

from GraphInterface import GraphInterface
from NodeData import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.numOfVertices = 0
        self.numOfEdges = 0
        self.countMc = 0
        self.vertices = {}
        self.inEdges = {}
        self.outEdges = {}

    def __copy__(self, other):
        # todo implement me

        def v_size(self) -> int:
            """
            zur's implementation
            :return:  number of vertices
            """

    def e_size(self) -> int:
        return self.numOfEdges

    def get_all_v(self) -> dict:
        """
        zur's implementation
        :return:
        """

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        this function is checking, if the given node's id is
        in value of another node's id,
        which means, that they are connected
        if it is , i put the node in another dictionary
        and return the dictionary
        :param id1:
        :return:
        """
        ans_dic = {}
        if id1 in self.vertices:
            for a in self.vertices.get(id1):
                ans_dic = a
        return ans_dic

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        zur's implementation
        :param id1:
        :return:
        """

    def get_mc(self) -> int:
        return self.countMc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        zur's implementation
        :param id1:
        :param id2:
        :param weight:
        :return:
        """

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        this function is adding the object Node to a dictionary
        if it is not there
        also we are updating the ModeCount and the amount of vertices
        in our graph
        i used the self.vertices.update(...), because i think that
        it is instead of .add
        see here - https://stackoverflow.com/questions/1024847/how-can-i-add-new-keys-to-a-dictionary
        :param node_id:
        :param pos:
        :return:
        """
        if node_id not in self.vertices:
            node = Node(node_id, pos)
            self.vertices.update(node_id, node)
            self.countMc += 1
            self.numOfVertices += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        zur's implementation
        :param node_id:
        :return:
        """

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        i am not sure about this implementation
        but i am checking if both of id are in vertices dict
        then i check if given id is contains in a value of another id
        if yes , i remove it
        also the opposite
        :param node_id1:
        :param node_id2:
        :return:
        """
        if node_id1 in self.vertices and node_id2 in self.vertices:
            ans = False
            if self.vertices.get(node_id1) == node_id2:
                self.vertices.pop(node_id1)
                self.countMc += 1
                self.numOfEdges -= 1
                ans = True
            if self.vertices.get(node_id2) == node_id1:
                self.vertices.pop(node_id2)
                self.countMc += 1
                self.numOfEdges -= 1
                ans = True

        return ans