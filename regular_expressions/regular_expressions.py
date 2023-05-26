class RegularExpressions:
    __ignore_meta = []

    @staticmethod
    def start():
        inp = '|'
        while '|' in inp:
            RegularExpressions.__ignore_meta.clear()
            inp = input()
            str_list = inp.split('|')
            transform_str = RegularExpressions.gen_ignore_meta(str_list[0])
            result = RegularExpressions.check_start_end(transform_str, str_list[1])

            print(f"Input: '{inp}'  Output: {result}")

    @staticmethod
    def compare_strings(str1: str, str2: str, i1: int = 0, i2: int = 0, result: bool = False, one: bool = False):
        meta_list = RegularExpressions.__ignore_meta

        if i1 == len(str1) or i2 == len(str2):
            return result

        result = RegularExpressions.compare(str1[i1], str2[i2], i1)

        if len(str1) > i1+1 and str1[i1+1] == '?' and i1+1 not in meta_list:
            return RegularExpressions.compare_strings(str1[:i1+1] + str1[i1+2:], str2, i1, i2, result, one) if result \
                else RegularExpressions.compare_strings(str1[:i1] + str1[i1 + 2:], str2, i1, i2, result, one)

        if len(str1) > i1+1 and str1[i1+1] == '*' and i1+1 not in meta_list:
            return RegularExpressions.compare_strings(str1, str2, i1, i2 + 1, result, one) if result \
                else RegularExpressions.compare_strings(str1[:i1] + str1[i1 + 2:], str2, i1, i2, result, one)

        if len(str1) > i1+1 and str1[i1+1] == '+' and i1+1 not in meta_list:
            if result:
                return RegularExpressions.compare_strings(str1, str2, i1, i2 + 1, result, one)
            elif i2-i1 >= 1:
                return RegularExpressions.compare_strings(str1[:i1] + str1[i1 + 2:], str2, i1, i2, result, one)
            else:
                return False

        if result:
            return RegularExpressions.compare_strings(str1, str2, i1 + 1, i2 + 1, result, one)
        elif one:
            return False
        else:
            return RegularExpressions.compare_strings(str1, str2, 0, i2-i1+1, result, one)

    @staticmethod
    def check_start_end(str1: str, str2: str):
        meta_list = RegularExpressions.__ignore_meta
        operation = 0
        if str1[0] == '^' and 0 not in meta_list:
            operation += 1
            str1 = str1[1:]

        if str1[-1] == '$' and len(str1) - 1 not in meta_list:
            operation += 2
            str1 = str1[:-1]

        match operation:
            case 0: return RegularExpressions.compare_strings(str1, str2)
            case 1: return RegularExpressions.compare_strings(str1, str2, 0, 0, False, True)
            case 2: return RegularExpressions.compare_strings(str1[::-1], str2[::-1], 0, 0, False, True)
            case 3:
                return RegularExpressions.compare_strings(str1, str2, 0, 0, False, True)\
                       and RegularExpressions.compare_strings(str1[::-1], str2[::-1], 0, 0, False, True)

    @staticmethod
    def gen_ignore_meta(str1: str):
        result = ""
        meta_list = RegularExpressions.__ignore_meta
        for i in range(len(str1)):
            if str1[i] == '\\' and i-len(meta_list) not in meta_list:
                RegularExpressions.__ignore_meta.append(i - len(meta_list))
            else:
                result += str1[i]
        return result

    @staticmethod
    def compare(symbol1: str, symbol2: str, i1: int = 0):

        if symbol1 == symbol2 or (symbol1 == '.' and i1 not in RegularExpressions.__ignore_meta):
            return True
        elif len(symbol1) == 0 and len(symbol2) != 0:
            return True
        elif len(symbol1) == 0 and len(symbol2) == 0:
            return True
        elif symbol1 != '' and len(symbol2) == 0:
            return False
        return False


RegularExpressions.start()
