import asyncio
import json

import websockets

from pineapple_core.core.store import model_store, node_store


def _load_node_models():
    """
    Loading files containing nodes declaration
    """
    # noinspection PyUnresolvedReferences
    import pineapple_nodes.nodes  # noqa


async def server(websocket, path):
    while True:
        print("Listening..")
        command = json.loads(await websocket.recv())
        print(command)
        if command["type"] == "on_get_all_models":
            await websocket.send(
                json.dumps({"rid": command["rid"], "data": list(model_store.keys())})
            )
        elif command["type"] == "on_get_model":
            await websocket.send(
                json.dumps(
                    {
                        "rid": command["rid"],
                        "data": model_store[command["node_name"]].dump(False),
                    }
                )
            )
        elif command["type"] == "on_get_all_nodes":
            await websocket.send(
                json.dumps({"rid": command["rid"], "data": list(node_store.keys())})
            )
        elif command["type"] == "on_get_node":
            print("Trying to serialize", command["node_id"])
            print(node_store[command["node_id"]].dump())
            await websocket.send(
                json.dumps(
                    {
                        "rid": command["rid"],
                        "data": node_store[command["node_id"]].dump(True),
                    }
                )
            )

        """command = command.split(" ")
        print("Received :", command)
        if command[0] == "list":
            if command[1] == "passive":
                await websocket.send(json.dumps(list(models.keys())))
            elif command[1] == "active":
                await websocket.send(json.dumps(list(nodes.keys())))
        if command[0] == "node":
            if command[1] in models:
                await websocket.send(json.dumps(models[command[1]].dump(False)))
            elif command[1] in nodes:
                await websocket.send(json.dumps(nodes[command[1]].dump(True)))"""


def run():
    _load_node_models()
    print(model_store)
    start_server = websockets.serve(server, "127.0.0.1", 5678)

    print("SERVER START <=>")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
