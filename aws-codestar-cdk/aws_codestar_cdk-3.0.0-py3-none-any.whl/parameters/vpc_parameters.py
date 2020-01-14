from typing import List


class VpcParameters:
    """
    Parameters class.
    """
    def __init__(self, subnet_ids: List[str], security_group_ids: List[str]):
        """
        Parameters for your lambda functions Virtual Private Network configuration.

        :param subnet_ids: List of subnets your function should be deployed to.
        These subnets need a NAT gateway in order for the function to to access the internet.
        :param security_group_ids: List of security group IDs for your function

        :return No return.
        """
        self.subnet_ids = VpcParameters.__list_to_comma_separated_list(subnet_ids)
        self.security_group_ids = VpcParameters.__list_to_comma_separated_list(security_group_ids)

    @staticmethod
    def __list_to_comma_separated_list(strings: List[str]) -> str:
        """
        Converts a list to a comma separated strings.

        :param strings: A list to modify.

        :return: A string containing list's elements.
        """
        return ', '.join(strings)
