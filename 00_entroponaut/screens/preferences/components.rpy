screen entroponaut_slider(value=None, changed=None):
    hbox:
        style "preferences_item_slider_hbox"
        add Frame(
            Transform(
                f"{entroponaut_gui.root_directory}/gui/desktop/slider/minus.svg",
                matrixcolor=ColorizeMatrix(gui.accent_color, gui.accent_color),
            ),
            xsize=gui.slider_size,
            ysize=gui.slider_size,
        )
        bar value value changed changed style_suffix "slider"
        add Frame(
            Transform(
                f"{entroponaut_gui.root_directory}/gui/desktop/slider/plus.svg",
                matrixcolor=ColorizeMatrix(gui.accent_color, gui.accent_color),
            ),
            xsize=gui.slider_size,
            ysize=gui.slider_size,
        )

        transclude

screen preference_slider(pref):
    hbox:
        style "preferences_item_slider_hbox"
        add Frame(
            Transform(
                f"{entroponaut_gui.root_directory}/gui/desktop/slider/minus.svg",
                matrixcolor=ColorizeMatrix(gui.accent_color, gui.accent_color),
            ),
            xsize=gui.slider_size,
            ysize=gui.slider_size,
        )
        bar value Preference(pref)
        add Frame(
            Transform(
                f"{entroponaut_gui.root_directory}/gui/desktop/slider/plus.svg",
                matrixcolor=ColorizeMatrix(gui.accent_color, gui.accent_color),
            ),
            xsize=gui.slider_size,
            ysize=gui.slider_size,
        )

        transclude
