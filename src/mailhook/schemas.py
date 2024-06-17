from pydantic import BaseModel


class MailHook(BaseModel):
    subject: str
    body: str
    from_email: str
    date: str


class MailHookResponse(BaseModel):
    success: bool
    payload: dict | None = None