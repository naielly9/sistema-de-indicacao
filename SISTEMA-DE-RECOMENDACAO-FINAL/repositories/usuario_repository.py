from models.usuario import Usuario

class UsuarioRepository:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def adicionar(self, usuario: Usuario):
        self.cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (usuario.nome,))
        self.conexao.commit()
    
    def obter(self, id: int):
        self.cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
        usuario = self.cursor.fetchone()
        return Usuario(*usuario) if usuario else None
    
    def usuario_possui_produto(self, usuario_id: int, produto_id: int):
        self.cursor.execute('SELECT COUNT(*) FROM usuarios_produtos WHERE usuario_id = ? AND produto_id = ?', (usuario_id, produto_id))
        return self.cursor.fetchone()[0] > 0
    
    def obter_categoria_mais_frequente_do_usuario(self, usuario_id: int):
        self.cursor.execute('''
            SELECT p.categoria_id, COUNT(p.categoria_id) as categoria_count 
            FROM produtos p
            JOIN usuarios_produtos up ON p.id = up.produto_id
            WHERE up.usuario_id = ?
            GROUP BY p.categoria_id
            ORDER BY categoria_count DESC
            LIMIT 1
        ''', (usuario_id,))
        resultado = self.cursor.fetchone()
        return resultado[0] if resultado else None