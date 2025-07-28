from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.settings import settings

engine = create_engine(
    settings.get_postgres_url
)

Session = sessionmaker(bind=engine)
Base = declarative_base()


def create_db():
    Base.metadata.create_all(engine)


def get_session():
    with Session() as session:
        yield session
