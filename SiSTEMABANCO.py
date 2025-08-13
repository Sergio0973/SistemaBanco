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

#Manejo del Historial
def agregarHistorial(numeroCuenta, idProducto, valor, tipoMovimiento):
    """Registra un movimiento en el historial de un producto."""
    if numeroCuenta in cuentasBancarias and idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
        historial = cuentasBancarias[numeroCuenta]["Productos"][idProducto]["Historial"]

        nuevo_id = len(historial) + 1  # ID incremental
        historial[nuevo_id] = {
            "FechaMovimiento": time.strftime("%Y-%m-%d %H:%M:%S"),
            "Valor": valor,
            "TipoMovimiento": tipoMovimiento
        }
    else:
        print("No se pude registrar el historial del cliente: cuenta o producto no encontrado.")


#Ejecucion Principal
while True:
    try:
        opcion = int(input("Seleccione una opción valida:\n1. Crear una cuenta\n2. Depositar dinero\n3. Solicitar Crédito\n4. Retirar Dinero de la cuenta\n5. Pago de la Cuota del Crédito\n6. Cancelar Cuenta\n0. Salir \nIngresa una Opcion: "))
        match opcion:
            case 1:
                LimpiarConsola()

                #Generacion Producto y eleccion de producto a solicitar
                while True:
                    try:
                        menuPortafolio()
                        opcion = input('\nIngresa una opcion valida: ')
                        e = True
                        idProducto = None  # <- inicializamos por defecto

                        match opcion:
                            case "1":
                                producto = 'Cuenta Ahorros'
                                while e:
                                    idProducto = random.randint(10000, 20000)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False
                                break

                            case "2":
                                producto = 'Cta Corriente'
                                while e:
                                    idProducto = random.randint(4000, 10000)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False
                                break

                            case "3":
                                producto = 'CDT'
                                while e:
                                    idProducto = random.randint(500000, 622000)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False

                                # Solicitar datos del CDT
                                monto_inversion = float(input("Ingrese el monto a invertir en el CDT: "))
                                plazo_dias = int(input("Ingrese el plazo del CDT (en días): "))
                                tasa_interes = 0.05  # 5% anual fijo

                                # Guardar temporalmente estos datos para añadirlos tras crear la cuenta
                                datos_cdt = {
                                    "montoinversion": monto_inversion,
                                    "plazo": plazo_dias,
                                    "tasa": tasa_interes
                                }
                                break

                            case "4":
                                producto = 'Credito Libre Inversion'
                                while e:
                                    idProducto = random.randint(80000, 100000)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False
                                break

                            case "5":
                                producto = 'Credito Vivienda'
                                while e:
                                    idProducto = random.randint(400000, 500000)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False
                                break

                            case "6":
                                producto = 'Credito Compra AutoMovil'
                                while e:
                                    idProducto = random.randint(100000, 200000)
                                    existe = any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values())
                                    if not existe:
                                        e = False
                                break

                            case "0":
                                print("Cancelando de la creación de cuenta...")
                                break

                            case _:
                                print('Ingresa una Opcion especifica')
                                continue  # <- evitamos seguir si no es válido
                    except (ValueError,KeyboardInterrupt,TypeError) as e:
                        print(f'Error: {e}')

                # Si no se generó idProducto, no seguimos
                if idProducto is None:
                    continue

                LimpiarConsola()
                print("Crear Cuenta")

                #Datos Solicitados Cliente
                numeroCuenta = random.randint(1, numeroCuenta)
                print(f'Tu numero de cuenta general es: {numeroCuenta}')
                print(f'Tu producto: {producto}, el numero es: {idProducto}')

                cc = input('Ingresa la cedula del cliente: ')
                titular = input("Ingrese el nombre del cliente: ")
                email = input('Ingresa el correo del cliente: ')
                edad = int(input('Ingresa la edad del cliente: '))

                print('Ingresa el movil y fijo del cliente: ')
                movil = int(input('Ingresa el movil del cliente: '))
                fijo = int(input('Ingresa el fijo del cliente: '))

                print('Ingresa los datos de residencia del cliente: ')
                pais = input('Ingresa el pais del cliente: ')
                dep = input('Ingresa el departamento del cliente: ')
                ciudad = input('Ingresa la ciudad del cliente: ')
                direccion = input('Ingresa la Direccion del cliente: ')

                estado = "Activo"
                addCuenta(numeroCuenta, titular, cc, email, edad, movil, fijo, pais, dep, ciudad, direccion,idProducto, producto, estado)

                if producto == "CDT":
                    cuentasBancarias[numeroCuenta]["Productos"][idProducto]["Saldo"] = datos_cdt["monto"]
                    cuentasBancarias[numeroCuenta]["Productos"][idProducto]["Plazo"] = datos_cdt["plazo"]
                    cuentasBancarias[numeroCuenta]["Productos"][idProducto]["Tasa"] = datos_cdt["tasa"]
                    agregarHistorial(numeroCuenta, idProducto, datos_cdt["monto"], "Apertura CDT")

                input("Presione Enter para continuar...")
                LimpiarConsola()

            case 2:
                #Depositar Dinero en una cuenta
                LimpiarConsola()
                print("Depositar el Dinero")
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta in cuentasBancarias:

                    print("\nProductos disponibles:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        print(f"  {idProd} - {datosProd['NombreProducto']} (Saldo: {datosProd['Saldo']})")

                    # Pedir producto
                    idProducto = int(input("\nIngrese el ID del producto al que desea depositar: "))

                    if idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
                        monto = float(input("Ingrese el monto a depositar: "))

                        # Sumar al saldo
                        cuentasBancarias[numeroCuenta]["Productos"][idProducto]['Saldo'] += monto
                        agregarHistorial(numeroCuenta, idProducto, monto, "Depósito")

                        print(f"\nDepósito realizado con éxito.")
                        print(f"Nuevo saldo: {cuentasBancarias[numeroCuenta]['Productos'][idProducto]['Saldo']}")
                    else:
                        print("El producto no existe.")
                else:
                    print(f'La cuenta {numeroCuenta} No esta asociada')

                input("\nPresione Enter para continuar...")
                LimpiarConsola()

            case 3:
                #Solicitud de un Credito, Mirando si es Apto o no para el Credito
                LimpiarConsola()
                print('=== Solicitar Crédito ===')

                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta not in cuentasBancarias:
                    print("La cuenta no existe.")
                    input("Enter para continuar...")
                    break

                # Mostrar menú de créditos
                while True:
                    try:
                        print('\n¿Qué tipo de crédito deseas solicitar?')
                        opcion = input('1. Crédito Libre Inversión \n2. Crédito Vivienda \n3. Crédito Compra Automóvil \n0. Salir \nOpción: ')
                        e = True
                        idProducto = None

                        match opcion:
                            case "1":
                                producto = 'Crédito Libre Inversión'
                                while e:
                                    idProducto = random.randint(80000, 100000)
                                    if not any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values()):
                                        e = False
                                break
                            case "2":
                                producto = 'Crédito Vivienda'
                                while e:
                                    idProducto = random.randint(400000, 500000)
                                    if not any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values()):
                                        e = False
                                break
                            case "3":
                                producto = 'Crédito Compra Automóvil'
                                while e:
                                    idProducto = random.randint(100000, 200000)
                                    if not any(idProducto in cuenta["Productos"] for cuenta in cuentasBancarias.values()):
                                        e = False
                                break
                            case "0":
                                print("Solicitud cancelada.")
                                continue
                            case _:
                                print("Opción inválida.")
                                continue
                    except (ValueError, KeyboardInterrupt, TypeError) as e:
                        print(f'Error: {e}')

                LimpiarConsola()
                # Datos para evaluación
                ingresosMensuales = float(input('Ingresa el total de ingresos mensuales: '))
                montoSolicitado = float(input('Ingresa el monto de crédito solicitado: '))
                plazoMeses = int(input('Ingresa el plazo (meses) para pagar: '))
                LimpiarConsola()

                #Calculo del RCI - Relacion Cuota Ingresos
                cuota = montoSolicitado / plazoMeses
                RCI = cuota / ingresosMensuales

                print(f"\nEvaluando crédito... (RCI: {RCI:.2f})")
                time.sleep(1)

                LimpiarConsola()
                #Evaluacion si es Apto o No
                if RCI <= 0.4:
                    print("Crédito fue aprobado.")

                    # Registrar el crédito en la cuenta
                    cuentasBancarias[numeroCuenta]["Productos"][idProducto] = {
                        "NombreProducto": producto,
                        "Saldo": montoSolicitado,
                        "Estado": "Activo",
                        "Historial": {
                            1: {
                                "FechaMovimiento": time.strftime("%Y-%m-%d"),
                                "Valor": montoSolicitado,
                                "TipoMovimiento": "Crédito Aprobado"
                            }
                        }
                    }
                    print(f"Crédito {producto} creado con ID {idProducto} y saldo {montoSolicitado}")
                else:
                    print("No eres apto para el crédito (RCI mayor a 0.4).")
                input("Enter para continuar...")
                LimpiarConsola()

            case 4:
                #Retiraramos Dinero que tengamos en alguna de las cuentas
                LimpiarConsola()
                print("Retirar Dinero")
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                #La cuenta existe?
                if numeroCuenta in cuentasBancarias:

                    print("\nProductos disponibles:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        print(f"  {idProd} - {datosProd['NombreProducto']} (Saldo: {datosProd['Saldo']})")

                    # Pedir producto
                    idProducto = int(input("\nIngrese el ID del producto al que desea Retirar: "))

                    if idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
                        monto = float(input("Ingrese el monto a Retirar: "))

                        #Revisa que el saldo de la cuenta, es mayor al monto que desea retirar el cliente
                        if cuentasBancarias[numeroCuenta]["Productos"][idProducto]['Saldo'] > monto:
                            cuentasBancarias[numeroCuenta]["Productos"][idProducto]['Saldo'] -= monto
                            agregarHistorial(numeroCuenta, idProducto, -monto, "Retiro")

                            print(f"\nDepósito realizado con éxito.")
                            print(f"Nuevo saldo: {cuentasBancarias[numeroCuenta]['Productos'][idProducto]['Saldo']}")
                        else:
                            print('Saldo insuficiente')
                            print(f"Saldo: {cuentasBancarias[numeroCuenta]['Productos'][idProducto]['Saldo']}")

                    else:
                        print("El producto no existe.")
                else:
                    print("La cuenta no existe.")

                input("\nPresione Enter para continuar...")
                LimpiarConsola()

            case 5:
                #Pago de la cuota del Credito
                LimpiarConsola()
                print("Pago de Cuota de Crédito")
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta in cuentasBancarias:
                    # Mostrar productos disponibles
                    print("Productos de la cuenta:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        print(f"ID: {idProd} - {datosProd['Nombre']} - Saldo: {datosProd['Saldo']} - Estado: {datosProd['Estado']}")

                    idProducto = int(input("Ingrese el ID del producto (crédito) a pagar: "))

                    if idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
                        producto = cuentasBancarias[numeroCuenta]["Productos"][idProducto]

                        if "Credito" in producto["Nombre"]:
                            monto = float(input("Ingrese el monto a pagar: "))

                            if monto > 0:
                                if monto >= producto["Saldo"]:
                                    producto["Saldo"] -= monto
                                    agregarHistorial(numeroCuenta, idProducto, -monto, "Pago Cuota Crédito")

                                    print("Crédito pagado en su totalidad.")
                                else:
                                    producto["Saldo"] -= monto
                                    print(f"Pago realizado. Saldo restante del crédito: {producto['Saldo']}")
                            else:
                                print("El monto debe ser mayor a 0.")
                        else:
                            print("El producto seleccionado no es un crédito.")
                    else:
                        print("El ID del producto no existe.")
                else:
                    print("La cuenta no existe.")

                input("Presione Enter para continuar...")
                LimpiarConsola()

            case 6:
                #Cancelacion de una de las cuentas del cliente
                LimpiarConsola()
                print('Cancelar Cuenta')
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta in cuentasBancarias:
                    print("\nProductos disponibles:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        print(f"  {idProd} - {datosProd['NombreProducto']} (Saldo: {datosProd['Saldo']})")

                    idProducto = int(input("\nIngrese el ID del producto al que desea Cancelar: "))
                    if cuentasBancarias[numeroCuenta]["Productos"][idProducto] == 0:
                        valorEliminado = cuentasBancarias[numeroCuenta]["Productos"].pop(idProducto)
                        print(valorEliminado)
                        print(cuentasBancarias)
                    else:
                        print('')

                    input('Enter para continuar')

                LimpiarConsola()

            case 7:
                LimpiarConsola()
                print("Redimir CDT")
                numeroCuenta = int(input("Ingrese el número de cuenta: "))

                if numeroCuenta in cuentasBancarias:
                    print("\nCDTs disponibles:")
                    for idProd, datosProd in cuentasBancarias[numeroCuenta]["Productos"].items():
                        if datosProd["NombreProducto"] == "CDT":
                            print(f"  {idProd} - Monto: {datosProd['Saldo']} - Plazo: {datosProd.get('Plazo', 0)} días")

                    idProducto = int(input("\nIngrese el ID del CDT a redimir: "))

                    if idProducto in cuentasBancarias[numeroCuenta]["Productos"]:
                        cdt = cuentasBancarias[numeroCuenta]["Productos"][idProducto]
                        interes_ganado = cdt["Saldo"] * cdt["Tasa"] * (cdt["Plazo"] / 365)
                        total_a_pagar = cdt["Saldo"] + interes_ganado
                        print(f"Total a recibir: {total_a_pagar:.2f}")

                        agregarHistorial(numeroCuenta, idProducto, total_a_pagar, "Redención CDT")
                        cdt["Saldo"] = 0
                        cdt["Estado"] = "Pagado"
                    else:
                        print("CDT no encontrado.")
                else:
                    print("Cuenta no encontrada.")

                input("\nPresione Enter para continuar...")
                LimpiarConsola()

            case 0:
                LimpiarConsola()
                print("Saliendo del sistema...")
                break

            case _:
                print('Ingresa una Opcion valida')
                LimpiarConsola()

    except (ValueError, TypeError, KeyboardInterrupt) as e:
        print(f"Error: {e}. Por favor, ingrese un valor válido.")
        continue