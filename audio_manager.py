from typing import List, Tuple
import soundfile as sf
import numpy as np

from debug import log_duration


raw_data: List[np.ndarray] = []
sample_rate: int = None
is_playing: List[bool] = []


def read_audio_file(audio_file_path: str) -> Tuple[np.ndarray, int]:
    """
    Read audio file and return its audio data and sample rate.

    Args:
        audio_files_path: An audio file path.

    Returns:
        Tuple containing:
            - Audio data array (2D: frames x channels)
            - sample rate (int)
    """
    audio_data, sample_rate = sf.read(audio_file_path, dtype="float32", always_2d=True)
    return audio_data, sample_rate


def read_audio_files(audio_file_paths: List[str]) -> Tuple[List[np.ndarray], int]:
    """
    Read multiple audio files, ensure they all have the same sample rate, and return their data.

    Args:
        audio_file_paths: A list of audio file paths.

    Returns:
        Tuple containing:
            - List of audio data arrays (2D: frames x channels)
            - Common sample rate (int)

    Raises:
        ValueError: If files have different sample rates.
    """
    audio_data = []
    sample_rate = None

    for audio_file_path in audio_file_paths:
        current_audio_data, current_sample_rate = read_audio_file(audio_file_path)

        if sample_rate is None:
            sample_rate = current_sample_rate
        elif current_sample_rate != sample_rate:
            raise ValueError(
                f"All files must have the same sample rate, but '{audio_file_path}' has {current_sample_rate} Hz "
                f"instead of {sample_rate} Hz."
            )

        audio_data.append(current_audio_data)

    return audio_data, sample_rate


def align_audio_lengths(audio_data: List[np.ndarray]) -> List[np.ndarray]:
    """
    Pad all audio tracks so they are the same length.

    Args:
        audio_data: List of 2D numpy arrays (frames x channels).

    Returns:
        List of aligned 2D numpy arrays.
    """
    if not audio_data:
        return None

    max_length = max(data.shape[0] for data in audio_data)
    aligned_audio = []

    for data in audio_data:
        pad_amount = max_length - data.shape[0]
        if pad_amount > 0:
            data = np.pad(data, ((0, pad_amount), (0, 0)), mode="constant")
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
    if not tracks:
        return None

    mix = np.sum(tracks, axis=0,)
    mix = mix.astype(np.float64)
    peak = np.max(np.abs(mix))

    if peak > 0:
        mix /= peak

    return mix.astype(np.float32)


def create_mix(raw_data: List[np.ndarray]):
    with log_duration(".....create_mix"):
        if not raw_data:
            return None
        aligned_data = align_audio_lengths(raw_data)
        mixed_audio = mix_tracks(aligned_data)
        return mixed_audio


# Exemple d'utilisation
def main():
    raw_data, sample_rate = read_audio_files(
        [
            "testing/beat.wav",
            "testing/synth.wav",
            "testing/pluck.wav",
            "testing/voice.wav",
        ]
    )
    mixed_audio = create_mix(raw_data)

    print(f"Sample rate: {sample_rate} Hz")
    duration_seconds = mixed_audio.shape[0] / sample_rate
    print(f"Total duration of the loop: {duration_seconds:.2f} seconds")


if __name__ == "__main__":
    main()
