# challenge-monorepo-python-redis-angular

## Descrição
Monorepo com backend em Python/Flask e frontend em Angular, integrando autenticação JWT, CRUD de produtos, fila com Redis e worker.

## Estrutura
```
/backend
  /app
    __init__.py
    models/
    routes/
    services/
    auth/
    worker.py
  requirements.txt
/frontend
  (projeto Angular)
docker-compose.yml (opcional)
README.md
```

## Backend
- Python 3.x
- Flask
- Flask-SQLAlchemy
- PostgreSQL
- Redis
- Autenticação JWT
- Worker para fila

## Frontend
- Angular
- HttpClient para API REST
- Route Guard para proteção de rotas


## Como rodar

### Backend
1. Instale dependências:
   ```sh
   cd backend
   pip install -r requirements.txt
   ```
2. Configure variáveis de ambiente (banco, Redis, JWT).
   - Exemplo: crie um arquivo `.env` ou exporte variáveis no shell.
3. Inicie o backend:
   ```sh
   python run.py
   ```
4. Inicie o worker:
   ```sh
   python app/worker.py
   ```
5. Acesse a documentação da API (Swagger):
   - [http://localhost:5000/api/docs](http://localhost:5000/api/docs)

### Frontend
1. Instale dependências:
   ```sh
   cd frontend
   npm install
   ```
2. Inicie o frontend:
   ```sh
   ng serve
   ```
3. Acesse [http://localhost:4200](http://localhost:4200)

### Docker Compose
Para subir todos os serviços juntos:
```sh
docker-compose up --build
```
Consulte o arquivo `docker-compose.yml` para detalhes.


## Funcionalidades
- Login/logout com JWT
- Proteção de rotas no frontend e backend
- CRUD de produtos protegido
- Operações de produtos via fila Redis
- Worker processando fila
- Documentação da API via Swagger


## Observações
- Ajuste URLs e variáveis conforme ambiente.
- Consulte os arquivos de cada pasta para detalhes de implementação.
- Para testes automatizados e diferenciais, veja instruções adicionais no backend/frontend.
