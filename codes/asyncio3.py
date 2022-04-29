import asyncio
import time


# asyncio program

async def main():
    await asyncio.sleep(1)
    print('hello')

# asyncio.run(main())


# Making Tasks

async def my_coro():
    print('i do not know what to say')


async def main2():
    start = time.time()
    print(start)
    # await asyncio.sleep(1)
    # task = asyncio.create_task(my_coro())
    
    asyncio.gather(my_coro(), my_coro())
    
    print(time.time() - start)
# This outputs two of the my_coro 
# asyncio.run(main())

def main3():
    start= time.time()
    print(start)
    my_coro()
    time.sleep(1)
    my_coro()
    print(time.time() - start)

# main3()


# Task at once

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"task {name}: Compute factorial({number}), currently i = {i}...")
        await asyncio.sleep(1)
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main():
    L = await asyncio.gather(
        factorial("A",2),
        factorial("B",3),
        factorial("C",4)
    )
    print(L)

# asyncio.run(main())
        

# another thread

async def blocking_io():
    print(f"start blocking_io at {time.strftime('%X')}")
    await asyncio.sleep(2)
    print(f"blocking_io complete at {time.strftime('%X')}")


async def main():
    print(f"started main at {time.strftime('%X')}")
    
    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1)
    )

    print(f"finished main at {time.strftime('%X')}")

# The coroutines run in a different thread    
asyncio.run(main())

