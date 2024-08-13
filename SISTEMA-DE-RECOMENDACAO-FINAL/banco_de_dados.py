import sqlite3

class BancoDeDados:
    def __init__(self, nome='sistema_de_recomendacao'):
        self.conectar(nome)
        self.cursor = self.conexao.cursor()
        self.criar_tabelas()
        
    def conectar(self, nome: str):
        self.conexao = sqlite3.connect(nome)

    def obter_cursor(self):
        return self.cursor
    
    def obter_conexao(self):
        return self.conexao
        
    def criar_tabelas(self):        
        # Cria tabela de categorias
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')

        # Cria tabela de produtos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                popularidade INTEGER DEFAULT 0,
                categoria_id INTEGER,
                FOREIGN KEY (categoria_id) REFERENCES categorias (id)
            )
        ''')

        # Cria tabela de usuários
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
        
        # Cria tabela de usuários-produtos
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios_produtos (
                usuario_id INTEGER,
                produto_id INTEGER,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id),
                FOREIGN KEY (produto_id) REFERENCES produtos (id),
                PRIMARY KEY (usuario_id, produto_id)
            )
        ''')
        
        self.conexao.commit()

    # def adicionar_usuario(self, usuario: Usuario):
    #     self.cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (usuario.nome,))
    #     self.conexao.commit()

    # def obter_usuario(self, id: int):
    #     self.cursor.execute('SELECT * FROM usuarios WHERE id = ?', (id,))
    #     usuario = self.cursor.fetchone()
    #     return Usuario(*usuario)

    def desconectar(self):
        self.conexao.close()