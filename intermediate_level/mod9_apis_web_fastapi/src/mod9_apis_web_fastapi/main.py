from fastapi import FastAPI

from .database import Base, engine
from .routers import auth, orders

Base.metadata.create_all(bind=engine)  # tabla orders (sqlite)

app = FastAPI(
    title="Orders API",
    description="API para gestionar órdenes con autenticación JWT",
    version="1.0.0",
)
# endpoints:
app.include_router(auth.router)
app.include_router(orders.router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Orders API is running"}
