# Transform used for each item in the navigation menu.
define entroponaut_config.navigation_item_transform = alpha_easein

style narrator_thought is nvl_thought:
    font gui.text_font
    size 19

define narrator = NVLCharacter(
    who_style='nvl_label',
    what_style='narrator_thought',
    window_style='nvl_entry',
    type='nvl',
    mode='nvl',
    clear=False,
    kind=adv,
    ctc=nvl_ctc,
    ctc_position='nestled',
)


define menu = nvl_menu

init python:
    # Remove left click to advance NVL screen.
    config.keymap['dismiss'] = [ 'K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT']

init python:
    config.font_replacement_map[f"{entroponaut_gui.root_directory}/fonts/noto_sans/NotoSans-Regular.ttf", False, True] = (f"{entroponaut_gui.root_directory}/fonts/noto_sans/NotoSans-Bold.ttf", False, False)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define config.nvl_list_length = 12
