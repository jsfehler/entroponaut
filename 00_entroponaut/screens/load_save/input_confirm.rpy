# Screen for the player to input the name of the save file.
# Basically a confirm screen with an input
screen input_confirm(message, yes_action, no_action, input_action):
    modal True

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

    on "show" action input_action.Toggle()

    dismiss action no_action

    frame:
        style_prefix "confirm"

        xalign 0.5
        yalign 0.5

        vbox:
            spacing 45

            label message:
                style "confirm_prompt"
                xalign 0.5

            frame:
                style "input_confirm_input_frame"
                input:
                    length 20
                    style "file_info_frame_text"
                    value input_action
            hbox:
                xalign 0.5
                spacing 150

                textbutton _("ACCEPT"):
                    hover_sound entroponaut_config.audio.ui.button_hover
                    activate_sound entroponaut_config.audio.ui.button_action
                    action yes_action

                textbutton _("CANCEL"):
                    hover_sound entroponaut_config.audio.ui.button_hover
                    activate_sound entroponaut_config.audio.ui.button_action
                    action no_action
