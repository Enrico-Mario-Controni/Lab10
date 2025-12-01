from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        nodes= DAO.num_nodes()
        for el in nodes:
            self.G.add_node(el)


        edges= DAO.num_edges()
        for (u,v), peso in edges.items():
            if peso >= threshold:
                self.G.add_edge(u, v, weight=peso)

        return self.G




    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        self._edges = self.G.number_of_edges()
        return self._edges


    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        self._nodes = self.G.number_of_nodes()
        return self._nodes



    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        tratte={}
        for u,v, data in self.G.edges(data=True):
            tratte[(u,v)]= data["weight"]
        return tratte





