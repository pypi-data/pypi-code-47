class Hello:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    __repl__ = __str__

    def print(self):
        print(self.message)

if __name__ == "__main__":
    hello = Hello("Hello, world")
    hello.print()
