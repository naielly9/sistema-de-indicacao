from models.produto import Produto

class ProdutoRepository:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def adicionar(self, produto: Produto):
        self.cursor.execute(
            'INSERT INTO produtos (nome, categoria_id, popularidade) VALUES (?, ?, ?)', 
            (produto.nome, produto.categoria_id, produto.popularidade)
        )
        self.conexao.commit()
    
    def obter(self, id: int):
        self.cursor.execute('SELECT * FROM produtos WHERE id = ?', (id,))
        produto = self.cursor.fetchone()
        return Produto(*produto) if produto else None
    
    def obter_produtos_por_genero_ordenados_por_popularidade(self, genero_id: int):
        self.cursor.execute(
            'SELECT id, nome, popularidade FROM produtos WHERE genero_id = ? ORDER BY popularidade DESC', 
            (genero_id,)
        )
        return [Produto(*produto) for produto in self.cursor.fetchall()]
