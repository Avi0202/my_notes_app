from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from .config import templates
from .routes import router  # Import the router
import os

app = FastAPI()

app.include_router(router)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

