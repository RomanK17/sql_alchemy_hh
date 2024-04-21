from sqlalchemy import Integer, and_, func, insert, select, text, update
from sqlalchemy.orm import aliased
from src.models import metadata_obj, workers_table

from database import engine


def get_123_sync():
    with engine.connect() as conn:
        res = conn.execute(text("SELECT 1,2,3 union select 4,5,6"))
        print(f"{res.first()=}")


def create_table(metadata: metadata_obj):
    metadata.drop_all(engine) # удаляем таблицы
    metadata.create_all(engine)


def insert_data():
    with engine.connect() as conn:
        # statement = """
        # INSERT INTO workers (username) VALUES ('ИВАНГАЙ'), ('Вишневая девятка')"""
        statement = insert(workers_table).values([
            {"username" : "ИВАНГАЙ"}, {"username" : "Вишневая девятка"}
        ])
        # conn.execute(text(statement))
        conn.commit()

# def insert_data(metadata: metadata_obj):