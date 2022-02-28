from modules.connector import Interface_mysql
from modules.mongo import Interface_db
from modules.classe_professor import Professor
import time

def menu():
    """Menu do programa contendo cinco opções, representando uma função específica cada.  
       O menu solicita ao usuário que esolha um entre as cinco opções.

        Args:
            op (int): armazena o valor da opção escolhida.

        Returns:
            [int]: retorna a opção escolhida.
        """
    lista_op = [1, 2, 3, 4, 0]

    while True:
        try: 
            print("-" * 70)
            print("MENU:\n")
            op = int(input("1 - Cadastrar\n2 - Atualizar\n3 - Excluir\n4 - Listar\n0 - Sair\n\n->"))
            
            if op not in (lista_op):
                print("Opção Inválida!")
            else:
                return op
        except:
            print("Opção inválida!")

if (__name__ == "__main__"):
    try:
        banco_sql = Interface_mysql("root", "", "localhost", "mydatabase") #CRIANDO CONEXÃO COM O MYSQL
        banco_mongo = Interface_db() #CRIANDO CONEXAO COM O MONGO DB

        op = menu() #CHAMANDO O MENU

        while True:
            if op == 1: #CADASTRAR DADOS NO MYSQL E NO MONGO
                print("-" * 70)
                print("INSERIR:")

                try:
                    id = int(input("\nId: "))
                    nome = input("Nome: ")
                    materia = input("Matéria: ")
                except Exception as e:
                    print(str(e))

                professor = Professor(id, nome, materia)

                #ENVIANDO DADOS PARA O MYSQL
                query = f"""INSERT INTO professor(id, nome, materia) 
                            VALUES{professor.get_id(), professor.get_nome(), professor.get_materia()}"""
                banco_sql.inserir(query)

                #ENVIANDO DADOS PARA O MONGO DB
                dados = {"id":professor.get_id(), "nome":professor.get_nome(), "materia":professor.get_materia()}
                banco_mongo.inserir_um(dados)

                print("\nINSERÇÃO CONFIRMADA!")
                time.sleep(2)
                op = menu() #RETORNANDO AO MENU

            elif op == 2: #ATUALIZAR DADOS
                print("-" * 70)
                print("ATUALIZAR:")
                
                try:
                    id = int(input("\nId do professor(a) a ser atualizado: "))
                    nome = input("Novo nome: ")
                    materia = input("Nova matéria: ")
                except Exception as e:
                    print(str(e))

                professor = Professor(id, nome, materia)

                #ATUALIZANDO DADOS NO MYSQL
                query = f"""UPDATE professor 
                            SET nome = '{professor.get_nome()}', materia = '{professor.get_materia()}'
                            WHERE id = {str(id)};"""
                banco_sql.atualizar(query)

                #ATUALIZANDO DADOS NO MONGO DB
                regra = {"id":professor.get_id()}
                dados = {"$set":{"nome":professor.get_nome(), "materia":professor.get_materia()}}
                banco_mongo.atualizar_um(regra, dados)

                print("\nATUALIZAÇÃO CONFIRMADA!")
                time.sleep(2)
                op = menu() #RETORNANDO AO MENU

            elif op == 3: #EXCLUIR DADOS
                print("-" * 70)
                print("EXCLUIR:")
                
                try:
                    id = int(input("\nId do professor(a) a ser excluído: "))
                except Exception as e:
                    print(str(e))

                #EXCLUINDO DADOS NO MYSQL
                query = f"""DELETE FROM professor 
                            WHERE id = {str(id)};"""
                banco_sql.excluir(query)

                #EXCLUINDO DADOS NO MONGO DB
                regra = {"id":id}
                banco_mongo.excluir_um(regra)

                print("\nEXCLUSÃO CONFIRMADA!")
                time.sleep(2)
                op = menu() #RETORNANDO AO MENU

            elif op == 4: #LISTAR DADOS
                print("-" * 70)
                print("DADOS MYSQL:\n")

                #IMPRIMINDO DADOS DA TABELA NO MYSQL
                dados_mysql = banco_sql.selecionar("SELECT * FROM professor") #ARMAZENANDO OS DADOS DA TABELA EM UMA VARIÁVEL
                dados_my = []

                for d in dados_mysql: #PERCORRENDO AS LINHAS ARMAZENADAS E ATRIBUINDO OS VALORES DAS COLUNAS PARA OS SEUS RESPECTIVOS ATRIBUTOS NA CLASSE "PROFESSOR"
                    professor = Professor(d[0], d[1], d[2])
                    dados_my.append(professor) #ARMAZENANDO OS OBJETOS GERADOS EM UMA LISTA

                for d in dados_my: #PERCORRENDO A LISTA DE OBJETOS E CHAMANDO O METODO "PRINTAR" DE CADA UM PARA MOSTRAR SEUS ATRIBUTOS
                    d.printar()

                #IMPRIMINDO DADOS DA TABELA NO MONGO DB
                print("\n")
                print("-" * 70)
                print("DADOS MONGO DB:\n")

                dados_mongo = banco_mongo.buscar()
                valores = []
                dados_mo = []

                for d in dados_mongo:
                    for chave, valor in d.items():
                        valores.append(valor)
                    professor = Professor(valores[1], valores[2], valores[3])
                    dados_mo.append(professor)
                    valores.clear()

                for d in dados_mo: #PERCORRENDO A LISTA DE OBJETOS E CHAMANDO O METODO "PRINTAR" DE CADA UM PARA MOSTRAR SEUS ATRIBUTOS
                    d.printar()

                print("\n\nLISTAGEM CONFIRMADA!")
                time.sleep(7)
                op = menu() #RETORNANDO AO MENU
            else:
                print("-" * 70)
                print("FECHANDO PROGRAMA!")
                break
    except Exception as e:
        print(str(e))
