from dataclasses import dataclass
from model.artista import Artista
@dataclass
class Connessione:
    artista1: Artista
    artista2: Artista



    def __hash__(self):
        return (self.artista1, self.artista2)

    def __str__(self):
        pass

    def __eq__(self, other):
        pass