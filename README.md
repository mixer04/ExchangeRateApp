# ExchangeRateApp

This is a simple Python application that uses the ExchangeRate-API to fetch real-time exchange rates.

## Installation

Install the `requests` library by running the following command:

```bash
pip install requests
```

## Usage

In a  file named `api_key.txt` in the same directory as your Python script, add your ExchangeRate-API key.

Now, you can run the application using the following command:

```bash
python exchange.py
```

The application will prompt you to enter the base currency, target currency, and the amount to convert. It will then display the exchange rate for the given amount.

## API Key

To use the ExchangeRate-API, you need to sign up for a free account at https://www.exchangerate-api.com/. Once you have signed up, you will receive an API key.

## Error Handling

The application includes basic error handling for invalid API keys and network issues. If the API is not working or the API key is invalid, the application will display an appropriate error message.
