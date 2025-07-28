from unittest.mock import patch
from decimal import Decimal


class TestIntegration:
    @patch('app.api.tron.router.client')
    def test_post_info_by_address_success(self, mock_client, client):
        mock_client.get_account_balance.return_value = Decimal("100.0")
        mock_client.get_bandwidth.return_value = 1000
        mock_client.get_energy.return_value = 500

        test_address = "TJRabPrwbZy45sbavfcjinPJC18kjpRTv8"
        test_data = {"address": test_address}

        response = client.post("/api/tron/info", json=test_data)

        assert response.status_code == 200

        response_data = response.json()
        assert "balance" in response_data
        assert "energy" in response_data
        assert "bandwidth" in response_data
        assert response_data["balance"] == "100.0"
        assert response_data["energy"] == 500
        assert response_data["bandwidth"] == 1000

    @patch('app.api.tron.router.client')
    def test_post_info_by_address_not_found(self, mock_client, client):
        from tronpy.exceptions import AddressNotFound
        mock_client.get_account_balance.side_effect = AddressNotFound("Address not found")

        test_data = {"address": "TJRabPrwbZy45sbavfcjinPJC18kjpRTv9"}

        response = client.post("/api/tron/info", json=test_data)

        assert response.status_code == 404
        assert response.json()["detail"] == "Address not found"

    @patch('app.api.tron.router.client')
    def test_post_info_by_address_bad_address(self, mock_client, client):
        from tronpy.exceptions import BadAddress
        mock_client.get_account_balance.side_effect = BadAddress("Bad address")

        test_data = {"address": "invalid_address"}

        response = client.post("/api/tron/info", json=test_data)

        assert response.status_code == 400
        assert response.json()["detail"] == "Bad address"
