

import sys
sys.path.append("./src")

from fastapi import FastAPI

from models.support_ticket.web_api.api import TicketAPI


app = FastAPI()
app.include_router(TicketAPI().router, prefix="/ticket",tags=["Ticket Operations"])


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}

