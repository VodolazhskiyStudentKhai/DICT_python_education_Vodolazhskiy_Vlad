import json

import requests as requests


class CurrencyExchange:
    exchanges = {}
    __json_file = None

    def convert_exchange(self):
        main_curr = None

        while self.__json_file is None:
            main_curr = input().strip().lower()

            try:
                self.__json_file = json.loads(requests.get(f"http://www.floatrates.com/daily/{main_curr}.json").text)
            except json.decoder.JSONDecodeError:
                self.__json_file = None
                print("Input another currency")
                continue

        currency = None

        while currency is None:
            currency = input().strip().upper()
            try:
                self.__json_file[currency.lower()]["rate"]
            except KeyError:
                currency = None
                print("Input another currency")
                continue

        value = float(input())

        summ = value if main_curr.upper() == currency else CurrencyExchange.calculate(value, self.get_rate(currency))
        print(f"You received {summ} {currency}")

    def get_rate(self, exc_name: str):
        if len(self.exchanges) == 0:
            self.add_currency("USD")
            self.add_currency("EUR")

        print("Checking the cache...")

        if exc_name in self.exchanges.keys():
            print("It is in the cache!")
            return self.exchanges[exc_name]

        print("Sorry, but it is not in the cache!")
        return self.add_currency(exc_name)

    def add_currency(self, curr_name: str):
        rate = self.__json_file[curr_name.lower()]["rate"]
        self.exchanges[curr_name] = rate
        return rate

    @staticmethod
    def calculate(value: float, rate: float):
        return round(value*rate, 2)


ce = CurrencyExchange()
ce.convert_exchange()
