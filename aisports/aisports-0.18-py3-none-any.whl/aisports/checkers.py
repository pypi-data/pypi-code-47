import requests
import websockets
import asyncio
import json
import os


class Actions:

    @staticmethod
    def move(initial_position, next_positions):

        return {
            "initial_position": initial_position,
            "next_positions": next_positions
        }


class Checkers:
    def __init__(self, api_key, strategy):
        self.api_url = os.environ["AISPORTS_BACKEND"] or "http://aisports.ai:3000"
        self.ws_url = os.environ["AISPORTS_BACKEND_SOCKET"] or "ws://aisports.ai:3000"
        self.game_id = None
        self.api_headers = {
            "X-Api-Key": api_key
        }
        self.strategy = strategy

    async def _listen(self):
        async with websockets.connect(self.ws_url) as websocket:
            await websocket.send(json.dumps({"event": "authenticate", "data": {"key": self.api_headers.get("X-Api-Key")}}))
            stop_socket = False

            while (not stop_socket):
                response = json.loads(await websocket.recv())
                print("[WEBSOCKET] " + str(response))
                event = response.get("event")

                if (event == "game_finished"):
                    print("Game finished, thank you")
                    stop_socket = True
                elif event == "new_game":
                    print("You found new game!")
                    self.game_id = response.get("data").get("gameId")
                    self.player = response.get("data").get("player")
                    self.state = response.get("data").get("state")
                elif event == "turn":
                    self._on_turn()

    def _get_game_information(self):
        return {
            "game_id": self.game_id,
            "player": self.player
        }

    def _get_state(self):
        return self.state

    def _on_turn(self):
        print("Your move")
        action = self.strategy(self._get_game_information(), self._get_state())
        print("You decided to", action)

        data = {
            "gameId": self.game_id,
            "from": {
                "x": action.get("initial_position")[0],
                "y": action.get("initial_position")[1]
            },
            "to": list(map(lambda position: {"x": position[0], "y": position[1]}, action.get("next_positions")))
        }

        result = requests.post(self.api_url + "/checkers/turn", json=data,
                               headers=self.api_headers)

        if (result.status_code != 200):
            print("[API ERROR]: " + str(result.content))
            result.raise_for_status()

    def start(self):
        print("Searching for opponent ...")
        asyncio.get_event_loop().run_until_complete(self._listen())
