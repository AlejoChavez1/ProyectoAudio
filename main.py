import librosa
import soundfile as sf

# Ruta del archivo de audio en formato .mp3
mp3_file = 'C:\\Users\\alede\\Desktop\\Cosas\\paor.mp3'
wav_file = 'C:\\Users\\alede\\Desktop\\Cosas\\paor.wav'

# Paso 1: Cargar el archivo .mp3 y convertirlo a .wav
try:
    # Cargar el archivo .mp3
    y, sr = librosa.load(mp3_file, sr=None)  # sr=None preserva la tasa de muestreo original

    # Guardar el archivo como .wav
    sf.write(wav_file, y, sr)
    print(f"Archivo convertido guardado en: {wav_file}")
except Exception as e:
    print(f"Error durante la conversión: {e}")

# Paso 2: Cargar el archivo .wav y realizar el análisis de muestreo
try:
    # Cargar el archivo .wav
    y, sr = librosa.load(wav_file, sr=None)  # sr=None preserva la tasa de muestreo original

    # Mostrar información sobre el archivo
    print(f"Duración del archivo: {librosa.get_duration(y=y, sr=sr)} segundos")
    print(f"Tasa de muestreo: {sr} Hz")
except Exception as e:
    print(f"Error durante el análisis: {e}")
