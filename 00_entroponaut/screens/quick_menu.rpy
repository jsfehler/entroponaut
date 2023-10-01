## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        frame:
            style_prefix "quick"
            vbox:
                style_prefix "quick"

                textbutton _("REWIND") action Rollback()
                textbutton _("SKIP") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("AUTO") action Preference("auto-forward", "toggle")
                textbutton _("SAVE") action ShowMenu('save')
                textbutton _("Q.SAVE") action QuickSave()
                textbutton _("Q.LOAD") action QuickLoad()
                textbutton _("OPTIONS") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties entroponaut_gui.button_properties("quick_button")
    hover_background gui.accent_color
    selected_background gui.hover_color
    xfill True
    left_padding 12
    right_padding 6

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    idle_color entroponaut_gui.quick_button_font_idle_color
    hover_color entroponaut_gui.quick_button_font_hover_color
    selected_color entroponaut_gui.quick_button_font_hover_color
    xalign 1.0

style quick_frame:
    background None
    yalign 0.9
    xpos 0.62
    xanchor 1.0
    xsize 0.07
