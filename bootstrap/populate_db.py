import os
import pandas as pd

from utils import connect, reflect_schema
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError

print("🔌 Connecting to database")
while True:
    try:
        engine = connect(
            username=os.environ["MYSQL_USER"],
            password=os.environ["MYSQL_PASSWORD"],
            db_name=os.environ["MYSQL_DATABASE"],
            host=os.environ["MYSQL_HOST"],
            port=3306,
        )

        orm = reflect_schema(engine)
        break
    except OperationalError as e:
        print(f"🔌 Connecting to database (retrying)")
        pass

print("🚀 Populating database with data from ./viscosity.tsv and ./density.tsv")

with Session(engine) as sess:
    # Add mixture row
    mixture_name = "ethylene glycol-water"
    mixture = orm.classes.mixtures(name=mixture_name)
    sess.add(mixture)

    # Retrieve ID for density and viscosity
    mixture_id = sess.query(orm.classes.mixtures).first().id

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

print("✅ Done!")
