from abc import ABC, abstractmethod

# Target interface that our client expects
class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass

# Adaptee classes with incompatible interfaces
class Mp4Player:
    def play_mp4(self, file_name: str):
        print(f"Playing MP4 file: {file_name}")

class VlcPlayer:
    def play_vlc(self, file_name: str):
        print(f"Playing VLC file: {file_name}")

# Adapter class that inherits from both MediaPlayer and adaptees
class Mp4Adapter(MediaPlayer, Mp4Player):
    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "mp4":
            self.play_mp4(file_name)

class VlcAdapter(MediaPlayer, VlcPlayer):
    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "vlc":
            self.play_vlc(file_name)

# Client class that uses adapters for various formats
class AudioPlayer(MediaPlayer):
    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "mp3":
            print(f"Playing MP3 file: {file_name}")
        elif audio_type.lower() == "mp4":
            adapter = Mp4Adapter()
            adapter.play(audio_type, file_name)
        elif audio_type.lower() == "vlc":
            adapter = VlcAdapter()
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
