from roc.channel import Channel


class ChannelManager:
    def __init__(self):
        self.channels = {}

    def get(self, key: int, initialize: bool = False) -> None | Channel:
        if key in self.channels:
            return self.channels[key]

        if initialize:
            self.channels[key] = self.make()
            return self.channels[key]

        return None

    def make(self) -> Channel:
        return Channel()

    def close(self, key: int) -> bool:
        chan = self.get(key)
        if chan is None:
            return True

        return chan.close()

    def flush(self):
        for key in self.channels:
            self.close(key)
