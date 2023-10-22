import pyttsx3

# Crear un objeto de motor de texto a voz
engine = pyttsx3.init()

# Texto que deseas convertir en voz
number=123
mensaje = f"Este es un mensaje de ejemplo que será convertido en voz. {number}"

# Configura la voz y el idioma (puedes ajustar la voz según tus preferencias)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Elige la primera voz disponible

# Reproduce el mensaje
engine.say(mensaje)
engine.runAndWait()

# Cierra el motor de texto a voz
engine.stop()
