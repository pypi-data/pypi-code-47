from dataclasses import dataclass


@dataclass
class CustomerRefField:
    '''
    :param customer_ref: Optional parameter allowing the client
    to pass a unique string (up to 32 chars) that is
     used to de-dupe mistaken re-submissions.
     CustomerRef can contain: upper/lower chars, digits,
      chars : - . _ + * : ; ~ only.
      Please note: There is a time window associated
      with the de-duplication of duplicate
      submissions which is 60 seconds.

    '''
    customer_ref: str = None
