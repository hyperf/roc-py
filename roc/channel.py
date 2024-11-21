import asyncio


class Channel:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.is_closed = False
        self.is_popping = False

    # TODO: 增加超时
    async def pop(self) -> any:
        if self.is_closed:
            return False

        self.is_popping = True
        res = await self.queue.get()
        self.is_popping = False

        if res is None:
            self.is_closed = True
            return False

        return res

    async def push(self, data: any):
        if self.is_closed:
            return False

        await self.queue.put(data)

        return True

    def close(self):
        if self.is_closed:
            return False

        if self.is_popping:
            self.queue.put(None)

        return True
