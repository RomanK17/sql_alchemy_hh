from sqlalchemy import Table, Integer, String, Column, MetaData

metadata_obj = MetaData()

workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column("username", String)

)
