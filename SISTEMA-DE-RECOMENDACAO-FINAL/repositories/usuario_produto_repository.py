class UsuarioProdutoRepository:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def relacionar_usuario_produto(self, usuario_id: int, produto_id: int):
        self.cursor.execute('INSERT INTO usuarios_produtos (usuario_id, produto_id) VALUES (?, ?)', (usuario_id, produto_id))
        self.conexao.commit()
    
    # def obter_produtos_do_usuario(self, usuario_id: int):
    #     self.cursor.execute('''
    #         SELECT p.id, p.nome
    #         FROM produtos p
    #         JOIN usuarios_produtos up ON p.id = up.produto_id
    #         WHERE up.usuario_id = ?
    #     ''', (usuario_id,))
    #     produtos = self.cursor.fetchall()
    #     return produtos