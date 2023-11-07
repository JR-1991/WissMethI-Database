import sqlalchemy as sa

from sqlalchemy.ext.automap import automap_base


def connect(
    username: str,
    password: str,
    host: str,
    port: int,
    db_name: str,
    **kwargs,
):
    """
    Creates a SQLAlchemy engine object for a MySQL database.

    Args:
        username (str): The username to connect to the database.
        password (str): The password to connect to the database.
        host (str): The host address of the database.
        port (int): The port number of the database.
        db_name (str): The name of the database.

    Returns:
        sqlalchemy.engine.base.Engine: The SQLAlchemy engine object for the MySQL database.
    """
    return sa.create_engine(
        f"mysql+pymysql://{username}:{password}@{host}:{port}/{db_name}"
    )


def reflect_schema(engine):
    """
    Automaps classes from the database using SQLAlchemy's automap_base function.

    Args:
        engine: SQLAlchemy engine object.

    Returns:
        Base: SQLAlchemy automap_base object.
    """
    Base = automap_base()
    Base.prepare(autoload_with=engine)
    return Base
