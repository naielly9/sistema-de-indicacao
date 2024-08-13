from banco_de_dados import BancoDeDados
from models.usuario import Usuario
from models.produto import Produto
from models.categoria import Categoria
from repositories.usuario_repository import UsuarioRepository
from repositories.produto_repository import ProdutoRepository
from repositories.usuario_produto_repository import UsuarioProdutoRepository
from repositories.categoria_repository import CategoriaRepository
from recomendador import Recomendador

bd = BancoDeDados()
cursor = bd.obter_cursor()
conexao = bd.obter_conexao()

usuario_repository = UsuarioRepository(cursor, conexao)
produto_repository = ProdutoRepository(cursor, conexao)
usuario_produto_repository = UsuarioProdutoRepository(cursor, conexao)
categoria_repository = CategoriaRepository(cursor, conexao)

recomendador = Recomendador(usuario_repository, produto_repository)

novo_usuario = Usuario(id=None, nome="João Cândido")
usuario_repository.adicionar(novo_usuario)

nova_categoriaA = Categoria(id=None, nome="Romance")
nova_categoriaB = Categoria(id=None, nome="Drama")
nova_categoriaC = Categoria(id=None, nome="Ação")
nova_categoriaD = Categoria(id=None, nome="Aventura")

categoria_repository.adicionar(nova_categoriaA)
categoria_repository.adicionar(nova_categoriaB)
categoria_repository.adicionar(nova_categoriaC)
categoria_repository.adicionar(nova_categoriaD)

novo_produtoA = Produto(id=None, categoria_id=1, nome="Produto1", popularidade=120)
novo_produtoB = Produto(id=None, categoria_id=2, nome="Produto2", popularidade=12)
novo_produtoC = Produto(id=None, categoria_id=2, nome="Produto3", popularidade=16)
novo_produtoD = Produto(id=None, categoria_id=2, nome="Produto4", popularidade=124)
novo_produtoE = Produto(id=None, categoria_id=2, nome="Produto5", popularidade=500)
novo_produtoF = Produto(id=None, categoria_id=3, nome="Produto6", popularidade=3)
novo_produtoG = Produto(id=None, categoria_id=3, nome="Produto7", popularidade=16)
novo_produtoH = Produto(id=None, categoria_id=3, nome="Produto8", popularidade=119)

produto_repository.adicionar(novo_produtoA)
produto_repository.adicionar(novo_produtoB)
produto_repository.adicionar(novo_produtoC)
produto_repository.adicionar(novo_produtoD)
produto_repository.adicionar(novo_produtoE)
produto_repository.adicionar(novo_produtoF)
produto_repository.adicionar(novo_produtoG)
produto_repository.adicionar(novo_produtoH)

usuario_produto_repository.relacionar_usuario_produto(1, 1)
usuario_produto_repository.relacionar_usuario_produto(1, 2)
usuario_produto_repository.relacionar_usuario_produto(1, 3)
usuario_produto_repository.relacionar_usuario_produto(1, 4)
usuario_produto_repository.relacionar_usuario_produto(1, 5)
usuario_produto_repository.relacionar_usuario_produto(1, 6)
usuario_produto_repository.relacionar_usuario_produto(1, 7)
usuario_produto_repository.relacionar_usuario_produto(1, 8)

recomendador.recomendar(1)