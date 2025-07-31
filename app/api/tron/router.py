from typing import Annotated, List

from fastapi import APIRouter, HTTPException, Depends
from tronpy import Tron
from tronpy.exceptions import AddressNotFound, BadAddress
from tronpy.providers import HTTPProvider

from app.repositories import WalletRepository, get_wallet_repository
from app.schemas import Address, AccountData, ExceptionMessage, WalletsResponse

from app.settings import settings

provider = HTTPProvider(api_key=settings.API_KEY)

client = Tron(provider=provider, network="shasta")

router = APIRouter(prefix="/tron")


@router.get("/")
def read_wallets(
        offset: Annotated[int, 0],
        limit: Annotated[int, 100],
        wallet_repository: Annotated[WalletRepository, Depends(get_wallet_repository)]) -> List[WalletsResponse]:
    wallets = wallet_repository.get_wallets(offset=offset, limit=limit)
    response = [
        WalletsResponse(id=wallet.id, address=wallet.address) for wallet in wallets
    ]
    return response


@router.post("/info",
             responses={
                 400: {"model": ExceptionMessage},
                 404: {"model": ExceptionMessage},
                 200: {"model": AccountData},
             })
def info_by_address(
        data: Annotated[Address, Address(address="")],
        wallet_repository: Annotated[WalletRepository, Depends(get_wallet_repository)]) -> AccountData:
    try:
        response = AccountData(
            balance=client.get_account_balance(data.address),
            bandwidth=client.get_bandwidth(data.address),
            energy=client.get_energy(data.address),
        )
        wallet_repository.create_wallet(data)

    except AddressNotFound:
        raise HTTPException(
            status_code=404,
            detail="Address not found"
        )

    except BadAddress:
        raise HTTPException(
            status_code=400,
            detail="Bad address"
        )

    return response
