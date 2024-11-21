import asyncio

from roc.request import Request
from roc.socket import Client


async def main():
    client = Client(host="127.0.0.1", port=9502)
    while True:
        req = Request(path="/push_interface/sendSms",
                      params={"mobile": "123123", "templateId": 1, "data": "HelloWorld"})
        res = await client.request(req)
        print(res.result)
        await asyncio.sleep(1)


asyncio.run(main())
