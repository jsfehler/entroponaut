"""renpy
init python:
"""
import math

font_phys_size = 19

# The expected physical width of the font.
# With a variable width font this is impossible to predict perfectly,
# so try to get an average.
font_width = 13


@renpy.pure
def get_correct_leng(dialogue: "_NVLEntry", has_items=None) -> int:
    last_dialogue = dialogue[-1]

    line_height: int

    if has_items:
        line_height = entroponaut_gui.menu_height_adjustment * len(has_items)
    else:
        line_height = get_dialogue_size(last_dialogue)

    return line_height


@renpy.pure
def get_dialogue_size(dialogue: "_NVLEntry") -> int:
    """Get number of physical lines this dialogue block takes up.

    Arguments:
        dialogue: Internal Ren'Py tuple sub-class.
    """
    # Can't predict the NVL window size, so calculate dynamically.
    window_size: int = style.nvl_window.xminimum * config.screen_width

    # Estimate how many characters until a line break.
    max_char_per_line = math.floor(window_size / font_width)

    # Get approximate number of lines the text will take up.
    lines_amount = len(dialogue.what) / max_char_per_line

    # Round up because a line of dialogue might be less than 1 full line.
    lines_amount = math.ceil(lines_amount)

    # Get the height of the text block.
    lines_height = lines_amount * entroponaut_gui.menu_height_adjustment

    return lines_height
