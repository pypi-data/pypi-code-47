"""briar cli-messenger for briar:headless"""

import asyncio
import types
from . import connections as conn
from . import contacts as cont
from . import messages as msgs
from . import repl
from .repl import prompt_session as ps
from .repl import help, exit_repl
from .contacts import show_contacts, show_pending_contacts, show_own_briar_link, add_contact
from .blogs import show_blog_posts


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(conn.probe_headless())
    loop.run_until_complete(show_contacts())
    loop.run_until_complete(chose_action())
    loop.close()


async def chat_with(contact_id):
    """
    chats with specific contact in 1:1 chat
    """
    if not contact_id.isdigit():
        contact_id = await cont.get_contact_id_by_alias(contact_id)
    with repl.patch_stdout():
        await msgs.show_history(contact_id)
        background_task = asyncio.create_task(conn.connect_websocket())
        try:
            await send_msgs(contact_id)
        finally:
            background_task.cancel()
        print("leaving chat..")


async def send_msgs(contact_id):
    repl.selected = "send_msgs"
    completes = {"/back"}
    completes.update(cont.contact_names)
    while True:
        msg_text = await ps.prompt_async(
            "msg: ",
            style=repl.prompt_style_chat,
            completer=repl.repl_completer(list(completes)),
        )
        if msg_text == "/back":
            break
        elif msg_text.startswith("/"):
            command, *args = msg_text[1:].split()
            if command in repl.implemented:
                # print(f"this now runs command: {command} with args: {args}")
                perform = repl.implemented.get(command)
                await perform(*args)

            else:
                print("sorry could not find this command..")

        elif len(msg_text) > 0:
            await msgs.send(contact_id, msg_text)


async def chose_action():
    repl.selected = "chose_action"
    completes = set(repl.implemented.keys())
    completes.update(cont.contact_names)
    while True:
        action = await ps.prompt_async(
            "com: ", 
            completer=repl.repl_completer(list(completes)),
            style=repl.prompt_style_commands,
        )
        command, *args = action.split()
        if command in repl.implemented:
            # print(f"this now runs command: {command} with args: {args}")
            perform = repl.implemented.get(command)
            await perform(*args)
        else:
            print("sorry could not find this command..")


if __name__ == "__main__":
    repl.implemented = {key: val for key, val in globals().items()
                        if isinstance(val, types.FunctionType)
                        and key not in repl.hidden}
    # print(repl.implemented.keys())
    main()
