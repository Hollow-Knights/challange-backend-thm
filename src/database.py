import os
from pymongo import MongoClient

# Configurações do MongoDB (hardcoded)
MONGODB_URL = "mongodb+srv://guialves:witrwit1@cluster0.3eslth4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = "empresa_api"

# Criar uma conexão com o MongoDB
try:
    client = MongoClient(MONGODB_URL)
    # Verifica a conexão
    client.admin.command('ping')
    print("✅ Conectado ao MongoDB com sucesso!")
except Exception as e:
    print(f"❌ Erro ao conectar ao MongoDB: {e}")
    raise e  # Re-lança a exceção para que a aplicação não continue com o banco desconectado

db = client[DB_NAME]

# Coleções
users_collection = db.users 
