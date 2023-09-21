import random
import os
import shutil
from pathlib import Path

import torch
import torchaudio
import torch.nn.functional as F


class MelSpectrogram:
    def __init__(
        self,
        sample_rate,
        n_fft=512,
        win_length=400,
        hop_length=160,
        n_mels=80,
    ):
        # Spectrogram parameters
        self.spectrogram = torchaudio.transforms.Spectrogram(
            n_fft=n_fft,
            win_length=win_length,
            hop_length=hop_length,
            power=None,
            return_complex=True,
        )
        self.amplitude_to_db = torchaudio.transforms.AmplitudeToDB()
        self.mel_scale = torchaudio.transforms.MelScale(
            n_mels=n_mels, sample_rate=sample_rate, n_stft=n_fft // 2 + 1
        )

    def __call__(self, audio):
        mel = self.spectrogram(audio)

        # Perform time stretching (SpecAugment)
        apply_specaugment = random.random() < self.specaugment_probability
        if apply_specaugment:
            time_stretch = random.uniform(
                self.specaugment_min_speed, self.specaugment_max_speed
            )
            mel = self.time_stretching(mel, time_stretch)

        # Convert from complex to real domain
        mel = mel.abs().pow(2)

        # Convert to mel scale, convert from amplitude to decibels and
        # normalize over the frequency dimension
        mel = self.mel_scale(mel)
        mel = self.amplitude_to_db(mel)
        mel = F.normalize(mel, dim=1)

        return mel
