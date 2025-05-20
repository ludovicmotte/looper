import sounddevice as sd
import soundfile as sf
import numpy as np
from typing import List, Tuple


def read_audio_files(audio_files_paths: List[str]) -> Tuple[List[np.ndarray], int]:
    """
    Read multiple audio files and ensure they all have the same sample rate.

    Args:
        audio_files_paths: A list of audio file paths.

    Returns:
        Tuple containing:
            - List of audio data arrays (2D: frames x channels)
            - Common sample rate (int)

    Raises:
        ValueError: If files have different sample rates.
    """
    audio_data = []
    sample_rate = None

    for file_path in audio_files_paths:
        data, current_sample_rate = sf.read(file_path, dtype='float32', always_2d=True)

        if sample_rate is None:
            sample_rate = current_sample_rate
        elif current_sample_rate != sample_rate:
            raise ValueError(
                f"All files must have the same sample rate, but '{file_path}' has {current_sample_rate} Hz "
                f"instead of {sample_rate} Hz."
            )

        audio_data.append(data)

    return audio_data, sample_rate


def align_audio_lengths(audio_data: List[np.ndarray]) -> List[np.ndarray]:
    """
    Pad all audio tracks so they are the same length.

    Args:
        audio_data: List of 2D numpy arrays (frames x channels).

    Returns:
        List of aligned 2D numpy arrays.
    """
    max_length = max(data.shape[0] for data in audio_data)
    aligned_audio = []

    for data in audio_data:
        pad_amount = max_length - data.shape[0]
        if pad_amount > 0:
            data = np.pad(data, ((0, pad_amount), (0, 0)), mode='constant')
        aligned_audio.append(data)

    return aligned_audio


def mix_tracks(tracks: List[np.ndarray]) -> np.ndarray:
    """
    Mix multiple tracks by summing them and normalize the result.

    Args:
        file_paths: A list of audio file paths.

    Returns:
        Normalized mixed audio as a 2D numpy array.
    """
    mix = np.sum(tracks, axis=0)
    peak = np.max(np.abs(mix))

    if peak > 0:
        mix /= peak

    return mix


def play(audio_files_paths: List[str]):
    """
    Play mixed audio files in an infinite loop.

    Args:
        audio_files_paths: A list of audio file paths.

    Returns:
        None
    """
    audio_data, sample_rate = read_audio_files(audio_files_paths)
    aligned_data = align_audio_lengths(audio_data)
    mixed_audio = mix_tracks(aligned_data)

    duration_seconds = mixed_audio.shape[0] / sample_rate
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Total duration of the loop: {duration_seconds:.2f} seconds")

    # Infinite playback loop
    while True:
        sd.play(mixed_audio, sample_rate)
        sd.wait()

def main():
    audio_files_paths = ['beat.wav', 'synth.wav', 'pluck.wav', 'voice.wav']
    play(audio_files_paths)


if __name__ == "__main__":
    main()
