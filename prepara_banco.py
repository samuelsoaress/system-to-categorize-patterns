import pymysql
import pprint

def main(args):
    bd = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                db='data_note',
                                cursorclass=pymysql.cursors.DictCursor)
    cursor = bd.cursor()
    sql = '''SELECT nome from palavras_chaves where categoria = 10'''
    try:
        # Execute o comando
        cursor.execute(sql)
        print(type(cursor.execute(sql)))
        # Confirme a inserção na base de dados
        bd.commit()
 
    except:
        # limpe tudo se algo saiu errado
        bd.rollback()
        print("Erro na inserção de dados na tabela de fornecedores")
    # fecha a conexão
    bd.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))