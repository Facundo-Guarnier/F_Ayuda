'''
Consiste en trasladar la naturaleza de los objetos reales al codigo de programación
Es decir, los objetos tienen un estado, comportamiento y propiedades
'''

'''
Conceptos:
    - Clase: modelo donde se redactan las caracteristicas comunes de un grupo de objetos.
    - Modularización: un programa puede estar compuesto de varias clases o modulos que funcionan en forma independiente.
    - Encapsulamiento / encapsulación: habla de como una clase o modulo unicamente comprende su funcionamiento y no el de otros modulos,
        asi, de esta manera cada modulo permanece protegido a intervencion externa de otros modulos. Estas logran conectarse creando
        metodos de acceso.
    - Herencia: heredar atributos de una clase padre a las demas clases.
'''

class Auto:

    def __init__(self,motor,ruedas,gas):              #* El __init__ es el constructor de tu clase en el que creas una nueva instancia de la clase
        self.motor = motor                            #* en este se colocan los atributos propios de la clase
        self.ruedas = ruedas
        self.gas = gas

'''
Caracteristicas __init__:

    El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
    El método __init__ se llama automáticamente. Es decir es imposible de olvidarse de llamarlo ya que se llamará automáticamente.
    El método __init__ no puede retornar dato.
    el método __init__ puede recibir parámetros que se utilizan normalmente para inicializar atributos.
    El método __init__ es un método opcional, de todos modos es muy común declararlo.
'''

'''
Herencia: permite crear una clase general primero y luego más tarde crear clases más especializadas que re-utilicen código de la clase general

Ejemplo practico de Herencia con POO: Se quieren realizar transacciones de deposito/extracción en una cuenta bancaria, para ello de debe considerar:

    - Si la cuenta es de tipo Caja de ahorro, el saldo no puede ser menor a 0 y no hay limite de extracción
    - Si la cuenta es de tipo Cuenta corriente, el saldo no puede ser menor a -3000 y hay un limite de extraccion de 2000
'''

class CuentaBancaria:                                 #* Se crea la clase padre Cuenta Bancaria

    def __init__ (self):                              #* En este caso no se colocan variables luego del self, para que al usar herencia, las clases hijas no repitan los valores de las demas clases
        self.movimientos = []                         #* Aca directamente se crea la variable movimientos y se especifica que es una lista           

    def deposito(self, monto):                        #* Se crea una funcion deposito que es comun, y sera heredado a todas las clases
        self.movimientos.append(monto)

    def saldo_final(self):                            #* Esta funcion tambien sera comun, y calculara el saldo final mediante la suma de los elementos en la lista movimientos
        saldo = 0
        for mov in self.movimientos:
            saldo += mov
        return saldo


class CajaAhorro(CuentaBancaria):                     #* Se coloca la clase padre entre parentesis para heredar sus atributos
   
    def extraccion (self, monto):                     #* Al no colocar __init__, CajaAhorro toma el constructor de CuentaBancaria directamente (padre)
        if monto <= self.saldo_final():
            self.movimientos.append(-monto)

class CuentaCorriente(CuentaBancaria):

    def __init__ (self):
        super().__init__()                            #* Se llama al constructor de la clase padre -CuentaBancaria-
        self.limite = -3000                           #* En este caso se utiliza para poder agregar un atributo mas pero propio de la clase -CuentaCorriente-

    def extraccion (self, monto):
        if self.saldo_final() - monto >= self.limite:
            self.movimientos.append(-monto)

'''
Función super():

    Esta función nos permite invocar y conservar un método o atributo de una clase padre (primaria) desde una clase hija (secundaria) sin tener que 
    nombrarla explícitamente. Esto nos brinda la ventaja de poder cambiar el nombre de la clase padre (base) o hija (secundaria) cuando queramos y 
    aún así mantener un código funcional, sencillo  y mantenible.
'''