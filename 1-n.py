from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, Mapped, mapped_column

import config


engine = create_engine(config.POSTGRES_1N)

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
session = Session()

class Person(Base):
    __tablename__ = "people"
    
    id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )
    
    things: Mapped[list["Thing"]] = relationship(
        "Thing", back_populates='person'
    )
    
class Thing(Base):
    __tablename__ = "things"
    
    id: Mapped[int] = mapped_column(
        primary_key=True, index=True
    )
    name: Mapped[str] = mapped_column(
        nullable=False
    )
    person_id: Mapped[int] = mapped_column(
        ForeignKey("people.id")
    )
    
    person: Mapped["Person"] = relationship(
        "Person", back_populates='things'
    )

Base.metadata.create_all(engine)


# Insert

amir = Person(name="Amirhossein")

macbook = Thing(name="MacBook", person=amir)
iphone = Thing(name="iPhone", person=amir)

session.add(amir)
session.commit()

sina = Person(name="Sina")

home = Thing(name="Home")
car = Thing(name="Car")

sina.things.append(home)
sina.things.append(car)

session.add(sina)
session.commit()

# Select

people = session.query(Person).all()

for prsn in people:
    print(f"Name: {prsn.name}")
    for thng in prsn.things:
        print(f"Thing name: {thng.name}")   
        
    print("")
    
print("")
    
thngs = session.query(Thing).all()

for thng in thngs:
    print(f"Thing name: {thng.name} | Owner: {thng.person.name}")