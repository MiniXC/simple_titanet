import torchaudio

from simple_titanet.models import TitaNet
from simple_titanet.transforms import MelSpectrogram


def prepare_mel(audio, sr=16000):
    if sr != 16000:
        audio = torchaudio.transforms.Resample(sr, 16000)(audio)
    return MelSpectrogram(16000)(audio)
