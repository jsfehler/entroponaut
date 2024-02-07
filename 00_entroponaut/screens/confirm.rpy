## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add f"{entroponaut_gui.root_directory}/gui/desktop/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("CONFIRM") action yes_action
                textbutton _("CANCEL") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background "entroponaut_v_stripe_frame"
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    font entroponaut_gui.prompt_font
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties entroponaut_gui.button_properties("confirm_button")
    background Solid(gui.accent_color)
    hover_background Solid(gui.hover_color)
    insensitive_background Solid(gui.insensitive_color)

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")
    size 24
    font entroponaut_gui.button_font
    outlines [ ( 0, "#000", 1, 1) ]
    bold False
    color entroponaut_gui.button_font_color
    insensitive_color "#000"
