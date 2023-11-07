# WissMeth I: Database lecture

This repository contains all necessary scripts and data to spin up a MySQL database and populate it.

## Usage

Simply run the `docker compose up -d` to spin up the database and populate it with data. Please note, for this to work, you need to have docker installed on your system and a running docker engine.

## DataModel

```mermaid
classDiagram
    mixtures <-- viscosity
    mixtures <-- density

    class mixtures {
        +INT(PK) id 
        +VARCHAR(100) name
    }

    class viscosity {
        +INT(PK) id
        +DECIMAL(12,4) viscosity
        +DECIMAL(5,4) mole_fraction_water
        +DECIMAL(7,4) temperature
        +VARCHAR(1000) literature_doi
        +INT(FK) mixture_id
    }

    class density {
        +INT(PK) id
        +DECIMAL(12,4) density
        +DECIMAL(5,4) mole_fraction_water
        +DECIMAL(7,4) temperature
        +VARCHAR(1000) literature_doi
        +INT(FK) mixture_id
    }
```
