import numpy as np
import wave

# Configurações do arquivo WAV
output_file = "audio_1khz3.wav"
duration = 3  # Duração em segundos
sample_rate = 44100  # Taxa de amostragem em Hz
num_channels = 1  # Número de canais (mono)
num_frames = int(duration * sample_rate)  # Número total de quadros

# Frequência do sinal de áudio
frequency = 1000  # 1 kHz

# Amplitude mínima e máxima em volts
min_amplitude = 0.001  # 1 mV
max_amplitude = 1.0  # 1 V

# Gerando o sinal de áudio
time = np.linspace(0, duration, num_frames)
amplitude = np.linspace(min_amplitude, max_amplitude, num_frames)
audio_signal = amplitude * np.sin(2 * np.pi * frequency * time)

# Convertendo a amplitude de volts para int16
audio_signal_int = np.int16(audio_signal * 32767)

# Abrindo o arquivo WAV para escrita
with wave.open(output_file, 'wb') as wav_file:
    wav_file.setnchannels(num_channels)
    wav_file.setsampwidth(2)  # 2 bytes para int16
    wav_file.setframerate(sample_rate)
    wav_file.writeframes(audio_signal_int.tobytes())
