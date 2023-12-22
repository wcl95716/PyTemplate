from fastapi import FastAPI


from api.chat_record.api import CharRecordAPI

from api.support_ticket.api import TicketAPI


fast_api = FastAPI()
fast_api.include_router(
    TicketAPI().router, prefix="/ticket", tags=["Ticket Operations"]
)
fast_api.include_router(
    CharRecordAPI().router, prefix="/chat_record", tags=["Chat Record Operations"]
)


@fast_api.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}
