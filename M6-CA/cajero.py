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

    