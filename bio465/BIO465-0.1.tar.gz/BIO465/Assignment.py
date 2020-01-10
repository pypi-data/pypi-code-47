from abc import ABC, abstractmethod


class Assignment:
    """
    The Assignment class is a wrapper for labs and homework, it is to give them their attributes
    and given them common methods
    """
    def __init__(self, title: str, body: str, instructions: str, number: int):
        self.title = title
        self.body = body
        self.instructions = instructions
        self.number = number

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_instructions(self):
        pass

    @abstractmethod
    def get_number(self):
        pass
