# Hyperf 多路复用 RPC 组件 Python 版本

## 如何使用

```python
import asyncio

from roc.request import Request
from roc.socket import Client


async def main():
    client = Client(host="127.0.0.1", port=9502)
    while True:
        req = Request(path="/test/test",
                      params={"mobile": "123123", "data": "HelloWorld"})
        res = await client.request(req)
        print(res.result)
        await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())

```