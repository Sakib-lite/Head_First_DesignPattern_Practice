from abc import ABC, abstractmethod


# Target interface that we want to adapt to
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass


# Advanced media players with incompatible interfaces
class Mp4Player:
    def play_mp4(self, file_name: str):
        print(f"Playing MP4 file: {file_name}")


class VlcPlayer:
    def play_vlc(self, file_name: str):
        print(f"Playing VLC file: {file_name}")


# Adapter to integrate AdvancedMediaPlayer with MediaPlayer
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: str):
        if audio_type.lower() == "vlc":
            self.advanced_player = VlcPlayer()
        elif audio_type.lower() == "mp4":
            self.advanced_player = Mp4Player()
        else:
            self.advanced_player = None

    def play(self, audio_type: str, file_name: str):
        if isinstance(self.advanced_player, VlcPlayer):
            self.advanced_player.play_vlc(file_name)
        elif isinstance(self.advanced_player, Mp4Player):
            self.advanced_player.play_mp4(file_name)


# Client class that uses MediaAdapter to handle various formats
class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "mp3":
            print(f"Playing MP3 file: {file_name}")
        elif audio_type.lower() in ["vlc", "mp4"]:
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, file_name)
        else:
            print(f"Invalid media type: {audio_type}. MP3, VLC, and MP4 formats supported.")


# Client code
if __name__ == "__main__":
    player = AudioPlayer()
    player.play("mp3", "song.mp3")
    player.play("mp4", "video.mp4")
    player.play("vlc", "movie.vlc")
    player.play("avi", "clip.avi")
