import os
import pandas as pd

from utils import connect, reflect_schema
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

while True:
    try:
        engine = connect(
            username="root",
            password=os.environ["MYSQL_ROOT_PASSWORD"],
            db_name=os.environ["MYSQL_DATABASE"],
            host=os.environ["MYSQL_HOST"],
            port=3306,
        )

        with Session(engine) as sess:
            # Revoke all privileges from the user
            sess.execute(
                text(f"REVOKE ALL PRIVILEGES, GRANT OPTION FROM '{os.environ['MYSQL_USER']}'@'%';")
            )
            
            # Grant only SELECT privilege to the user
            sess.execute(
                text(f"GRANT SELECT ON `{os.environ['MYSQL_DATABASE']}`.* TO '{os.environ['MYSQL_USER']}'@'%';")
            )
        
        orm = reflect_schema(engine)
        break
    except OperationalError:
        print("🔌 Connecting to database (retrying)")
        pass

with Session(engine) as sess:
    # Add mixture row
    mixture_name = "ethylene glycol-water"
    mixture = orm.classes.mixtures(name=mixture_name)
    sess.add(mixture)

    # Retrieve ID for density and viscosity
    mixture_id = sess.query(orm.classes.mixtures).first().id # type: ignore

    # Add viscosity rows
    viscosities = pd.read_csv("./viscosity.tsv", sep="\t").to_dict("records")

    for viscosity in viscosities:
        if viscosity["mol_fraction_water"] > 1:
            continue

        sess.add(orm.classes.viscosity(mixture_id=mixture_id, **viscosity))

    # Add density rows
    densities = pd.read_csv("./density.tsv", sep="\t").to_dict("records")

    for density in densities:
        if density["mol_fraction_water"] > 1:
            continue

        sess.add(orm.classes.density(mixture_id=mixture_id, **density))

    sess.commit()