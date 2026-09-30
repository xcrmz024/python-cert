from fastapi import FastAPI

from proyecto_final_integrador.api.routers import auth, orders

app = FastAPI(
    title="Orders API",
    version="1.0.0",
    description="API para la gestión de órdenes.",
)

app.include_router(auth.router)
app.include_router(orders.router)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
