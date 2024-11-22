# Hyperf 多路复用 RPC 组件 Python 版本

[![pypi](https://img.shields.io/badge/PyPi-Passed-green?logo=python)](https://pypi.org/project/roc-py/)
[![Release](https://github.com/hyperf/roc-py/actions/workflows/release.yml/badge.svg)](https://github.com/hyperf/roc-py/actions/workflows/release.yml)
[![Release](https://img.shields.io/github/release/hyperf/roc-py)](https://github.com/hyperf/roc-py/releases)

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