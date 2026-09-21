# 1. pathlib + csv + json + logging
import csv
import json
import logging
from datetime import UTC, datetime
from pathlib import Path

# ---4. logging---
logging.basicConfig(
    level=logging.INFO,  # nivel1-INFO
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

# Paths
BASE_DIR = Path(__file__).resolve().parent  # path src/mod6_libreria_estandar_es/
DATA_FILE = (
    BASE_DIR / "data" / "orders.csv"
)  # src/mod6_libreria_estandar_es/data/orders.csv
OUTPUT_FILE = (
    BASE_DIR / "output" / "metrics.json"
)  # src/mod6_libreria_estandar_es/output/metrics.json

# --1. csv ingesta:--
try:
    with DATA_FILE.open("r", encoding="utf-8", newline="") as file:
        orders = list(csv.DictReader(file))

    logger.info("CSV leído correctamente: %s", DATA_FILE)

except FileNotFoundError:
    logger.error("No se encontró el archivo: %s", DATA_FILE)  # nive2-ERORR
    raise

# logging nivel3-WARNING
for order in orders:
    quantity = int(order["quantity"])

    if quantity > 4:
        logger.warning(
            "La orden %s tiene una cantidad alta: %s unidades",
            order["order_id"],
            quantity,
        )

# --2. metricas--
total_orders = len(orders)
total_units = sum(int(order["quantity"]) for order in orders)
total_value = sum(int(order["quantity"]) * float(order["price"]) for order in orders)

logger.info("Órdenes procesadas: %s", total_orders)
logger.info("Unidades totales: %s", total_units)
logger.info("Valor total: %.2f", total_value)

# --3. Exportacion de metricas a JSON:--
# date
generated_at = datetime.now(UTC).isoformat()

metrics = {
    "generated_at": generated_at,
    "total_orders": total_orders,
    "total_units": total_units,
    "total_value": total_value,
}

with OUTPUT_FILE.open("w", encoding="utf-8") as file:
    json.dump(metrics, file, indent=4)

logger.info("Métricas exportadas a %s", OUTPUT_FILE)  # metrics.json
