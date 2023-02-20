import copy


class MatrixProcessing:
    @staticmethod
    def main_menu():
        close = False

        while not close:
            menu_str = "[Main menu]\n" \
                       "1. Add matrices\n" \
                       "2. Multiply matrix by a constant\n" \
                       "3. Multiply matrices\n" \
                       "4. Transpose matrices\n" \
                       "5. Calculate a determinant\n" \
                       "6. Inverse matrix\n" \
                       "0. Exit\n"
            print(menu_str)

            answer = int(input("Your choice: >").strip())
            match answer:
                case 0:
                    close = True
                case 1:
                    MatrixProcessing.add()
                case 2:
                    MatrixProcessing.multiply()
                case 3:
                    MatrixProcessing.multiply_m()
                case 4:
                    MatrixProcessing.transpose_menu()
                case 5:
                    MatrixProcessing.find_determinant()
                case 6:
                    MatrixProcessing.inverse_matrix()

    @staticmethod
    def add():
        a_matrix = Matrix("Enter size of matrix A: >").get_matrix()
        b_matrix = Matrix("Enter size of matrix B: >").get_matrix()
        result_matrix = []

        if len(a_matrix) != len(b_matrix) or len(a_matrix[0]) != len(b_matrix[0]):
            print("Error: matrix's must have equal size")
            return

        for i in range(len(a_matrix)):
            row1 = a_matrix[i]
            row2 = b_matrix[i]

            for j in range(len(row1)):
                row1[j] += row2[j]
                ...
            result_matrix.append(row1)

        print(f"Result matrix:\n" + Matrix.to_format_matrix(result_matrix))
        ...

    @staticmethod
    def multiply():
        matrix = Matrix("Enter size of matrix: >").get_matrix()
        const = int(input("Enter const: > "))
        result_matrix = []

        for i in range(len(matrix)):
            row = matrix[i]

            for j in range(len(row)):
                row[j] *= const
                ...
            result_matrix.append(row)

        print(f"Result matrix:\n" + Matrix.to_format_matrix(result_matrix))
    ...

    @staticmethod
    def multiply_m():
        a_matrix = Matrix("Enter size of matrix A: >").get_matrix()
        b_matrix = Matrix("Enter size of matrix B: >").get_matrix()
        result_matrix = []

        for i in range(len(a_matrix)):
            arr = [0] * len(b_matrix[0])
            result_matrix.append(arr)
            ...

        if len(a_matrix[0]) != len(b_matrix):
            print("Error: columns 1st matrix's must be equal rows 2nd matrix's")
            return

        for i in range(len(a_matrix)):
            for j in range(len(b_matrix[0])):
                for k in range(len(b_matrix)):
                    result_matrix[i][j] += a_matrix[i][k] * b_matrix[k][j]
                    ...
                ...
            ...

        print(f"Result matrix:\n" + Matrix.to_format_matrix(result_matrix))
        ...
    ...

    @staticmethod
    def transpose_menu():
        menu_str = "[Transpose menu]\n" \
                   "1. Main diagonal\n" \
                   "2. Side diagonal\n" \
                   "3. Vertical line\n" \
                   "4. Horizontal line\n"
        print(menu_str)
        answer = int(input("Your choice: >"))
        match answer:
            case 1:
                MatrixProcessing.transpose_main_diagonal()
            case 2:
                MatrixProcessing.transpose_side_diagonal()
            case 3:
                MatrixProcessing.transpose_vertical()
            case 4:
                MatrixProcessing.transpose_horizontal()

    @staticmethod
    def transpose_main_diagonal():
        matrix = Matrix("Enter size of matrix: >").get_matrix()

        result_matrix = copy.deepcopy(matrix)

        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[i])):
                result_matrix[i][j] = matrix[j][i]
                ...
            ...
        print(f"Result matrix:\n" + Matrix.to_format_matrix(result_matrix))
        ...

    @staticmethod
    def transpose_side_diagonal():
        matrix = Matrix("Enter size of matrix: >").get_matrix()

        result_matrix = copy.deepcopy(matrix)

        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[i])):
                result_matrix[i][j] = matrix[-1-j][-1-i]
                ...
            ...
        print(f"Result matrix:\n" + Matrix.to_format_matrix(result_matrix))
        ...

    @staticmethod
    def transpose_vertical():
        matrix = Matrix("Enter size of matrix: >").get_matrix()

        result_matrix = copy.deepcopy(matrix)

        for i in range(len(result_matrix)):
            result_matrix[i].reverse()
            ...
        print(f"Result matrix:\n" + Matrix.to_format_matrix(result_matrix))
        ...
    ...

    @staticmethod
    def transpose_horizontal():
        matrix = Matrix("Enter size of matrix: >").get_matrix()

        result_matrix = copy.deepcopy(matrix)

        for i in range(len(result_matrix)):
            for j in range(len(result_matrix[i])):
                result_matrix[i][j] = matrix[-1-i][j]
                ...
            ...
        print(f"Result matrix:\n" + Matrix.to_format_matrix(result_matrix))
        ...

    @staticmethod
    def find_determinant():
        matrix = Matrix("Enter size of matrix: >").get_matrix()
        result = MatrixProcessing.__get_determinant(matrix)
        print(f"The result is:\n{result}")
        return result

    @staticmethod
    def inverse_matrix():
        matrix = Matrix("Enter size of matrix: >").get_matrix()

        if MatrixProcessing.__get_determinant(matrix) == 0:
            print("This matrix doesn't have an inverse.")
            return

        result_matrix = MatrixProcessing.__get_second_matrix(matrix)

        for f in range(len(matrix)):
            scaler1 = 1.0 / matrix[f][f]

            for j in range(len(matrix)):
                matrix[f][j] *= scaler1
                result_matrix[f][j] *= scaler1

            for i in list(range(len(matrix)))[0:f] + list(range(len(matrix)))[f + 1:]:
                scaler2 = matrix[i][f]
                for j in range(len(matrix)):
                    matrix[i][j] = matrix[i][j] - scaler2 * matrix[f][j]
                    result_matrix[i][j] = result_matrix[i][j] - scaler2 * result_matrix[f][j]
                    ...
                ...
            ...
        print(f"Result matrix:\n" + Matrix.to_format_matrix(result_matrix))
        return result_matrix

    @staticmethod
    def __get_determinant(matrix: list):

        if len(matrix) != len(matrix[0]):
            print("Matrix must be NxN format")
            return

        if len(matrix) == 1:
            return matrix[0][0]

        elif len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        else:
            result = 0
            for i in range(len(matrix)):
                rex = matrix[0][i] * MatrixProcessing.__get_determinant(
                    [[el for ind, el in enumerate(matx) if ind != i] for matx in matrix[1:]])
                result += rex if i % 2 == 0 else -rex
                ...

            return result

    @staticmethod
    def __get_second_matrix(matrix: list):
        size = len(matrix)
        return [[1 if i == j else 0 for i in range(size)] for j in range(size)]
    ...


class Matrix:
    __matrix = []

    def __init__(self, message: str):
        matrix = []
        while len(matrix) == 0:
            size = input(message).strip().split()

            if len(size) != 2:
                print("Enter matrix in format: 'n m'\n where 'n' - column, 'm' - row\n Try again!")
                continue

            size = list(map(int, size))

            for i in range(size[0]):
                inp = input("Enter matrix: >").strip().split()
                m = size[1]

                if len(inp) != m:
                    print(f"Row must be {m} length")
                    break

                int_inp = list(map(int, inp))
                matrix.append(int_inp)
                ...
            ...
        self.__matrix = matrix

    def __str__(self):
        return Matrix.to_format_matrix(self.__matrix)

    def get_matrix(self):
        return self.__matrix

    @staticmethod
    def to_format_matrix(matrix: list):
        str_matrix = ""

        if type(matrix[0][0]) == float:
            for v in range(len(matrix)):
                for k in range(len(matrix)):
                    matrix[v][k] = round(matrix[v][k], 2)
                    ...
                str_matrix += "{0}\n".format(matrix[v])
                ...
            ...
        else:
            for i in range(len(matrix)):
                str_matrix += "{0}\n".format(matrix[i])
                ...
        return str_matrix.replace("[", "").replace("]", "").replace(",", "")


MatrixProcessing.main_menu()
