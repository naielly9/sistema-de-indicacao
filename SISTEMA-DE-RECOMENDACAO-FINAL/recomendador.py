from models.usuario import Usuario
from models.produto import Produto
from repositories.produto_repository import ProdutoRepository
from repositories.usuario_repository import UsuarioRepository

class Recomendador:
    def __init__(self, usuario_repo: UsuarioRepository, produto_repo: ProdutoRepository):
        self.usuario_repo = usuario_repo
        self.produto_repo = produto_repo

    def recomendar(self, usuario: Usuario, limite: int = 5):
        produtos_recomendados = self.produto_repo.obter_produtos_por_genero_ordenados_por_popularidade(2)
        
        print(produtos_recomendados)





