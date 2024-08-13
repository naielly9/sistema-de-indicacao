from dataclasses import dataclass

@dataclass
class Produto: 
    id: int
    nome: str
    popularidade: int
    categoria_id: int