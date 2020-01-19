import requests
from pprint import pprint
from .start_up import URLS, AUTH


async def check_response(resp, topic=None):
    status = resp.status_code
    if status != 200:
        print(f"{topic or ''}request not successful: {status} - {resp.reason}")
    return resp


async def get_contacts():
    resp = requests.get(URLS["CONTACTS"], headers=AUTH)
    if await check_response(resp, topic="get_contacts"):
        [contact_ids.add(  c["contactId"]) for c in resp.json()]
        [contact_names.add(c["author"]["name"])     for c in resp.json()]
        return resp.json()


async def show_contacts():
    """
    lists your contacts
    """
    contacts = await get_contacts()
    print(f"  > your {len(contacts)} contacts:")
    for contact in contacts:
        print(f"{contact['contactId']:4}: {contact['author']['name']}")
        # print(f"{contact['contactId']:4}, {contact['alias']}, {contact['author']['name']}")


async def get_contact_id_by_alias(alias):
    contacts = await get_contacts()
    for contact in contacts:
        if contact['author']['name'] == alias:
            return str(contact["contactId"])


async def show_contacts_full_info():
    pprint(get_contacts())


async def get_pending_contacts():
    resp = requests.get(URLS["CONTACTS_PENDING"], headers=AUTH)
    if await check_response(resp, topic="get_pending_contacts"):
        return resp.json()


async def show_pending_contacts():
    """
    lists your peding contacts
    """
    pending_contacts = await get_pending_contacts()
    if not pending_contacts:
        print("  > no pending_contacts")
        return
    print(f"  > your {len(pending_contacts)} pending contacts:")
    for contact in pending_contacts:
        #print(f"{contact['contactId']:4}: {contact['alias']}")
        pprint(contact)


async def add_contact(briar_link, alias):
    """
    add contact with briar_link and alias
    """
    add_contact = {
        "link": briar_link,
        "alias": alias
    }
    resp = requests.post(URLS["CONTACTS_PENDING"], headers=AUTH, json=add_contact)
    if await check_response(resp, topic=f"add_contact {alias} - {briar_link}"):
        return resp.json()


async def get_own_briar_link():
    resp = requests.get(URLS["ADD_LINK"], headers=AUTH)
    if await check_response(resp, topic="get_own_briar_link"):
        return resp.json()


async def show_own_briar_link():
    """
    displays your own briar link
    """
    link = await get_own_briar_link()
    print(f"  > your own briar link: \n    {link['link']}")


contacts       = {}
contact_ids   = set()
contact_names = set()
