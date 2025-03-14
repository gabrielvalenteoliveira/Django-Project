# Estágio base (builder)
FROM python:3.11 AS builder

# Define o diretório de trabalho
WORKDIR /app

# Configurações de ambiente para Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Atualiza o pip e instala as dependências
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Estágio final (produção)
FROM python:3.11-slim

# Cria um usuário não-root e configura permissões
RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser:appuser /app

# Define o diretório de trabalho
WORKDIR /app

# Configurações de ambiente para Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Muda para o usuário appuser
USER appuser

# Copia as dependências instaladas do builder
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/

# Copia os arquivos do projeto do host (incluindo manage.py)
COPY --chown=appuser:appuser . /app/

# Expõe a porta
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]