# 📊 Processamento de Números Assíncrono - Desafio FPF

Aplicação full stack que permite o envio de três números inteiros para cálculo de média e mediana de forma assíncrona. Utiliza Django + Django REST no backend, Angular no frontend, RabbitMQ para orquestração de tarefas assíncronas com Celery, banco de dados SQLite e todo o ambiente dockerizado.

---

## 📌 Objetivo

Criar uma solução assíncrona onde um usuário pode:
- Enviar três números via forms Angular.
- Acompanhar o status do processamento em uma tabela.
- Visualizar os resultados (média e mediana) após o processamento.

---

## 🧱 Arquitetura da Solução

### 🔙 Backend – Django + DRF

- Dois endpoints:
  - `POST /processar/`: salva os dados no banco e envia mensagem ao RabbitMQ.
  - `GET /status/{id}`: retorna status atual da requisição e resultados, se houver.
- Uso de `DecimalField` com `max_digits=20` para garantir precisão nos cálculos.
- Testes unitários utilizando `Django TestCase` por simplicidade e compatibilidade imediata.
- Validações básicas implementadas para casos de entrada inválida e tipos incorretos.

> 💡 **Decisão técnica:** optou-se por `DecimalField` ao invés de `FloatField` devido à maior precisão matemática, e por `Django TestCase` ao invés de `Pytest` para evitar complexidade de configuração e otimizar o tempo.

### 🧠 Worker – Python + Celery

- Conecta-se ao RabbitMQ para consumir as mensagens de processamento.
- Realiza o cálculo da média e da mediana.
- Atualiza o status da requisição e armazena os resultados no banco.

> 💡 **Decisão técnica:** processamento simples foi feito diretamente dentro da task Celery. A mediana é calculada com base nos três números ordenados.

### 🧮 Banco de Dados – SQLite

- Modelo `Calculator` com os campos:
  - `id`, `num1`, `num2`, `num3`
  - `media`, `mediana`
  - `status` (inicia com "Processando" e termina com "Concluído")

> 💡 **Decisão técnica:** uso do SQLite por praticidade no desenvolvimento local e simplicidade no setup Docker, embora o código seja facilmente adaptável para PostgreSQL.

### 💻 Frontend – Angular

- Formulário para inserção de três números.
- Botão “Calcular” que envia os dados à API.
- Tabela dinâmica exibindo todas as requisições, seus status e os respectivos resultados.

> 💡 **Decisão técnica:** optou-se por uma UI funcional e direta para focar na solidez da arquitetura geral.

### 🐳 Docker

- Orquestração feita com `docker-compose`.
- Serviços:
  - Angular frontend
  - Django backend
  - Celery worker
  - RabbitMQ
  - Redis (broker/cache para Celery)
- Comunicação entre serviços garantida via rede Docker interna.

---

## ✅ Funcionalidades

- [x] Envio de três números via interface Angular.
- [x] Processamento assíncrono com RabbitMQ + Celery.
- [x] Cálculo de média e mediana.
- [x] Armazenamento e atualização no banco.
- [x] Interface atualizável manualmente.
- [x] Aplicação dockerizada ponta-a-ponta.
- [x] Testes unitários básicos no backend.

---

## 🚫 Funcionalidades não implementadas (por restrição de tempo)

- ❌ Atualização automática via Polling ou WebSockets.

> ⚠️ Apesar de serem possíveis com relativa facilidade, essas funcionalidades demandariam ajustes significativos no frontend e backend. Dado o tempo curto para entrega, priorizou-se a entrega robusta da arquitetura principal. A implementação de WebSockets, por exemplo, exigiria configuração adicional com Django Channels e Redis, o que sairia do escopo de tempo viável.

---

## 🧪 Testes

Os testes foram escritos utilizando `Django TestCase`, com foco em:

- Caso de uso principal (valores válidos e worker ativo).
- Validação de payload ausente.
- Validação de tipo incorreto.

---

## 🚀 Como rodar a aplicação

### 📦 Pré-requisitos

- [Docker](https://www.docker.com/) 
- [Docker Compose](https://docs.docker.com/compose/) 

### 🧰 Passos para executar a aplicação

1. Clone este repositório:

```bash
git clone https://github.com/gabriellvalle/FPFChallenge.git
cd FPFChallenge
```

2. Construa e suba os containers com Docker Compose:

```bash
docker-compose up --build
```

3. Acesse os serviços

Espere alguns insantes para os containers subirem completamente, isto pode durar alguns poucos minutos.
Em seguida, acesse:
- Frontend (Angular): http://localhost:4200 (aqui é onde se poderá usar a interce e aplicação)
- Backend (API Django): http://localhost:8000/admin/ (⚠️ Obs: o backend não possui página inicial, apenas o painel /admin e os endpoints da API.)

Após subir os containers, execute:
```bash
docker exec -it django_app python manage.py createsuperuser
```
Basta seguir as instruções de criação e acessar.

- Painel do RabbitMQ: http://localhost:15672
```bash
Usuário: guest
Senha: guest
```
