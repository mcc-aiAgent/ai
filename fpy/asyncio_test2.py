import asyncio


async def coroutine_one():
    print("hello")


async def coroutine_two():
    print("world")


async def main():
    task1 = asyncio.create_task(coroutine_one())
    task2 = asyncio.create_task(coroutine_two())
    await task1
    await task2


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
