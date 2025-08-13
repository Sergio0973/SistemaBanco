"""
Sistema de Gestión de Cuentas Bancarias
1. Crear cuenta
2. Depositar
3. Solicitar Credito
4. Retirar Dinero
5. Pago Cuota Credito
6. Cancelar Cuenta
7. Salir

Portafolio - Banco
- cta Ahorros
- cta Corriente
- CDT
- Credito:
    - Libre Inv.
- Credito:
    - Vivienda
- Credito:
    - Compra Auto
    - Movil

Datos Cliente
- CC
- Nombre
- Email
- Edad
- Contacto:
    - Movil
    - Fijo
- Ubicacion:
    - Pais
    - Departamento
    - Ciudad
    - Direccion

ProductoClient
- CC
- Producto:
    - idProducto
    - fechaInicio
    - Estado(Activo, Inactivo, Cancelado, Pagado)
    - Saldo - pendiente en el producto
    - Historial:
        - id
        - fechaMovimiento
        - Valor
        - Tipo Movimiento
"""
#Importacion Librerias
import os, random, time
from colorama import Fore, Style, init
init(autoreset=True)

cuentasBancarias = {}

#Funcionn Limpiar Consola
def LimpiarConsola():
    limpiar = os.system("cls" if os.name == "nt" else "clear")
    return limpiar

#Funcion Agregar Cuenta
def addCuenta(numeroCuenta, titular, cc, correo, edad, movil, fijo, pais, dep, ciudad, direccion,idProducto, producto, estado):
    if numeroCuenta in cuentasBancarias:
        print("La cuenta ya existe.")
    else:
        cuentasBancarias[numeroCuenta] = {
            "CC": cc,
            "titular": titular,
            "Correo": correo,
            "Edad": edad,
            "Contacto": {
                "Movil": movil,
                "Fijo": fijo
            },
            "Ubicacion": {
                "Pais": pais,
                "Departamento": dep,
                "Ciudad": ciudad,
                "Direccion": direccion
            },
            "Productos": {
                idProducto: {
                    'NombreProducto' : producto,
                    'Saldo': 0,
                    'Estado': estado,
                    'Historial' : {}
                }
            },
        }
    print("Cuenta creada exitosamente.")

#Funcion Menu Clientes
def menuClientes():
    print('1. Datos Cliente \n2. Saldos \n3. Creditos \n4. Inversiones \n0.Salir')

#Funcion Menu Saldos
def menuSaldos():
    print('1. Cta Ahorros \n2. Cta Corriente')

#Funcion Menu Creditos
def menuCreditos():
    print('1. Credito Libre Inversion \n2. Credito Vivienda \n3. Credito Compra AutoMovil \n0. Salir ')

#Funcion Menu Portafolio
def menuPortafolio():
    print('1. Cta Ahorros \n2. Cta Corriente \n3. CDT \n4. Credito Libre Inversion \n5. Credito Vivienda \n6. Credito Compra AutoMovil \n0. Salir')

