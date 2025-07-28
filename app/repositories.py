from typing import Annotated, List

from fastapi import Depends
from sqlalchemy.orm import Session

from .database import get_session
from .models import Wallet
from .schemas import Address


class WalletRepository:
    def __init__(self, session):
        self.session = session

    def create_wallet(self,
                      address: Annotated[Address, Address(address="")]):
        wallet = Wallet(address=address.address)
        self.session.add(wallet)
        self.session.commit()

    def get_wallets(
            self,
            offset: Annotated[int, 0],
            limit: Annotated[int, 100]) -> List[Wallet]:
        return self.session.query(Wallet).offset(offset).limit(limit).all()


def get_wallet_repository(session: Annotated[Session, Depends(get_session)]) -> WalletRepository:
    return WalletRepository(session)
