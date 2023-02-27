class MarkdownEditor:
    __full_text = ""
    __FILE_NAME = "output.md"

    def main_menu(self):
        close = False

        while not close:
            query = input("Choose a formatter:>").lower().strip()
            match query:
                case "!done":
                    close = True
                    self.__write_file()
                case "!help":
                    print("Available formatters: plain bold italic header link inline-code\n"
                          "ordered-list unordered-list new-line\n"
                          "Special commands: !help !done\n")
                    ...
                case "header":
                    self.__set_header()
                case "link":
                    self.__set_link()
                case "plain":
                    self.__set_plain()
                case "new-line":
                    self.__set_new_line()
                case "bold":
                    self.__set_bold()
                case "italic":
                    self.__set_italic()
                case "unordered-list":
                    self.__set_unordered_list()
                case "ordered-list":
                    self.__set_ordered_list()
                case "inline-code":
                    self.__set_code()
                case _:
                    print("Unknown formatting type or command")

    def __set_header(self):
        count = int(input("Level>:"))
        max_level = 6
        min_level = 1

        while min_level > count or count > max_level:
            print("The level should be within the range of 1 to 6.")
            count = int(input("Level>:"))
            ...
        text = input("Text:>")
        self.__full_text += "{0} {1}\n".format("#" * count, text)
        print(self.__full_text)
        return self.__full_text

    def __set_plain(self):
        text = input("Text:>")
        self.__full_text += text
        print(self.__full_text)
        return self.__full_text

    def __set_bold(self):
        text = input("Bold text:>".strip())
        self.__full_text += f"**{text}**"
        print(self.__full_text)
        return self.__full_text

    def __set_italic(self):
        text = input("Italic text:>".strip())
        self.__full_text += f"*{text}*"
        print(self.__full_text)
        return self.__full_text

    def __set_code(self):
        text = input("Code in line:>")
        self.__full_text += f"`{text}`"
        print(self.__full_text)
        return self.__full_text

    def __set_link(self):
        label = input("Label:>")
        url = input("URL>:")
        self.__full_text += "[{0}]({1})".format(label, url)
        return self.__full_text

    def __set_new_line(self):
        self.__full_text += "\n"
        print(self.__full_text)
        return self.__full_text

    def __set_ordered_list(self):
        rows = self.__set_rows()

        for i in range(rows):
            n = i+1
            text = input("Row #{0}:>".format(n))
            self.__full_text += "\n{0}. {1}".format(n, text)

        print(self.__full_text)
        return self.__full_text

    def __set_unordered_list(self):
        rows = self.__set_rows()

        for i in range(rows):
            text = input("Row #{0}:>".format(i+1))
            self.__full_text += "\n* {0}".format(text)

        print(self.__full_text)
        return self.__full_text

    @staticmethod
    def __set_rows():
        rows = int(input("Number of rows: >"))

        while 0 > rows:
            print("The number of rows should be greater than zero.")
            rows = int(input("Number of rows: >"))
            ...
        return rows

    def __write_file(self):
        with open(self.__FILE_NAME, 'w', encoding="utf-8") as file:
            file.write(self.__full_text)
        ...


MarkdownEditor().main_menu()
