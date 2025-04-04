from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # List of names to display
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Evan"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create and add labels for each name in the list."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.labels_container.add_widget(label)

DynamicLabelsApp().run()