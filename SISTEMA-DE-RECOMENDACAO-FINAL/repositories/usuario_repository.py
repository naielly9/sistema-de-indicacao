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