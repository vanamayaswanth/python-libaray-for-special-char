class SpecialChar:
    def __init__(self):
        self.char = ""
        self.name = ""
        self.specialCharDict = {
            "!": "exclamation mark",
            "@": "at sign",
            "#": "Hash-Tag",
            "$": "dollar sign",
            "%": "percent sign",
            "^": "caret",
            "&": "ampersand",
            "*": "asterisk",
            "(": "left parenthesis",
            ")": "right parenthesis",
            "-": "hyphen",
            "_": "underscore",
            "+": "plus sign",
            "=": "equals sign",
            "{": "left curly brace",
            "}": "right curly brace",
            "[": "left square bracket",
            "]": "right square bracket",
            "|": "vertical bar",
            "\\": "backslash",
            ":": "colon",
            ";": "semicolon",
            "'": "single quote",
            '"': "double quote",
            ",": "comma",
            ".": "period",
            "<": "less than",
            ">": "greater than",
            "?": "question mark",
            "/": "forward slash",
        }

    def main(self):
        print("Enter a special character")
        self.char = input()
        self.name = self.specialCharDict[self.char]
        print("The name of the character is", self.name)

if __name__ == "__main__":
    specialChar = SpecialChar()
    specialChar.main()
