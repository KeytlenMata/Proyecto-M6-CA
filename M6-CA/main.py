import cajero

pin = cajero.login()

def menu_principal(pin):   
    while True:
        saldo = cajero.usuarios[pin]["saldo"]

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
            input("Presione ENTER para continuar...")

        elif opcion == "2":
            cajero.deposito(pin)
            
        elif opcion == "3":
            cajero.retirar(pin)

        elif opcion == "4":
            cajero.mostrar_historial(pin)

        elif opcion == "5":
            print("\n Gracias por usar el cajero. Hasta luego.")
            break

        else:
            print("\n Opción inválida. Intenta nuevamente.")

menu_principal(pin)