from pymongo import MongoClient

class Interface_db:
    client = ""
    database = ""
    collection = ""
    
    def __init__(self, host="mongodb://127.0.0.1:27017/"):
        self.client = MongoClient(host)
        self.set_database()
        self.set_collection()
    
    def set_database(self, database="teste"):
        self.database=self.client[database]
        
    def set_collection(self, collection="professor"):
        self.collection = self.database[collection]
    
    def buscar(self):
        lista = []
        dados = self.collection.find()
        for d in dados:
            lista.append(d)
        return lista
    
    def inserir_um(self, dado):
        self.collection.insert_one(dado)
        
    def inserir_varios(self, dados):
        self.collection.insert_many(dados)
        
    def atualizar_um(self, regra, novo_dado):
        self.collection.update_one(regra, novo_dado)
        
    def atualizar_varios(self, regra, novo_dado):
        self.collection.update_many(regra, novo_dado)
        
    def excluir_um(self, regra):
        self.collection.delete_one(regra)
        
    def excluir_varios(self, regra):
        self.collection.delete_many(regra)