from models import Palavra


SQL_BUSCA = 'SELECT nome from palavras_chaves where categoria = %s'
SQL_CRIA = 'INSERT into palavras_chaves (nome, categoria) values (%s, %s)'


class PalavraDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, palavra):
        cursor = self.__db.cursor()
        cursor.execute(SQL_CRIA, (palavra.nome, palavra.categoria))
        self.__db.commit()
        return palavra
