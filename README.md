# ExchangeRateApp

A simple Python application that uses the ExchangeRate-API to fetch real-time exchange rates.

## Installation

Install the required packages:

```bash
pip install requests
```

## Usage

First, sign up for a free API key from ExchangeRate-API (https://www.exchangerate-api.com/).

Paste your API key into it.

Now, you can run the app:

```bash
python exchange.py
```

The app will prompt you to enter the base currency, target currency, and the amount to convert. It will then display the exchange rate for the given amount.

## API Key

The API key is stored in a separate file (`api_key.txt`) to avoid exposing it in the code. This file should be in the root directory of the project.

Enjoy!
