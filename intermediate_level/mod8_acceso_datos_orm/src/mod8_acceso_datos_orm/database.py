from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


# sqlite en memoria y sesiones:
engine = create_engine(
    "sqlite+pysqlite:///:memory:",  # db en memoria (pysqlite)
    echo=True,
)

SessionLocal = sessionmaker(bind=engine)  # sesiones


Base.metadata.create_all(engine)
