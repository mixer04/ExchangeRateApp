import requests

with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

def test_api_key():
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def get_exchange_rate(base_currency, target_currency, amount):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}/{amount}'
    response = requests.get(url)
    data = response.json()
    is_success = data['result']
    if is_success == 'success':
        result = data['conversion_result']
        print(f"Today, {amount} {base_currency} is equal to {result:.2f} {target_currency}.")
    elif is_success == 'error':
        print("Error:" + data['error-type'])
    else:
        print("Unknown error occurred.")
        exit(1)

def main():
    if not test_api_key():
        print('API is not working. Try again or change your API key.')
    else:
        print("Welcome to the ExchangeRateApp")
        base_currency = input("Enter the base currency (USD, EUR, GBP, etc.): ")
        target_currency = input("Enter the target currency: ")
        amount = float(input("Enter the amount to convert: "))
        get_exchange_rate(base_currency, target_currency, amount)

if __name__ == '__main__':
    main()