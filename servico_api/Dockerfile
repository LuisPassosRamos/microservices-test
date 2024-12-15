# Usa a imagem oficial do Python
FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exposição da porta 5000
EXPOSE 5000

# Comando para rodar o serviço
CMD ["python", "app.py"]
