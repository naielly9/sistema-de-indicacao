from models.categoria import Categoria

class CategoriaRepository:
    def __init__(self, cursor, conexao):
        self.cursor = cursor
        self.conexao = conexao

    def adicionar(self, categoria: Categoria):
        self.cursor.execute('INSERT INTO categorias (nome) VALUES (?)', (categoria.nome,))
        self.conexao.commit()
    
    def obter(self, id: int):
        self.cursor.execute('SELECT * FROM categorias WHERE id = ?', (id,))
        categoria = self.cursor.fetchone()
        return Categoria(*categoria) if categoria else None
    
    # def obter_todos(self):
    #     self.cursor.execute('SELECT * FROM categorias')
    #     return self.cursor.fetchall()
