from dataclasses import dataclass

@dataclass
class Artista:
    id_artista: int
    name: str
    popolarita: int



    def __hash__(self):
        return self.id_artista

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other):
        return self.id_artista == other.id_artista