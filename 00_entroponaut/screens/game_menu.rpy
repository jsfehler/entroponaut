## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

transform from_left:
    xsize 0.0
    easein 0.5 xsize 1.0

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame at increase_xzoom:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing 16
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:
                    vbox:
                        spacing 16
                        transclude

    use navigation

    frame:
        style "return_button_frame"

        use game_menu_navigation_buttons

    frame at increase_xzoom:
        style "game_menu_title_frame"
        label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

# Buttons that only appear on the game menu.
screen game_menu_navigation_buttons():
    vbox:
        textbutton _("RETURN"):
            style "return_button"

            action Return()

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    background entroponaut_gui.game_menu_frame_background
    xpos 0.30
    xsize 0.5
    bottom_padding 45
    top_padding 180

style game_menu_content_frame:
    xsize 1.0
    right_margin 40
    left_margin 40
    top_margin 15
    yfill True

style game_menu_viewport

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_title_frame:
    background Solid(gui.accent_color)
    xanchor 0.0
    xpos 0.29
    ysize 100
    ypos 0.05
    padding (36, 0, 36, 0)

style game_menu_label

style game_menu_label_text:
    yalign 0.5
    size gui.title_text_size
    color "#000"
    font f"{entroponaut_gui.root_directory}/fonts/noto_sans/NotoSans-Black.ttf"

style return_button_frame is navigation_frame:
    background None
    ypos 0.8

style return_button:
    yalign 1.0
