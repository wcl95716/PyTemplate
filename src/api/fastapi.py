

import sys
sys.path.append("./src")

from fastapi import FastAPI

from services.support_ticket.web_api.api import TicketAPI


fast_api = FastAPI()
fast_api.include_router(TicketAPI().router, prefix="/ticket",tags=["Ticket Operations"])


@fast_api.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}

