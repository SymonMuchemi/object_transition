from sqlalchemy import inspect
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///users.db", echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()  # create

# new_user = User(name="John Doe", phone_number="1234567890")
# new_usr2 = User(name="Jane", phone_number="1234567890")
# peninah = User(name="Peninah", phone_number="1234567890")
bob = session.query(User).filter_by(name="Bob")



# session.add(bob)

# session.commit()
# change
bob.name = "Pen"

print(bob.name)

bob.name = "Collimore"

session.delete()

insp = inspect(bob)

print(insp.attrs.name.history)


if insp.deleted:
    print("John is deleted")
elif insp.detached:
    print("John is detached")
elif insp.pending:
    print("in pending state!")
elif insp.persistent:
    print("Persistent!")
elif insp.transient:
    print("in Transient state")
else:
    print("Not yet")



