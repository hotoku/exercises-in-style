#!/usr/bin/env python3

import logging
import asyncio
import sys


logging.basicConfig(
    level=logging.INFO,
    stream=sys.stderr
)
LOGGER = logging.getLogger()


def make_coro(f, src, sink):
    async def coro():
        LOGGER.info("%s start", f(0))
        while True:
            n = await src.get()
            await sink.put(f(n))
            src.task_done()
    return coro()


async def printer(queue):
    LOGGER.info("printer start")
    while True:
        n = await queue.get()
        print(n, end="")
        queue.task_done()


async def dispatch(queue, fizz, buzz, number):
    LOGGER.info("dispatch start")
    while True:
        n = await queue.get()
        flag = True
        if n % 3 == 0:
            await fizz.put(n)
            flag = False
        if n % 5 == 0:
            await buzz.put(n)
            flag = False
        if flag:
            await number.put(n)
        print()
        queue.task_done()


async def main():
    fizz = asyncio.Queue(1)
    buzz = asyncio.Queue(1)
    num = asyncio.Queue(1)
    qprint = asyncio.Queue(1)
    qdispatch = asyncio.Queue()
    tasks = [
        asyncio.create_task(make_coro(lambda n: "Fizz", fizz, qprint)),
        asyncio.create_task(make_coro(lambda n: "Buzz", buzz, qprint)),
        asyncio.create_task(make_coro(lambda n: str(n), num, qprint)),
        asyncio.create_task(printer(qprint)),
        asyncio.create_task(dispatch(qdispatch, fizz, buzz, num))
    ]
    for n in range(1, 10):
        qdispatch.put_nowait(n)
    await qdispatch.join()

    for t in tasks:
        t.cancel()
    await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(main())
