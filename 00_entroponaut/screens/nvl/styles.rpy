style nvl_window is default:
    background "entroponaut_h_stripe_frame"
    xfill False
    xsize 0.30
    xpos 0.925
    xanchor 1.0
    padding Borders(40, 0, 40, 60).padding

style nvl_viewport is viewport:
    yfill True

style nvl_viewport_vbox:
    spacing 32

style nvl_entry is default:
    xfill True

style nvl_label:
    ypos 0
    yanchor 0.0
    kerning 2
    size 18
    outlines [ ( 0, "#000", 1, 1) ]

style nvl_dialogue is say_dialogue:
    xpos 0.05
    xalign 0.0
    yalign 0.0
    outlines [ ( 0, "#000", 1, 1) ]

style nvl_what_frame:
    background None
    xfill True
    padding (0, 0, 40, 0)

style nvl_thought:
    xalign 0.0

style nvl_button is button:
    xalign 0.0
    xpos 10

style nvl_break_button:
    background Solid(gui.accent_color)
    ysize 48
    xsize 1.0
    xalign 0.5
    left_padding 24
    bottom_padding 0
    top_padding 12

style nvl_break_button_text:
    xalign 0.8
    yalign 0.5
    size 32
    font entroponaut_gui.button_font
    color entroponaut_gui.button_font_color
    hover_color "#000"
    outlines [ ( 0, "#000", 1, 1) ]
    hover_outlines [ ( 0, gui.accent_color, 1, 1) ]
    bold False

style nvl_break_button_caret is nvl_break_button_text:
    font "DejaVuSans.ttf"
    size 26
    yalign 0.5


style choice_menu_text:
    font gui.text_font
    color gui.accent_color
    hover_color "#FFF"
    xalign 0.5
