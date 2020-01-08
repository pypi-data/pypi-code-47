# -*- coding:utf-8 -*-

from itertools import permutations

from faker import Faker
from faker.providers import BaseProvider


class _Provider(BaseProvider):
    prefix_dot = ["{{first_name}}", "{{last_name}}"]
    prefix_no_dot = prefix_dot + ["{{random_letter}}"]
    prefixes = [".".join(perm) for perm in permutations(prefix_dot)]
    prefixes += ["".join(perm) for perm in permutations(prefix_no_dot, 2)]
    suffixes = ["", "{{year}}", "#", "##", "###", "####", "#####"]
    username_formats = []
    for prefix in prefixes:
        for suffixes in suffixes:
            username_formats.append(prefix + suffixes)

    safe_email_tlds = ("org", "com", "net")

    def domain(self) -> str:
        return f"example.{self.random_element(self.safe_email_tlds)}"

    def username(self) -> str:
        pattern = self.random_element(self.username_formats)
        username = self.numerify(self.generator.parse(pattern)).lower()
        return username


fake = Faker()
fake.add_provider(_Provider)


def domain() -> str:
    return fake.domain()


def username() -> str:
    return fake.username()
