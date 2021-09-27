#pip install gTTs
from gtts import gTTS #Generador de audio.

audio= ("Nombre_archivo" + ".extensión")

lenguage="es"

"""
Lenguajes disponibles (reemplazar en variable lenguaje):
- en
- fr
- zh-CN
- zh-TW
- pt
- es

Documentación: https://gtts.readthedocs.io/en/latest/module.html
"""
texto= input("Ingresar texto para transformar a sonido:\n")

sp=gTTS(text=texto, lang = lenguage , slow=False) #Generar audio con texto escrito.
sp.save(audio) #Guardar audio.

print("Audio generado correctamente")
