from pweb_orm import PwebModel, pweb_orm


class Person(PwebModel):
    firstName = pweb_orm.Column("first_name", pweb_orm.String(150), nullable=False)
    lastName = pweb_orm.Column("last_name", pweb_orm.String(150),)
    email = pweb_orm.Column("email", pweb_orm.String(150), nullable=False)
    password = pweb_orm.Column("password", pweb_orm.String(250), nullable=False)
    address = pweb_orm.Column("address", pweb_orm.Text())