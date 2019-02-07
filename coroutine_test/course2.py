import time
import asyncio


def now(): return time.time()


async def do_some_work(x):
    print('waiting:', x)
    await asyncio.sleep(x)
    return 'Done after %ss' % x


def callback(future):
    print('callback:', future.result())


start = now()
coroutine = do_some_work(2)

loop = asyncio.get_event_loop()

task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)
loop.run_until_complete(task)

print('Time:', now()-start)
