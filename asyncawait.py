import time
import asyncio
print(111)
time.sleep(0.5100)
print(222)

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')
    await asyncio.sleep(5)



asyncio.run(main())

print('finished')