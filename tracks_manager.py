from typing import Dict, List, Optional
import numpy as np

from audio_manager import create_mix
from audio_player import play_loop, stop_playing


class Track:
    def __init__(self, index: int, data: np.ndarray, active: bool = True):
        self.index = index
        self.data = data
        self.active = active

    def toggle(self):
        self.active = not self.active

    def is_active(self) -> bool:
        return self.active


class TrackManager:
    def __init__(self):
        self.sample_rate: int = None
        self.tracks: Dict[int, Track] = {}
        self.active_mix: Optional[np.ndarray] = None

    def set_track(
        self, index: int, audio_data: np.ndarray, sample_rate: int, active: bool = True
    ):
        if self.sample_rate is None:
            self.sample_rate = sample_rate
        elif self.sample_rate != sample_rate:
            raise ValueError(
                f"Sample rate mismatch: expected {self.sample_rate}, got {sample_rate}"
            )

        self.tracks[index] = Track(index, audio_data, active)
        self.mix_active_tracks()

    def toggle_track(self, index: int):
        if index in self.tracks:
            self.tracks[index].toggle()
            self.mix_active_tracks()

    def is_active(self, index: int) -> bool:
        return self.tracks.get(
            index, Track(index, data=np.array([]), active=False)
        ).is_active()

    def get_active_tracks(self) -> Dict[int, np.ndarray]:
        """Retourne une liste de tracks actives."""
        return [i for i, track in self.tracks.items() if track.is_active()]

    def mix_active_tracks(self):
        # Mix all active tracks into a single array
        actives_tacks = [track for track in self.tracks.values() if track.is_active()]
        print("Active tracks:", [track.index for track in actives_tacks])
        self.active_mix = create_mix([track.data for track in actives_tacks])
        if self.active_mix is None:
            stop_playing()
        else:
            play_loop(self.active_mix, self.sample_rate)


# Exemple d'utilisation
def main():
    track_manager = TrackManager()
    track_manager.set_track(3, np.array([30, 31, 32]))
    track_manager.set_track(
        0,
        np.array([0, 1, 2]),
    )

    # L’index 2 est vide pour l’instant
    print("Track 2 active ?", track_manager.is_active(2))  # False

    # Afficher les tracks actives et le mix actif
    print("Pistes actives :", track_manager.get_active_tracks())  # [3, 0]
    print("Active mix", track_manager.active_mix)

    # Toggle track 0
    track_manager.toggle_track(0)

    # Afficher les tracks actives et le mix actif
    print("Pistes actives :", track_manager.get_active_tracks())  # [3, 0]
    print("Active mix", track_manager.active_mix)


if __name__ == "__main__":
    main()
