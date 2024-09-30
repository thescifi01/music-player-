import os
import pygame
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView

# Initialize the pygame mixer for playing music
pygame.mixer.init()

class MusicPlayerApp(App):
    def build(self):
        # Main layout
        self.layout = BoxLayout(orientation='vertical')
        
        # Label to display the song name
        self.song_label = Label(text="Choose a song to play", size_hint=(1, 0.1))
        self.layout.add_widget(self.song_label)
        
        # File chooser to select the music file
        self.filechooser = FileChooserListView(filters=['*.mp3', '*.wav'], size_hint=(1, 0.7))
        self.layout.add_widget(self.filechooser)
        
        # Button layout for Play and Pause buttons
        self.button_layout = BoxLayout(size_hint=(1, 0.2))
        
        # Play button with emoji
        self.play_button = Button(text='>Play', font_size=32)
        self.play_button.bind(on_press=self.play_music)
        self.button_layout.add_widget(self.play_button)
        
        # Pause button with emoji
        self.pause_button = Button(text='•Pause', font_size=32)
        self.pause_button.bind(on_press=self.pause_music)
        self.button_layout.add_widget(self.pause_button)
        
        # Add the button layout to the main layout
        self.layout.add_widget(self.button_layout)
        
        return self.layout
    
    def play_music(self, instance):
        # Check if a file is selected
        selected = self.filechooser.selection
        if selected:
            song_path = selected[0]
            self.song_label.text = f"Playing: {os.path.basename(song_path)}"
            # Load and play the selected music
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
    
    def pause_music(self, instance):
        # Pause the music if it's playing
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.song_label.text = "Music Paused"

if __name__ == '__main__':
    MusicPlayerApp().run()
