style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text

style slot_time_text is slot_button_text:
    size entroponaut_gui.save_load_button_font_size
    font entroponaut_gui.save_load_button_font
    hover_color "#000"

style slot_name_text is slot_button_text:
    size entroponaut_gui.save_load_button_font_size
    font entroponaut_gui.save_load_button_font
    hover_color "#000"

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties entroponaut_gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties entroponaut_gui.button_properties("slot_button")
    padding (0, 0, 0, 0)
    background "entroponaut_frame_xthin"
    hover_background Solid(gui.accent_color)
    selected_background Solid(gui.accent_color)

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    font entroponaut_gui.button_font

style file_info_slot_name_button:
    background None
    xsize config.thumbnail_width
    ysize 28
    ypos -6
    xpos -6
    padding (6, 0, 0, 0)

style file_info_slot_name_button_text:
    font entroponaut_gui.button_font
    yalign 0.5
    size entroponaut_gui.save_load_button_font_size + 3

style entroponaut_save_slot_label:
    xalign 0.5

style entroponaut_save_slot_header_frame:
    background None
    padding (4, 4, 4, 4)

style file_info_frame_text:
    xalign 0.5
    yalign 0.5
    size gui.text_size
    font entroponaut_gui.save_load_button_font
    caret "input_confirm_caret"

style slot_button_hbox_frame:
    background None
    padding (4, 4, 4, 4)

style confirm_button_caret is confirm_button_text:
    font "DejaVuSans.ttf"

style input_confirm_input_frame:
    background entroponaut_gui.input_confirm_background
    xsize 0.24
    padding (0, 0, 0, 0)
    margin (0, 0, 0, 0)
