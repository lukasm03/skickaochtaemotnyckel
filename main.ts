input.onButtonPressed(Button.A, function () {
    radio.setGroup(89)
    master_key = 2
    radio.sendValue("m_key", master_key)
    basic.showString("skickad")
})
radio.onReceivedValue(function (name, value) {
    if (name == "m_key") {
        basic.showNumber(value)
    }
})
let master_key = 0
radio.setGroup(89)
