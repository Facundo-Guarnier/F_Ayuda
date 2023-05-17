import asyncio

# Corutina asíncrona que devuelve un valor
async def mi_corutina():
    print("C Inicio de la corutina")
    await asyncio.sleep(10)  # Simula una operación asíncrona (espera 1 segundo)
    print("C Fin de la corutina")
    return "¡Valor devuelto!"

# Función principal
async def main():
    print("M Inicio de la función principal")
    
    # Programa la corutina en segundo plano como una tarea asincrónica
    tarea_corutina = asyncio.create_task(mi_corutina())
    
    # Continúa ejecutando otras operaciones mientras la corutina se procesa en segundo plano
    print("M Continuando con otras operaciones...")
    
    # Ejemplo: Espera 2 segundos adicionales antes de continuar
    await asyncio.sleep(2)
    
    print("M Finalización de otras operaciones")
    
    # Espera el resultado de la corutina cuando sea necesario
    resultado = await tarea_corutina
    print("M Resultado:", resultado)
    
    print("M Fin de la función principal")


# Ejecución principal
if __name__ == '__main__':
    asyncio.run(main())  # Ejecuta la función principal como una tarea asyncio
