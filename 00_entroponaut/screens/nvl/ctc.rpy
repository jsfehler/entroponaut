init -1985:
    transform ctc_fade_in:
        alpha 0.0
        pause 5.0
        easein 3.0 alpha 1.0

        block:
            pause 1.0
            easein 3.0 alpha 0.2
            easein 1.0 alpha 1.0
            repeat


define nvl_ctc = ctc_fade_in(child=Text(entroponaut_gui.continue_caret, font="DejaVuSans.ttf"))
