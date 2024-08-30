# Instalación de PyAudio

Este archivo proporciona instrucciones para instalar la biblioteca `pyaudio` en un entorno Linux.

## Requisitos

Antes de instalar `pyaudio`, asegúrate de tener las herramientas de desarrollo necesarias y la biblioteca de PortAudio.

## Instalación de Dependencias

1. **Actualizar la lista de paquetes:**

   Abre una terminal y ejecuta el siguiente comando para actualizar la lista de paquetes disponibles:
   sudo apt-get update

2. **Instalar herramientas de desarrollo:**

   Instala las herramientas de desarrollo esenciales que se requieren para compilar paquetes:
   sudo apt-get install build-essential

3. **Instalar la biblioteca de PortAudio:**

   Instala `portaudio`, que es una dependencia necesaria para `pyaudio`:
   sudo apt-get install portaudio19-dev

4. **Instalar `pyaudio`:**

   Con las dependencias instaladas, ahora puedes instalar `pyaudio` usando `pip`:
   pip install pyaudio

## Verificación

Para verificar que `pyaudio` se ha instalado correctamente, puedes ejecutar el siguiente comando en tu terminal de Python:
import pyaudio
print(pyaudio.__version__)

Deberías ver la versión de `pyaudio` que se ha instalado.

## Problemas Comunes

- **Errores durante la instalación**: Asegúrate de que todas las dependencias están correctamente instaladas y actualizadas.
- **Compatibilidad**: Verifica que la versión de `pyaudio` sea compatible con tu versión de Python.

Si encuentras algún problema, por favor, proporciona detalles específicos para recibir asistencia adicional.
