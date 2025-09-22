from fastapi import FastAPI, APIRouter
from schema import Notification
import httpx
import os

# ==== CONFIG ====
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")

if not DISCORD_WEBHOOK_URL:
    print("no webhook url defined. Stopping server")
    exit()


# Create main app
app = FastAPI(title="Notifications API", version="1.0.0")

# Create router for notifications
router = APIRouter()

async def send_discord_message(message: str):
    async with httpx.AsyncClient() as client:
        await client.post(DISCORD_WEBHOOK_URL, json={"content": message})


@router.post("/discord")
async def send_message(payload: Notification):
    await send_discord_message(payload.message)
    return {"status" : "message send successfully"}

# Register router with prefix
API_PREFIX = "/notifications/v1"
app.include_router(router, prefix=API_PREFIX)