import State, Msg, WEBSOCKET_URL
from abc import ABC, abstractmethod
import websocket
import json

class CryptoDockStrategy(ABC) :

    def __init__(self, TRADING_SOCKET_HOST, TRADING_SOCKET_PORT) :
        websocket.enableTrace(True)

        self.ws = websocket.WebSocketApp(
            WEBSOCKET_URL(TRADING_SOCKET_HOST, TRADING_SOCKET_PORT),
            on_message=self.ws_on_message,
            on_error=self.ws_on_error,
            on_close=self.ws_on_close
        )
        self.ws.on_open = self.ws_on_open
        self.granularity = 60
        self.results = {
            'status': State.LATENT,
            'meta': {},
            'sequence': []
        }

    @abstractmethod
    def next(self) :
        pass

    def listen(self) :
        self.results['status'] = State.ACTIVE
        self.ws.run_forever()

    def destroy(self) :
        self.ws.close()
        self.ws = None

    def ws_on_open(self, ws) :
        self.ws.send(json.dumps({'command': Msg.START, 'granularity': self.granularity}))

    def ws_on_message(self, ws, message) :
        if message == Msg.POLL :
            self.on_poll()
        elif message == Msg.PAUSE :
            self.on_pause()
        elif message == Msg.RESTART :
            self.listen()
        elif message == Msg.FINISH :
            self.on_finish()
        elif message == Msg.RESOLVED :
            self.destroy()
        else :
            if self.results['status'] == State.ACTIVE :
                self.next()
            else :
                self.handle_non_active_state()

    def ws_on_error(self, ws, error) :
        pass

    def ws_on_close(self, ws) :
        pass

    def on_poll(self) :
        self.ws.send(json.dumps({'command': State.ACTIVE, 'results': self.results}))

    def on_pause(self) :
        self.ws.close()

    def on_finish(self) :
        self.ws.send(json.dumps({'command': State.FINISHED, 'results': self.results}))
        self.results['status'] = State.LATENT

    def handle_non_active_state(self) :
        print('NON ACTIVE STATE: ', self.results)
        self.ws.send(json.dumps({'command': State.LATENT, 'results': self.results}))
