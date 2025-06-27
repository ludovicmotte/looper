from typing import Dict, List, Optional
import numpy as np

from audio_manager import create_mix
from audio_player import play_loop, stop_playing


class Track:
    def __init__(self, index: int):
        self.index = index
        self.muted = False
        self.data: Optional[np.ndarray] = None

    def __str__(self):
        mute_status = "Muted" if self.muted else "Played"
        data_status = "Data" if self.data is not None else "NoData"
        return f"{mute_status}/{data_status}"

    def __repr__(self):
        return self.__str__()


class TracksManager:
    def __init__(self):
        self.sample_rate: int = 44100  # Default sample rate, can be changed later
        self.tracks: List[Track] = []
        self.current_mix: Optional[np.ndarray] = None
        self.current_track_index: int = -1  # -1 means no track

    def __str__(self):
        return f"->{self.current_track_index} Tracks={self.tracks}"

    def t_plus(self):
        self.current_track_index += 1
        if self.current_track_index > len(self.tracks) - 1:
            self.tracks.append(Track(self.current_track_index))
        print(self)

    def t_minus(self):
        print("t_moins")
        if self.current_track_index > 0:
            self.current_track_index -= 1
        print(self)

    def toggle_mute(self):
        print("toggle_mute")
        current_track = self.tracks[self.current_track_index]
        current_track.muted = True
        self.mix_tracks()
        print(self)

    def set_track_data(self, data: np.ndarray):
        print("set_track_data")
        self.tracks[self.current_track_index].data = data
        self.mix_tracks()
        print(self)

    def mix_tracks(self):
        print("mix_tracks")
        # Mix all non muted tracks into a single array
        all_tracks = [track for track in self.tracks if track.muted is False]
        print("Mix tracks with indexes:", [track.index for track in all_tracks])
        self.current_mix = create_mix(
            [track.data for track in all_tracks if track.data is not None]
        )
        if self.current_mix is None:
            stop_playing()
        else:
            play_loop(self.current_mix, self.sample_rate)


tracks_manager = TracksManager()  # tracks manager instance


# Exemple d'utilisation
def main():

    def print_detailled_state():
        print("Current track index: ", track_manager.current_track_index)
        print("Tracks: ", track_manager.tracks)
        print("Current mix: ", track_manager.current_mix)
        print("")

    track_manager = TracksManager()
    print_detailled_state()

    track_manager.t_plus()
    print_detailled_state()

    track_manager.set_track_data(np.array([0.1, 1], dtype=np.float32))
    print_detailled_state()

    track_manager.t_plus()
    print_detailled_state()

    track_manager.set_track_data(np.array([0.5, 1], dtype=np.float32))
    print_detailled_state()

    track_manager.toggle_mute()
    print_detailled_state()

    track_manager.t_minus()
    print_detailled_state()


if __name__ == "__main__":
    main()
