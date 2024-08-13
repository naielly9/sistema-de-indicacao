class UsuarioProdutoRepository:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def relacionar_usuario_produto(self, usuario_id: int, produto_id: int):
        self.cursor.execute('INSERT INTO usuarios_produtos (usuario_id, produto_id) VALUES (?, ?)', (usuario_id, produto_id))
        self.conexao.commit()