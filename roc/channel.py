import asyncio


class Channel:
    def __init__(self):
        self.queue = asyncio.Queue()
        self.close = False

    # TODO: 增加超时
    async def pop(self):
        res = await self.queue.get()
        if res is None:
            self.close = True
            return False

        return res

    async def push(self, data: any):
        if self.close:
            return False

        await self.queue.put(data)

        return True
