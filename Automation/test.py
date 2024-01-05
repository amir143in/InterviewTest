import requests
import pytest


def test_currency_exchange_rate():
    access_key = "fd6f6946921b0d034969b202"
    source_currency = "USD"
    target_currency = "EUR"
    specific_date = "2023-01-04"
    api_endpoint = "https://open.er-api.com/v6/latest"

    # Example of API
    url = f"{api_endpoint}?apikey={access_key}&symbols={source_currency},{target_currency}&base={source_currency}"
    response = requests.get(url)

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    data = response.json()
    assert "base_code" in data, "Missing 'base' in the response"
    assert "rates" in data, "Missing 'rates' in the response"

    assert target_currency in data["rates"], f"Target currency {target_currency} not found in the response"


if __name__ == "__main__":
    pytest.main([__file__])
