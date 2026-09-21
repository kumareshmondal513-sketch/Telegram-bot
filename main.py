import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import health, auth, game
from app.bot import start_bot-
@asynccontextmanager
async def lifespan(app: FastAPI):
    bot_task = asyncio.create_task(start_bot())
    yield
    bot_task.cancel()

app = FastAPI(
    title="TapRewards API Engine",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(auth.router)
app.include_router(game.router)

@app.get("/")
async def root():
    return {"message": "TapRewards Server-Authoritative API Running"}
