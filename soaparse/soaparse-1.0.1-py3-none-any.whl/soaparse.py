#!/usr/bin/env python3

class SOArecord:
    def __init__(self, nameserver, raw_email, parsed_email, date, ttl):
        self.nameserver = nameserver

        self.raw_email = raw_email
        self.parsed_email = parsed_email

        # date seems to be either YYYYmmddNN, or N days depending on server
        self.date = date

        self.ttl = ttl


# parse out data fields in SOA to object repr
def soa_parse(authority_data):
    soa_data = authority_data.split(" ")

    try:
        nameserver = soa_data[0][:-1]

        raw_email = soa_data[1][:-1]
        parsed_email = email_from_soa(raw_email)

        date = soa_data[2]

        ttl = soa_data[3]

        return SOArecord(nameserver, raw_email, parsed_email, date, ttl)

    except IndexError as e:
        print("error parsing SOA data field:\n" + repr(e))
        return None


# parse email address from DNS SoA data field
# assumes email hostname is root name, not a subdomain (most common case)
# may not be accurate if email hostname has multiple parts
def email_from_soa(soa_email_field):
    email_parts = soa_email_field.rsplit(".", maxsplit=2)
    email_name = email_parts[0]

    email = email_name + "@" + ".".join(email_parts[1:])
    return email
