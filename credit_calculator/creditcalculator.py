import math
import sys


class CreditCalculator:
    @staticmethod
    def get_annuity(lp: float, n: int, li: float, ap: float):
        i = CreditCalculator.__get_i(li)

        if n is None:
            n = CreditCalculator.get_number_of_months(lp, ap, i)
        elif lp is None:
            lp = CreditCalculator.get_loan_principal(ap, n, i)
        elif ap is None:
            ap = CreditCalculator.get_number_of_annuity(lp, n, i)
            ...
        CreditCalculator.__get_overpayment(lp, n, ap)
        ...

    @staticmethod
    def get_diff(lp: float, n: int, li: float):
        if lp is None or n is None or li is None:
            print("Incorrect parameters.")
        else:
            result = CreditCalculator.__get_d(lp, n, li)
            for i in range(n):
                print("Month {0}: payment is {1}".format(i+1, result[i]))
                ...
            print("Overpayment = {0}".format(math.ceil(sum(result) - lp)))

    @staticmethod
    def get_number_of_annuity(lp: float, n: float, i: float):
        result = math.ceil(lp * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
        print(f"Your annuity payment = {result}!")
        return result

    @staticmethod
    def get_loan_principal(ap: float, n: float, i: float):
        result = math.floor(ap / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
        print(f"Your loan principal = {result}!")
        return result

    @staticmethod
    def get_number_of_months(lp: float, mp: float, i: float):
        result = math.ceil(math.log(mp / (mp - i * lp), 1 + i))
        print(CreditCalculator.__get_months_mess(result))
        return result

    @staticmethod
    def __get_i(li: float):
        return li/(12*100.0)

    @staticmethod
    def __get_d(lp: float, n: int, li: float):
        i = CreditCalculator.__get_i(li)
        result = []
        for j in range(1, n+1):
            result.append(math.ceil(lp / n + (i * (lp - (lp * (j - 1)) / n))))
            ...
        return result

    @staticmethod
    def __get_overpayment(lp: float, n: int, ap: float):
        print("Overpayment = {0}".format(math.ceil((ap * n) - lp)))

    @staticmethod
    def __get_months_mess(months: int):
        message = "It will take "
        if months >= 12:
            y = int(months / 12)
            message += "{0} ".format(y) + ("years" if y > 1 else "year")
            ...
        m = months % 12
        if m != 0:
            message += " and {0} ".format(m) + ("months" if m > 1 else "month")
            ...
        message += " to repay this loan!"
        return message


class Parser:
    @staticmethod
    def main():
        args = Parser.parse_args(sys.argv)
        t = args.get("--type")
        match t:
            case "diff":
                lp = Parser.get_arg(args, "--principal", float)
                n = Parser.get_arg(args, "--periods", int)
                li = Parser.get_arg(args, "--interest", float)

                CreditCalculator.get_diff(lp, n, li)
                ...
            case "annuity":
                lp = Parser.get_arg(args, "--principal", float)
                n = Parser.get_arg(args, "--periods", int)
                li = Parser.get_arg(args, "--interest", float)
                ap = Parser.get_arg(args, "--payment", float)
                CreditCalculator.get_annuity(lp, n, li, ap)
            case _:
                print("Incorrect parameters.")

    @staticmethod
    def get_arg(args: dict, arg_name: str, t: type):
        a = args.get(arg_name)
        return t(a) if a is not None else None

    @staticmethod
    def parse_args(args: list):
        args_dict = {}

        for el in args:
            spl = el.split("=")
            if len(spl) == 2:
                args_dict[spl[0]] = spl[1]
            ...
        return args_dict


Parser.main()
