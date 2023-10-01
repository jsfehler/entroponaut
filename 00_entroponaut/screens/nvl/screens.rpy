# Args:
## ctc: Use nvl_break_item instead of nvl_menu_item.
## ctc_caret: Add a caret after the ctc.
screen nvl(dialogue, items=None, ctc=False, ctc_caret=''):
    window:
        id "nvl_window_id"
        style "nvl_window"

        # Animate the size adjustment
        # xsize animated_xsize

        # A transparent button over the text.
        # Only allow clicks inside the viewport to move advance the text.
        button:
            if not items:
                action Return()

        viewport:
            yinitial 1.0  # vertical offset of the viewport.

            scrollbars "vertical"
            side_yfill True
            style "nvl_viewport"

            vbox:
                style "nvl_viewport_vbox"
                use nvl_dialogue(dialogue, has_items=items):

                    ## Displays the menu, if given. The menu may be displayed incorrectly if
                    ## config.narrator_menu is set to True, as it is above.
                    if items:
                        default l_items = len(items)

                        vbox:
                            spacing 6
                            for idx, i in enumerate(items):
                                if ctc:
                                    use nvl_break_item(
                                        i.caption,
                                        ctc_caret,
                                        i.action,
                                        l_items,
                                    )
                                else:
                                    use nvl_menu_item(
                                        idx,
                                        i.caption,
                                        i.action,
                                        l_items,
                                    )

                            null height 6

screen nvl_menu_item(idx, item_text, action, l_items):
    $ item_number = str(idx + 1)
    $ duration = 1.0 - (l_items / 10)

    hbox:
        text "[item_number]. -" yalign 0.5

        button:
            text "[item_text]" style "choice_menu_text"

            action action
        at slide_up(
            leng=entroponaut_gui.menu_height_adjustment * l_items,
            duration=duration,
        )


screen nvl_break_item(button_text, button_caret, action, l_items):
    $ duration = 1.0 - (l_items / 10)

    button:
        style "nvl_break_button"
        hbox:
            yalign 1.0
            spacing 18
            text button_text style "nvl_break_button_text"
            text button_caret style "nvl_break_button_caret"

        action action
        at slide_up(
            leng=entroponaut_gui.menu_height_adjustment * l_items,
            duration=duration,
        )


screen nvl_dialogue(dialogue, has_items=None):
    python:
        # When a block of dialogue is added to the bottom of the viewport,
        # every entry is pushed up by the amount added.
        # To create a "slide up" effect:
        # 1. Move all the text down such that it looks like nothing moved
        # 2. Slide the text up to where it should be.
        if dialogue:
            leng = get_correct_leng(dialogue, has_items)
        else:
            leng = 48

        # The longer the text, the less time it takes to appear.
        # This prevents large blocks from appearing too slowly compared to
        # smaller blocks.
        if has_items:
            duration = 1.0 - (len(has_items) / 10)

        elif dialogue:
            duration = 1.0 - ( len(dialogue) / (10 + len(dialogue)) )

        else:
            duration = 1.0

    # Padding when the amount of text doesn't fill up viewport.
    # Prevents animation bugs.
    frame:
        background None

        if len(dialogue) > 1:
            at slide_up(leng=leng, duration=duration)

        #id dialogue[0].window_id

        ysize config.screen_height - leng

    for d in dialogue:
        frame:
            # Only apply animation when more than 1 dialogue item.
            if len(dialogue) > 1:
                # Scenario: Text isn't the latest, no alpha anim.
                if not d.current:
                    at slide_up(leng=leng, duration=duration)

                # Scenario: No menu items, add alpha anim on latest text.
                elif d.current and not has_items:
                    at slide_up(leng=leng, duration=duration), alpha_easein(1.0)

                # Scenario: Menu items, no alpha anim.
                elif d.current and has_items:
                    at slide_up(leng=leng, duration=duration)

            id d.window_id
            vbox:
                spacing 10

                if d.who is not None:

                    text d.who:
                        id d.who_id

                frame:
                    style "nvl_what_frame"
                    text d.what:
                        id d.what_id

    transclude
