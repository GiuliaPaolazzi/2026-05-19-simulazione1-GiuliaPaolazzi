from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._generi = DAO.get_all_genre(self)


    def buildGraph(self):
        pass

    @property
    def generi(self):
        return self._generi