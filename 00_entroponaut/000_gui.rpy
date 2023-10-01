
init -3:
    define entroponaut_gui.root_directory = "00_entroponaut"

# Default settings for buttons
define entroponaut_gui.button_borders = Borders(6, 6, 6, 6)
define entroponaut_gui.button_tile = False
define entroponaut_gui.button_font = f"{entroponaut_gui.root_directory}/fonts/oswald/static/Oswald-ExtraLight.ttf"
define entroponaut_gui.button_font_color = "#b9d8db"

define entroponaut_gui.prompt_font = f"{entroponaut_gui.root_directory}/fonts/oswald/static/Oswald-ExtraLight.ttf"

define entroponaut_gui.label_font = f"{entroponaut_gui.root_directory}/fonts/noto_sans/NotoSans-Bold.ttf"

# Quick menu
define entroponaut_gui.quick_button_font_idle_color = "#b9d8db"
define entroponaut_gui.quick_button_font_hover_color = "#000"

# Navigation buttons
define entroponaut_gui.nav_button_font = f"{entroponaut_gui.root_directory}/fonts/oswald/static/Oswald-Light.ttf"
define entroponaut_gui.nav_button_text_idle_color = "#b9d8db"
define entroponaut_gui.nav_button_text_hover_color = "#000"

# Sliders
define entroponaut_gui.slider_idle_color = "#b9d8db"
define entroponaut_gui.slider_thumb_idle_color = "#b9d8db"

# Save/Load
define entroponaut_gui.save_load_button_font = f"{entroponaut_gui.root_directory}/fonts/noto_sans/NotoSans-Light.ttf"
define entroponaut_gui.save_load_button_font_size = 19

# Save/Load carets
define entroponaut_gui.save_caret = "▼"
define entroponaut_gui.load_caret = "▲"

# Click to Continue caret.
define entroponaut_gui.continue_caret = "►"

# Used as a background for the input_confirm screen.
define entroponaut_gui.input_confirm_background = Solid('#000')

# The expected physical height of the font. Used for scrolling calculations.
define entroponaut_gui.menu_height_adjustment = 26

# The colour used for passive text
define entroponaut_gui.passive_text_colour = "#787878"

define entroponaut_gui.frame_alpha = 0.75

define entroponaut_gui.game_menu_frame_background = Transform(Solid('#000'), alpha=entroponaut_gui.frame_alpha)

init -1150 python in entroponaut_gui:
    from store import config, layout, _preferences, Frame, Null, persistent, Action, DictEquality, gui
    import math

    # The extension used for auto-defined images.
    button_image_extension = ".png"

    def button_properties(kind):
        """
        :doc: gui

        Given a `kind` of button, returns a dictionary giving standard style
        properties for that button. This sets:

        :propref:`background`
            As described below.

        :propref:`padding`
            To gui.kind_borders.padding (if it exists).

        :propref:`xsize`
            To gui.kind_width (if it exists).

        :propref:`ysize`
            To gui.kind_height (if it exists).

        (Note that if `kind` is the string "nvl_button", this will look for
        the gui.nvl_button_background variable.)

        The background is a frame that takes its background picture from
        the first existing one of:

        * gui/button/kind_[prefix\_].background.png
        * gui/button/[prefix\_].background.png

        If a gui variables named gui.kind_borders exists, it's
        used. Otherwise, :var:`gui.button_borders` is used. If gui.kind_tile
        exists, it determines if the borders are tiled, else :var:`gui.button_tile`
        controls tiling.

        For what [prefix\_] means, check out the :ref:`style prefix search <style-prefix-search>`
        documentation.
        """

        g = globals()

        def get(prop):
            if kind + "_" + prop in g:
                return g[kind + "_" + prop]

            return None

        borders = get("borders")

        tile = get("tile")
        if tile is None:
            tile = button_tile

        backgrounds = [ ]

        if kind != "button":
            backgrounds.append(f"{root_directory}/gui/desktop/button/" + kind[:-7] + "_[prefix_]background" + button_image_extension)

        backgrounds.append(f"{root_directory}/gui/desktop/button/[prefix_]background" + button_image_extension)

        if renpy.variant("small"):
            backgrounds = [ i.replace(f"{root_directory}/gui/desktop/button", f"{entroponaut_gui.root_directory}/gui/phone/button") for i in backgrounds ] + backgrounds

        rv = {
            "background" : Frame(backgrounds, borders or button_borders, tile=tile),
        }

        if borders is not None:
            rv["padding"] = borders.padding

        width = get("width")
        height = get("height")

        if width is not None:
            rv["xsize"] = width

        if height is not None:
            rv["ysize"] = height

        return rv
