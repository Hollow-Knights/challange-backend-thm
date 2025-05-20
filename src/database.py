import os
from pymongo import MongoClient

# Configurações do MongoDB (hardcoded)
MONGODB_URL = "mongodb+srv://firebird748:5YDZGZIkWnXRpU8Q@challengefiap.zspngt1.mongodb.net/?retryWrites=true&w=majority&appName=CHALLENGEFIAP"
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