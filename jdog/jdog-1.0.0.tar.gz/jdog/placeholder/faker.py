from jdog.placeholder.placeholder import Placeholder


class FakerPlaceholder(Placeholder):
    """
        Placeholder for faker user

        :var faker.Faker faker: Faker instance
    """
    def __init__(self, full_name, arguments, faker):
        super().__init__(full_name, arguments)
        self.faker = faker
