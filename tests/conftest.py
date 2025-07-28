import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_session
from app.repositories import WalletRepository


@pytest.fixture
def test_db():
    """Создает тестовую базу данных в памяти"""
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    def override_get_session():
        with Session() as session:
            yield session

    app.dependency_overrides[get_session] = override_get_session
    
    yield engine
    
    Base.metadata.drop_all(bind=engine)
    app.dependency_overrides.clear()


@pytest.fixture
def client(test_db):
    """Создает тестовый клиент для API"""
    return TestClient(app)


@pytest.fixture
def wallet_repository(test_db):
    """Создает репозиторий для работы с кошельками"""
    engine = test_db
    Session = sessionmaker(bind=engine)
    session = Session()
    return WalletRepository(session)
