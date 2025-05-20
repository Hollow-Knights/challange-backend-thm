FROM python:3.11-slim

WORKDIR /app/src

# Copiar requirements primeiro para aproveitar o cache de camadas do Docker
COPY requirements.txt /app/

# Instalar dependências
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar arquivos da aplicação
COPY ./src /app/src

# Definir variáveis de ambiente
ENV PYTHONPATH=/app/src
ENV PYTHONUNBUFFERED=1

# Expor a porta que o servidor utiliza
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 