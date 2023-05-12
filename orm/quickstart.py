from typing import List, Optional
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, select
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    # links User to Address
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "Address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column((ForeignKey("User.id")))

    # links Address to User
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address},user={self.user})"


# echo parameter is for logging SQL emitted by connections
engine = create_engine("sqlite:///q.db", echo=True)

# create tables
Base.metadata.create_all(engine)

# insert data
# with Session(engine) as session:
#     gilbert = User(name="Gilbert", fullname="Ssenyonjo Gilbert")
#     gilbert.addresses = [Address(email_address="gssenyonjo@gmail.com"), Address(email_address="ssg@hrpsolutions.com")]
#
#     joan = User(
#         name="Joan",
#         fullname="Joan of Arc",
#         addresses=[
#             Address(email_address="joan@fate.org")
#         ]
#     )
#     martha = User(name="Martha")
#     session.add_all([gilbert, joan, martha])
#     session.commit()


# read and update data from db
# with Session(engine) as session:
#     stmt = select(User).where(User.name.is_("Gilbert"))
#     for user in session.scalars(stmt):
#         print(user)
#
#     print("getting address for Joan")
#     stmt = select(Address).join(Address.user).where(User.name=="Joan")
#     joan_address = session.scalars(stmt).one()
#     print(joan_address)
#     print(joan_address.user)
#
#     # update
#     joan_address.email_address = "joan@anime.net"
#     session.commit()


# delete data
with Session(engine) as session:
    user1 = session.get(User, 1)
    print(user1)
    session.delete(user1)
    session.commit()
