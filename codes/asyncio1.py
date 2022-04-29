import asyncio
import time

async def main():
    start = time.time()
    print('Hello...')
    await asyncio.sleep(1) 
    print('...World!')
    print('time :', time.time() - start)
    
    
asyncio.run(main())