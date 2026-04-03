from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database import create_tables
from src.routers import auth, accounts, transactions


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="API Bancária Assíncrona",
    description="API RESTful assíncrona para gerenciar contas correntes e transações bancárias com autenticação JWT.",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(accounts.router, prefix="/accounts", tags=["Contas"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transações"])


@app.get("/", tags=["Health"])
async def root():
    return {"status": "online", "message": "API Bancária Assíncrona com FastAPI"}
