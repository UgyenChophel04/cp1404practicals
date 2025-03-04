BoxLayout:
    orientation: 'vertical'
    Label:
        text: app.status_text
        font_size: 60
        size_hint_y: 0.2
    BoxLayout:
        orientation: 'horizontal'
        Button:
            text: "Up"
            on_press: app.handle_press(1)
        Button:
            text: "Down"
            on_press: app.handle_press(-1)
    BoxLayout:
        id: names_box
    Label:
        text: "I did this :)"
        size_hint_y: 0.1  # Make the label take up 10% of the vertical space
