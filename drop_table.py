def drop_table(session):
    from model import Base
    Base.metadata.drop_all(session.connection())

if __name__ == "main":
    from model import session
    drop_table(session)

