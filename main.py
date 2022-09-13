def on_button_pressed_a():
    global master_key
    radio.set_group(89)
    master_key = 2
    radio.send_value("m_key", master_key)
    basic.show_string("skickad")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_value(name, value):
    if name == "m_key":
        basic.show_number(value)
radio.on_received_value(on_received_value)

master_key = 0
radio.set_group(89)