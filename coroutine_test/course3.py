import time
import asyncio


def now(): return time.time()


async def do_some_work(x):
    print('waiting:', x)
    await asyncio.sleep(x)
    return 'Done after %ss' % x

start = now()
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine3 = do_some_work(4)

tasks=[
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3)
]

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
    
except KeyboardInterrupt as e:  # press ctrl+C will cause this exception which cancel all tasks
    print(asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()

print('Time:', now()-start)