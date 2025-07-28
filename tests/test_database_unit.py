from app.schemas import Address


class TestDatabaseUnit:
    def test_create_wallet_success(self, wallet_repository):
        test_address = "TJRabPrwbZy45sbavfcjinPJC18kjpRTv8"
        address_data = Address(address=test_address)

        wallet_repository.create_wallet(address_data)

        wallets = wallet_repository.get_wallets(offset=0, limit=10)

        assert len(wallets) == 1
