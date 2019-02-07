import time
import asyncio


def now(): return time.time()


async def do_some_work(x):
    print('waiting: ', x)
    return 1

start = now()

coroutine = do_some_work(2)
print(coroutine)

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)

print('Time: ', now()-start)

print('*'*50)


start = now()
loop1 = asyncio.get_event_loop()
coroutine1 = do_some_work(3)
task = loop.create_task(coroutine1)
print(task)
loop1.run_until_complete(task)
print(task)
print('Time: ', now()-start)
