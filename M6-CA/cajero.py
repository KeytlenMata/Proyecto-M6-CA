usuarios = {
    "1234": {"saldo": 1500, "historial": []},
    "2219": {"saldo": 3500, "historial": []},
    "0000": {"saldo": 900, "historial": []}
}

print("\n" + "="*60)
print("                🏦  SISTEMA DE CAJERO AUTOMÁTICO")
print("="*60)
print(" Por favor, verifica tu identidad para acceder a tu cuenta.")
print("="*60)

intentos = 3
pin = ""

while intentos > 0:
    pin = input("\n🔐 Ingresa tu PIN (4 dígitos): ").strip()
    if pin in usuarios:
        print("\n✅ Acceso concedido. ¡Bienvenido!")
        print("-"*60)
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"❌ PIN incorrecto. Te quedan {intentos} intento(s).")
        else:
            print("❌ PIN incorrecto.")

if intentos == 0:
    print("\n⚠️  Demasiados intentos fallidos.")
    print("🔒 El sistema se ha bloqueado por seguridad.")
    print("="*60)
    exit()

# MENÚ PRINCIPAL - ESTUDIANTE 2

def menu_principal(pin):
    saldo = 0
    while True:
        print("\n" + "="*60)
        print("                 📋 MENÚ PRINCIPAL")
        print("="*60)
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial de transacciones")
        print("5. Salir")
        print("="*60)

        opcion = input(" Selecciona una opción: ").strip()

        if opcion == "1":
            print("Su saldo es ", saldo)

        elif opcion == "2":
            try:
                deposito = int(input("Cuanto desea depositar? "))
            except ValueError:
                print("Solo ingrese numeros validos, por favor.")
            saldo += deposito


        elif opcion == "3":
            retirar(pin)

        elif opcion == "4":
            mostrar_historial(pin)

        elif opcion == "5":
            print("\n Gracias por usar el cajero. Hasta luego.")
            break

        else:
            print("\n Opción inválida. Intenta nuevamente.")

#Parte 4 : Operacion de retiro

def retirar(pin):
    print("\n" + "="*60)
    print("                💸 OPERACIÓN DE RETIRO")
    print("="*60)

    # Verificar el saldo actual del usuario
    saldo_actual = usuarios[pin]["saldo"]
    print(f"💰 Saldo disponible: ${saldo_actual}")

    try:
        monto = float(input("Ingrese el monto que desea retirar: ").strip())

        # Validación de monto positivo
        if monto <= 0:
            print("⚠️  El monto debe ser mayor que cero.")
            return
        
    except ValueError:
        print("⚠️  Entrada inválida. Debe ingresar un número.")
        return

    # Verificación de saldo suficiente
    if monto > saldo_actual:
        print("❌ Fondos insuficientes. No se puede realizar el retiro.")
        return

    # Procesar el retiro
    usuarios[pin]["saldo"] -= monto

    # Registrar en el historial
    usuarios[pin]["historial"].append({
        "tipo": "Retiro",
        "monto": monto,
        "saldo_restante": usuarios[pin]["saldo"]
    })

    print(f"\n✅ Retiro exitoso. Ha retirado ${monto}.")
    print(f"💳 Nuevo saldo: ${usuarios[pin]['saldo']}")
    print("="*60)



# Llamada al menú después del login
menu_principal(pin)




    
