################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True
    hover_color gui.accent_color
    font gui.text_font

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties entroponaut_gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame(f"{entroponaut_gui.root_directory}/gui/desktop/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame(f"{entroponaut_gui.root_directory}/gui/desktop/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame(f"{entroponaut_gui.root_directory}/gui/desktop/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame(f"{entroponaut_gui.root_directory}/gui/desktop/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame(f"{entroponaut_gui.root_directory}/gui/desktop/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame(f"{entroponaut_gui.root_directory}/gui/desktop/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame(
        Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/scrollbar/idle_vbar.svg",
            matrixcolor=ColorizeMatrix(entroponaut_gui.slider_idle_color, entroponaut_gui.slider_idle_color),
        ),
        left=2,
        right=2,
    )
    hover_base_bar Frame(
        Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/scrollbar/idle_vbar.svg",
            matrixcolor=ColorizeMatrix(entroponaut_gui.slider_hover_color, entroponaut_gui.slider_hover_color),
        ),
        left=2,
        right=2,
    )
    thumb Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/scrollbar/idle_thumb.svg",
            matrixcolor=ColorizeMatrix(entroponaut_gui.slider_thumb_idle_color, entroponaut_gui.slider_thumb_idle_color),
        xsize=gui.scrollbar_size,
        ysize=gui.scrollbar_size,
    )

    hover_thumb Transform(
        f"{entroponaut_gui.root_directory}/gui/desktop/scrollbar/idle_thumb.svg",
        matrixcolor=ColorizeMatrix(entroponaut_gui.slider_thumb_hover_color, entroponaut_gui.slider_thumb_hover_color),
        xsize=gui.scrollbar_size,
        ysize=gui.scrollbar_size,
    )

    thumb_offset gui.scrollbar_size / 2

    top_gutter gui.scrollbar_size / 2
    bottom_gutter gui.scrollbar_size / 2

style slider:
    xsize 535
    ysize gui.slider_size
    base_bar Frame(
        Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/slider/horizontal_idle_bar.svg",
            matrixcolor=ColorizeMatrix(entroponaut_gui.slider_idle_color, entroponaut_gui.slider_idle_color)),
        gui.slider_borders,
        tile=gui.slider_tile,
    )
    hover_base_bar Frame(
        Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/slider/horizontal_idle_bar.svg",
            matrixcolor=ColorizeMatrix(entroponaut_gui.slider_hover_color, entroponaut_gui.slider_hover_color)),
        gui.slider_borders,
        tile=gui.slider_tile,
    )

    thumb Frame(
        Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/slider/horizontal_idle_thumb.svg",
            matrixcolor=ColorizeMatrix(entroponaut_gui.slider_idle_color, entroponaut_gui.slider_thumb_idle_color),
        ),
        xsize=gui.slider_size,
        ysize=gui.slider_size,
    )

    hover_thumb Frame(
        Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/slider/horizontal_idle_thumb.svg",
            matrixcolor=ColorizeMatrix(entroponaut_gui.slider_thumb_hover_color, entroponaut_gui.slider_thumb_hover_color),
        ),
        xsize=gui.slider_size,
        ysize=gui.slider_size,
    )

    thumb_offset gui.slider_size / 2

    left_gutter gui.slider_size / 2
    right_gutter gui.slider_size / 2

style vslider:
    xsize gui.slider_size
    base_bar Frame(f"{entroponaut_gui.root_directory}/gui/desktop/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)

    thumb Frame(
        Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/slider/vertical_idle_thumb.svg",
            matrixcolor=ColorizeMatrix("#0066cc", "#0066cc"),
        ),
        xsize=gui.slider_size,
        ysize=gui.slider_size,
    )

    hover_thumb Frame(
        Transform(
            f"{entroponaut_gui.root_directory}/gui/desktop/slider/vertical_idle_thumb.svg",
            matrixcolor=ColorizeMatrix("#66a3e0", "#66a3e0"),
        ),
        xsize=gui.slider_size,
        ysize=gui.slider_size,
    )

    thumb_offset gui.slider_size / 2

    left_gutter gui.slider_size / 2
    right_gutter gui.slider_size / 2

style frame:
    padding gui.frame_borders.padding
    background "entroponaut_v_stripe_frame"
