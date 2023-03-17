from guizero import App, Text, ButtonGroup, PushButton, Picture

def desc():
    if joke_choice.value == "Richard Stallman":
        display_joke.value = "Creator of the FSF and the GNU Project."
    elif joke_choice.value == "Linus Torvalds":
      display_joke.value = "Creator of the Linux Kernel and the Git VCS."
    elif joke_choice.value == "Lennart Poettering":
      display_joke.value = "Creator of Pulseaudio and systemd."

app = App()
HEADER = Text(app, text="Choose a software engineer...")
display_joke = Text(app, text="Waiting for a Joke Choice...")
joke_choice = ButtonGroup(app, options=["Richard Stallman", "Linus Torvalds", "Lennart Poettering"], selected="Richard Stallman", command=desc)

funnybutton1 = PushButton(app, text="DO NOT PRESS!", command=app.destroy, width="30", height="6")
display_joke = Text(app)
funnybutton1.bg = "red"
funnybutton1.text_color = "white"
stallman = Picture(app, image="rms.png")

app.display()
