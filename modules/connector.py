import mysql.connector

class Interface_mysql:
    usuario, senha, host, banco = "", "", "", ""
    
    def __init__(self, usuario, senha, host, banco):
        try:
            self.usuario = usuario
            self.senha = senha
            self.host = host
            self.banco = banco
        except Exception as e:
            print(str(e))
    
    def conectar(self):
        try:
            conn = mysql.connector.connect(user=self.usuario, password=self.senha, host=self.host, database=self.banco)
            cursor = conn.cursor()
            return conn, cursor
        except Exception as e:
            print(str(e))
            
    def desconectar(self, con, cursor):
        try:
            cursor.close()
            con.commit()
            con.close()
        except Exception as e:
            print(str(e))
    
    # do CRUD inserir é o C de create
    def inserir(self, query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            self.desconectar(con, cursor)
        except Exception as e:
            print(str(e))
    
    # do CRUD selecionar é o R de read
    def selecionar(self, query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            result = cursor.fetchall()
            resultado = []
            for i in result:
                resultado.append(i)
            return resultado
        except Exception as e:
            print(str(e))
        finally:
            self.desconectar(con, cursor)
            
    # do CRUD atualizar é o U de update
    def atualizar(self, query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            self.desconectar(con, cursor)
        except Exception as e:
            print(str(e))
    
    # do CRUD excluir é o D de delete
    def excluir(self, query):
        try:
            con, cursor = self.conectar()
            cursor.execute(query)
            self.desconectar(con, cursor)
        except Exception as e:
            print(str(e))