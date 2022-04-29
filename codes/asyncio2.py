import asyncio
import time


# async/await 
# async def allows to call the function to become an async function 
# This does not mean the function will actually be called
# This also means this function becomes coroutine function

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
async def main():
    print(f"started at {time.strftime('%X')}")
    
    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")
    
# asyncio.run(main())

# This function does not work.
# Why? This does not register itself as a coroutine. 
# The async, await grammar should be kept. 
def main2():
    print(f"started at {time.strftime('%X')}")
    
    say_after(10, 'hello')
    say_after(10, 'world')

    print(f"finished at {time.strftime('%X')}")

# main2()



async def main3():
    task1 = asyncio.create_task(
        say_after(1,'hello')
    )
    
    task2 = asyncio.create_task(
        say_after(2, 'world')
    )
    print(f"started at {time.strftime('%X')}")
    
    # Wait until both tasks are completed (takes about 2 seconds)
    await task1
    await task2 
    
    print(f"finished at {time.strftime('%X')}")


# asyncio.run(main3())


'''
The concept of awaitable 
'''

async def nested():
    return 42

async def main4():
    # just by doing this won't do anything. 
    # This will only register nested function as a coroutine
    nested() 
    
    print(await nested())

# asyncio.run(main4())


# generator based coroutine with asyncio
def my_function(x):
    x += 2
    return x

async def nested(a):
    output = my_function(a)
    return output

async def main5():
    # This way, task1 and task2 are run concurrently with main5
    # create_task registers the nested() function as a coroutine
    task1 = asyncio.create_task(name= 'my_task',coro= nested(1))
    task2 = asyncio.create_task(name = 'my_new_task', coro = nested(2))
    
    await task1 
    await task2
    
    
    a = task1.get_name()
    b = task2.result()
    print(f'the name of the task is {a}')
    print(f'the result of the task is {b}')

# asyncio.run(main5())

# Future Example

# async def main():
#     await function_that_returns_a_future_object()
    
#     await aysncio.gather(
#         function_that_returns_a_future_object(),
#         some_python_coroutine()
#     )






