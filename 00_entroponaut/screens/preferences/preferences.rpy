## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("OPTIONS"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            vbox:
                box_wrap True

                hbox:
                    style_prefix "preferences_item"
                    label _("Text Speed")
                    use preference_slider("text speed")

                hbox:
                    style_prefix "preferences_item"
                    label _("Auto-Forward Time")
                    use preference_slider("auto-forward time")

                null height gui.pref_spacing

                if config.has_music:
                    hbox:
                        style_prefix "preferences_item"
                        label _("Music Volume")
                        use preference_slider("music volume")

                if config.has_sound:
                    hbox:
                        style_prefix "preferences_item"
                        label _("Sound Volume")
                        use preference_slider("sound volume"):
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                if config.has_voice:
                    hbox:
                        style_prefix "preferences_item"
                        label _("Voice Volume")
                        use preference_slider("voice volume"):
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_sound)

                if config.has_music or config.has_sound or config.has_voice:
                    hbox:
                        style_prefix "preferences_item"
                        label _("Mute All")
                        button:
                            action Preference("all mute", "toggle")
                            style_suffix "check"

                use custom_preferences()


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    size 24

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties entroponaut_gui.button_properties("radio_button")
    idle_foreground Frame(Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/radio/idle.svg", matrixcolor=ColorizeMatrix(gui.accent_color, gui.accent_color)), xsize=gui.slider_size, ysize=gui.slider_size)
    hover_foreground Frame(Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/radio/selected_idle.svg", matrixcolor=ColorizeMatrix(gui.hover_color, gui.hover_color)), xsize=gui.slider_size, ysize=gui.slider_size)
    selected_idle_foreground Frame(Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/radio/selected_idle.svg", matrixcolor=ColorizeMatrix(gui.accent_color, gui.accent_color)), xsize=gui.slider_size, ysize=gui.slider_size)
    selected_hover_foreground Frame(Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/radio/selected_idle.svg", matrixcolor=ColorizeMatrix("#FFF", "#FFF")), xsize=gui.slider_size, ysize=gui.slider_size)
    left_padding 64

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    size 24
    yalign 0.5

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties entroponaut_gui.button_properties("check_button")
    idle_foreground entroponaut_checkbox_idle
    hover_foreground entroponaut_checkbox_hover
    selected_idle_foreground entroponaut_checkbox_selected_idle
    selected_hover_foreground entroponaut_checkbox_selected_hover
    left_padding 64

style check_button_text:
    properties gui.button_text_properties("check_button")
    size 24

style slider_slider:
    xsize 525

style slider_button:
    properties entroponaut_gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")
    size 24

style slider_vbox:
    xsize 675
