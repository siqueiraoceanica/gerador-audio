import numpy as np
from scipy.io.wavfile import write

# Parâmetros do arquivo de áudio
sample_rate = 44100  # taxa de amostragem (Hz)
duration = 2  # duração em segundos

# Parâmetros da batida de violão (em Hz)
fundamental_freq = 261.63  # frequência do Dó central
harmonics = [2, 3, 4, 5]  # harmônicos para criar um som de violão mais rico

# Geração da forma de onda
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)  # eixo do tempo
waveform = np.zeros_like(t)

# Adicionando as componentes do acorde (fundamental + harmônicos)
for harmonic in harmonics:
    waveform += np.sin(2 * np.pi * fundamental_freq * harmonic * t) / harmonic

# Normalizando a forma de onda para evitar distorções
waveform /= np.max(np.abs(waveform))

# Convertendo a forma de onda para o formato de 16 bits (int16)
waveform_int = np.int16(waveform * 32767)

# Escrevendo a forma de onda no arquivo .wav
write("acorde_do_maior.wav", sample_rate, waveform_int)
