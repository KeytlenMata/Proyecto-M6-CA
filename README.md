# Proyecto Módulo 6 – Cajero Automático – Grupo A

## Descripción

Programa colaborativo en Python que simula un **cajero automático** con autenticación por PIN, soporte para múltiples usuarios y registro de movimientos.  

El sistema solicita un PIN de 4 dígitos para verificar la identidad del usuario. Una vez autenticado, permite realizar operaciones como consultar saldo, depositar, retirar dinero y ver el historial de transacciones. El programa incluye validación de entradas, manejo de saldos individuales y protección ante intentos fallidos de acceso.

Este proyecto fue desarrollado por 5 integrantes del Grupo A como parte de la actividad del Módulo 6.

## Características

- **Autenticación segura**:  
  - 3 intentos para ingresar el PIN  
  - Bloqueo automático tras intentos fallidos  
- **Múltiples usuarios**: cada uno con saldo e historial independiente  
- **Operaciones disponibles**:  
  - Consultar saldo  
  - Depositar dinero  
  - Retirar dinero (con verificación de saldo suficiente)  
  - Ver historial de movimientos (depósitos y retiros)  
- **Interfaz amigable**:  
  - Mensajes claros con emojis  
  - Separadores visuales para mejor legibilidad  
  - Validación de entradas numéricas  

## Integrantes

- Keytlen Mata  
- Brayan Abrego  
- Georgina Hanna  
- Iván Rodríguez  
- Edgar García  

## Cómo ejecutar

Para probar el cajero automático, clona el repositorio y ejecuta:

```bash
python main.py
```
