radio.set_group(123)
music.play_melody("", 120)
def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)
radio.send_string(":D")
def on_received_string(receivedString):
    pass
radio.on_received_string(on_received_string)
basic.show_string(":D!")