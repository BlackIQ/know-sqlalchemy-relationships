# SQLAlchemy & SQLAlchemy ORM
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, Mapped, mapped_column

# Settings
from settings import config

# Engine
engine = create_engine(config.POSTGRES_11)


# Base Model
class Base(DeclarativeBase):
    pass


# Session & Session Maker
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = Session()


# Table: Person
class Person(Base):
    __tablename__ = "people"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )

    passport: Mapped["Passport"] = relationship(
        "Passport", back_populates="person", uselist=False
    )


# Table: Passport
class Passport(Base):
    __tablename__ = "passports"

    id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    number: Mapped[str] = mapped_column(
        unique=True, nullable=False
    )
    person_id: Mapped[int] = mapped_column(
        ForeignKey("people.id"), nullable=False, unique=True
    )

    person: Mapped["Person"] = relationship(
        "Person", back_populates="passport"
    )


# Create tables
Base.metadata.create_all(engine)

# ---------- INSERT ---------- #

amir = Person(name="Amirhossein")
passport_amir = Passport(number="ABC4859", person=amir)

session.add(amir)
session.commit()

sina_passport = Passport(number="XYZ1524")
sina = Person(name="Sina", passport=sina_passport)

session.add(sina_passport)
session.commit()

# ---------- SELECT ---------- #

people = session.query(Person).all()

for prsn in people:
    print(f"Name: {prsn.name} | Passport Number: {prsn.passport.number}")

print("------------------------------------------------------")

passports = session.query(Passport).all()

for psprt in passports:
    print(f"Password Number: {psprt.number} | Owner: {psprt.person.name}")
