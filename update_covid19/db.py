import psycopg2
from sqlalchemy import create_engine

engine = create_engine(
    'postgresql+psycopg2://postgres:password@localhost/postgres',
)


def save_db(data_frame, table_name, model):
    postgreSQLConnection = engine.connect()
    try:
        data_frame.to_sql(
            table_name, postgreSQLConnection, if_exists='append', dtype=model
        )

    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print(
            'PostgreSQL Table %s has been created successfully.'
            % postgreSQLTable
        )
    finally:
        postgreSQLConnection.close()
