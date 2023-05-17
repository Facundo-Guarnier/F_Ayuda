import asyncio

async def tarea_externa():
    print("1 Tarea externa comenzada")
    a = asyncio.create_task(tarea_interna())    
    await asyncio.sleep(1)
    print("1 Tarea externa completada")
    await a
    
async def tarea_interna():
    print("2 Tarea interna comenzada")
    await asyncio.sleep(5)
    print("2 Tarea interna completada")

async def tarea_extra():
    print("3Tarea extra comenzada")
    await asyncio.sleep(2)
    print("3Tarea extra completada")

async def main():
    await asyncio.gather(
        asyncio.create_task(tarea_externa()), 
        asyncio.create_task(tarea_extra()),
    )

if __name__ == '__main__':
    asyncio.run(main())