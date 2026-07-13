# SQLAlchemy Relationships

This repository contains simple examples of the three most common SQLAlchemy ORM relationships.

## Covered Relationships

- **One-to-One (1:1)**
- **One-to-Many (1:N)**
- **Many-to-Many (N:N)**

Each example includes a small test demonstrating how to create objects, define relationships, and query related data.

## Pipenv

This project is using **Pipenv**. So, remember to install if you don't have. Or just read `Pipfile` and use your own
package manager.

```shell
pipenv shell
pipenv install
```

## Configuration

Before running the examples, open:

```text
settings/config.py
```

and replace the database connection string with your own PostgreSQL URL.

Example:

```python
POSTGRES_11 = "postgresql+psycopg2://username:password@host:port/sqlalchemy_11"  # 1:1
POSTGRES_1N = "postgresql+psycopg2://username:password@host:port/sqlalchemy_1n"  # 1:N
POSTGRES_NN = "postgresql+psycopg2://username:password@host:port/sqlalchemy_nn"  # N:N
```

## Run

Simply execute the example you want to test:

```bash
python 1-1.py
python 1-n.py
python n-n.py
```

Each script creates its tables (if they don't already exist), inserts sample data, and demonstrates the relationship in
action.

## Debug

If you want to see what will happen after running each file, change `create_engine(url)` to
`create_engine(url, echo=True)`. For example:

Change this:

```python
# Engine
engine = create_engine(config.POSTGRES_11)
```

to this:

```python
# Engine
engine = create_engine(config.POSTGRES_11, echo=True)
```

---

[Amirhossein Mohammadi](https://amirhossein.info)