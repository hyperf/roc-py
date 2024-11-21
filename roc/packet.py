PING = 'ping'
PONG = 'pong'


class Packet:
    def __init__(self, id: int = 0, body: str = ""):
        self.id = id
        self.body = body

    def is_heartbeat(self):
        return self.id == 0 and (self.body == PING or self.body == PONG)

    def len(self):
        return len(self.body) + 4
