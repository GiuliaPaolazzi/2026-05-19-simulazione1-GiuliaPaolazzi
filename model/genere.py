from dataclasses import dataclass

@dataclass
class Genere:
    id_genere: int
    name: str



    def __hash__(self):
        return self.id_genere

    def __str__(self):
        return f"{self.name}"

    def __eq__(self, other):
        return self.id_genere == other.id_genere