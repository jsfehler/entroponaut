################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    frame at yanchor_easein(0.22):
        style_prefix "navigation"

        vbox:
            if main_menu:

                $ last_save = renpy.newest_slot()
                if last_save is not None:
                    textbutton _("CONTINUE") action FileLoad(last_save, slot=True) at entroponaut_config.navigation_item_transform(0.36)

                textbutton _("START") action Start() at entroponaut_config.navigation_item_transform(0.36)

            else:

                textbutton _("HISTORY") action ShowMenu("history") at entroponaut_config.navigation_item_transform(0.36)

                textbutton _("SAVE") action ShowMenu("save") at entroponaut_config.navigation_item_transform(0.36)

            textbutton _("LOAD") action ShowMenu("load") at entroponaut_config.navigation_item_transform(0.36)

            textbutton _("OPTIONS") action ShowMenu("preferences") at entroponaut_config.navigation_item_transform(0.36)

            if _in_replay:

                textbutton _("END REPLAY") action EndReplay(confirm=True) at entroponaut_config.navigation_item_transform(0.36)

            elif not main_menu:

                textbutton _("MAIN MENU") action MainMenu() at entroponaut_config.navigation_item_transform(0.36)

            textbutton _("ABOUT") action ShowMenu("about") at entroponaut_config.navigation_item_transform(0.36)

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("HELP") action ShowMenu("help") at entroponaut_config.navigation_item_transform(0.36)

            if renpy.variant("pc"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("QUIT") action Quit(confirm=not main_menu) at entroponaut_config.navigation_item_transform(0.36)


style navigation_frame:
    background "entroponaut_h_stripe_frame"

    padding (30, 0, 0, 0)

    xpos 0.075
    xsize 0.22

    yfill True

style navigation_vbox:
    yalign 0.5

    xfill True

    spacing gui.navigation_spacing

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties entroponaut_gui.button_properties("navigation_button")
    hover_background gui.accent_color
    selected_idle_background gui.accent_color

    xfill True

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font entroponaut_gui.nav_button_font
    color entroponaut_gui.nav_button_text_idle_color
    hover_color entroponaut_gui.nav_button_text_hover_color
