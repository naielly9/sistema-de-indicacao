from models.usuario import Usuario
from models.produto import Produto
from repositories.produto_repository import ProdutoRepository
from repositories.usuario_repository import UsuarioRepository

class Recomendador:
    def __init__(self, usuario_repo: UsuarioRepository, produto_repo: ProdutoRepository):
        self.usuario_repo = usuario_repo
        self.produto_repo = produto_repo

    def recomendar(self, usuario_id: int, limite: int = 2):
        categoria_mais_frequente = self.usuario_repo.obter_categoria_mais_frequente_do_usuario(usuario_id)
        print("Categoria mais frequente: ", categoria_mais_frequente)
        
        produtos_recomendados = self.produto_repo.obter_produtos_por_categoria_ordenados_por_popularidade(categoria_mais_frequente, limite)
        print("Produtos recomendados:", produtos_recomendados)

        return produtos_recomendados





