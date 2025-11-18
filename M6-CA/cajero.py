usuarios = {
    "1234": {"saldo": 1500, "historial": []},
    "2219": {"saldo": 3500, "historial": []},
    "0000": {"saldo": 900, "historial": []}
}

#Funcion de login
def login():

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
            return pin
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

#Operacion de deposito

def deposito(pin):
    print("\n" + "="*60)
    print("                💰 DEPÓSITO")
    print("="*60)

    try:
        monto = float(input("Ingrese el monto a depositar: ").strip())

        if monto <= 0:
            print("⚠️  El monto debe ser mayor que cero.")
            return

    except ValueError:
        print("⚠️  Entrada inválida. Debe ingresar un número.")
        return

    saldo_actual = usuarios[pin]["saldo"]

    usuarios[pin]["saldo"] = saldo_actual + monto

    usuarios[pin]["historial"].append({
        "tipo": "Depósito",
        "monto": monto,
        "saldo_restante": usuarios[pin]["saldo"]
    })

    print(f"\n✅ Depósito exitoso. Ha depositado ${monto}.")
    print(f"💳 Nuevo saldo: ${usuarios[pin]['saldo']}")
    print("="*60)

    input("Presione ENTER para continuar...")

#Operacion de retiro

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

    input("Presione ENTER para continuar...")


#Operación de historial 

def mostrar_historial(pin):
    print("\n" + "="*60)
    print("           📑 HISTORIAL DE TRANSACCIONES")
    print("="*60)

    historial = usuarios[pin]["historial"]

    if not historial:
        print("📭 No hay transacciones registradas aún.")
        print("="*60)
        return
    
    for i, mov in enumerate(historial, start=1):
        tipo = mov.get("tipo", "N/A")
        monto = mov.get("monto", "N/A")
        saldo_restante = mov.get("saldo_restante", "N/A")

        print(f"{i}. Tipo: {tipo} | Monto: ${monto} | Saldo restante: ${saldo_restante}")

        print("="*60)
    
    input("Presione ENTER para continuar...")




    
