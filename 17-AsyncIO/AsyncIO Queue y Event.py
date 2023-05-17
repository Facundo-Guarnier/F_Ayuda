import asyncio

#! Corutina que produce datos y los coloca en la cola
async def productor(queue, evento):
    print("P Inicio del productor")
    
    for item in range(5):
        # Realiza operaciones de producción
        await asyncio.sleep(2)
        
        await queue.put(item)
        print("P Productor: elemento", item, "colocado en la cola")
        evento.set()  # Establece el evento
    
    await asyncio.sleep(2)
    await queue.put("Fin")  # Marca el final de la cola
    print("P Fin del productor")
    evento.set()  # Establece el evento


#! Corutina que consume datos de la cola
async def consumidor(queue, evento):
    print("C Inicio del consumidor")
    while True:

        await evento.wait()  # Espera a que el evento se establezca
        evento.clear()  # Limpia el evento después de que se establezca
        
        item = await queue.get()
        if item == "Fin":
            break  # Si se recibe None, se finaliza el bucle
        
        print("C Consumidor: elemento", item, "recibido de la cola")
        

        # Realiza operaciones de consumo
        await asyncio.sleep(0.5)
    print("C Fin del consumidor")


#! Función principal
async def main():
    print("M Inicio de la función principal")
    
    # Crea una cola y un evento
    cola = asyncio.Queue()
    evento = asyncio.Event()
    # Crea las corutinas de productor y consumidor
    tarea_productor = asyncio.create_task(productor(cola, evento))
    tarea_consumidor = asyncio.create_task(consumidor(cola, evento))

    # Espera a que las corutinas finalicen
    await asyncio.gather(tarea_productor, tarea_consumidor)

    print("M Fin de la función principal")


#! Ejecución principal
if __name__ == '__main__':
    asyncio.run(main())  # Ejecuta la función principal como una tarea asyncio
