# The Displayables in this file are used for the GUI's various Frames.
# They use solid colours and thus scale easily.

init -2:
    # Ensure these Displayables are created as early as possible.

    # Base colour for the Frame.
    image _solid_base = Solid('#000')

    # Accent colour for the sides of the Frame.
    image _solid_accent = Solid(gui.accent_color)

    image _solid_insensitive = Solid(gui.insensitive_color)

    # The core of the Frame.
    image _frame_core = Frame(
        Transform("_solid_base", alpha=entroponaut_gui.frame_alpha),
    )

###
# Frame with a horizontal stripe on the left and right.
###
image _h_stripe = Transform("_solid_accent", xsize=16)

image _h_frame_base = Composite(
    (100, 100),
    (0, 0), "_h_stripe",
    (16, 0), "_frame_core",
    (84, 0), "_h_stripe",
)

image entroponaut_h_stripe_frame = Frame(
    "_h_frame_base", left=16, right=16, tile=gui.frame_tile,
)

###
# Frame with a vertical stripe on the top and bottom.
###
image _v_stripe = Transform("_solid_accent", ysize=16)

image _v_frame_base = Composite(
    (100, 100),
    (0, 0), "_v_stripe",
    (0, 16), "_frame_core",
    (0, 84), "_v_stripe",
)

image entroponaut_v_stripe_frame = Frame(
    "_v_frame_base", top=16, bottom=16, tile=gui.frame_tile,
)

###
# Boxed Frames
###

# Medium
image _v_stripe_medium = Transform("_solid_accent", ysize=16)
image _h_stripe_medium = Transform("_solid_accent", xsize=16)

image _frame_base_medium = Composite(
    (100, 100),
    (0, 0), "_v_stripe_medium",
    (0, 16), Frame("_solid_base"),
    (0, 84), "_v_stripe_medium",
    (0, 0), "_h_stripe_medium",
    (84, 0), "_h_stripe_medium",
)

image entroponaut_frame_medium = Frame("_frame_base_medium", left=16, top=16, bottom=16, tile=gui.frame_tile)

# Thin
image _v_stripe_thin = Transform("_solid_accent", ysize=4)
image _h_stripe_thin = Transform("_solid_accent", xsize=4)

image _frame_base_thin = Composite(
    (100, 100),
    (0, 0), "_v_stripe_thin",
    (0, 4), Frame("_solid_base"),
    (0, 96), "_v_stripe_thin",
    (0, 0), "_h_stripe_thin",
    (96, 0), "_h_stripe_thin",
)

image entroponaut_frame_thin = Frame("_frame_base_thin", left=4, top=4, bottom=4, tile=gui.frame_tile)

# Extra Thin
image _v_stripe_xthin = Transform("_solid_accent", ysize=2)
image _h_stripe_xthin = Transform("_solid_accent", xsize=2)

image _frame_base_xthin = Composite(
    (100, 100),
    (0, 0), "_v_stripe_xthin",
    (0, 2), Frame("_solid_base"),
    (0, 98), "_v_stripe_xthin",
    (0, 0), "_h_stripe_xthin",
    (98, 0), "_h_stripe_xthin",
)

image entroponaut_frame_xthin = Frame("_frame_base_xthin", left=2, top=2, bottom=2, tile=gui.frame_tile)

# Extra Thin Insensitive
image _v_stripe_xthin_insensitive = Transform("_solid_insensitive", ysize=2)
image _h_stripe_xthin_insensitive = Transform("_solid_insensitive", xsize=2)

image _frame_base_xthin_insensitive = Composite(
    (100, 100),
    (0, 0), "_v_stripe_xthin_insensitive",
    (0, 2), Frame("_solid_base"),
    (0, 98), "_v_stripe_xthin_insensitive",
    (0, 0), "_h_stripe_xthin_insensitive",
    (98, 0), "_h_stripe_xthin_insensitive",
)

image entroponaut_frame_xthin_insensitive = Frame("_frame_base_xthin_insensitive", left=2, top=2, bottom=2, tile=gui.frame_tile)

init -2:
    # Checkbox
    image entroponaut_checkbox_idle = Frame(
        Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/checkbox/idle.svg", matrixcolor=ColorizeMatrix(entroponaut_gui.checkbox_idle_color, entroponaut_gui.checkbox_idle_color)),
        xsize=gui.slider_size, ysize=gui.slider_size,
    )

    image entroponaut_checkbox_hover = Frame(
        Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/checkbox/idle.svg", matrixcolor=ColorizeMatrix(entroponaut_gui.checkbox_hover_color, entroponaut_gui.checkbox_hover_color)),
        xsize=gui.slider_size, ysize=gui.slider_size,
    )

    image entroponaut_checkbox_selected_idle = Frame(
        Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/checkbox/selected_idle.svg", matrixcolor=ColorizeMatrix(entroponaut_gui.checkbox_selected_idle_color, entroponaut_gui.checkbox_selected_idle_color)),
        xsize=gui.slider_size, ysize=gui.slider_size,
    )

    image entroponaut_checkbox_selected_hover = Frame(
        Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/checkbox/selected_idle.svg", matrixcolor=ColorizeMatrix(entroponaut_gui.checkbox_selected_hover_color, entroponaut_gui.checkbox_selected_hover_color)),
        xsize=gui.slider_size, ysize=gui.slider_size,
    )

    # Radio
    image entroponaut_radio_idle = Frame(
        Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/radio/idle.svg", matrixcolor=ColorizeMatrix(entroponaut_gui.radio_idle_color, entroponaut_gui.radio_idle_color)),
        xsize=gui.slider_size, ysize=gui.slider_size,
    )

    image entroponaut_radio_hover = Frame(
        Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/radio/idle.svg", matrixcolor=ColorizeMatrix(entroponaut_gui.radio_hover_color, entroponaut_gui.radio_hover_color)),
        xsize=gui.slider_size, ysize=gui.slider_size,
    )

    image entroponaut_radio_selected_idle = Frame(
        Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/radio/selected_idle.svg", matrixcolor=ColorizeMatrix(entroponaut_gui.radio_selected_idle_color, entroponaut_gui.radio_selected_idle_color)),
        xsize=gui.slider_size, ysize=gui.slider_size,
    )

    image entroponaut_radio_selected_hover = Frame(
        Transform(f"{entroponaut_gui.root_directory}/gui/desktop/button/radio/selected_idle.svg", matrixcolor=ColorizeMatrix(entroponaut_gui.radio_selected_hover_color, entroponaut_gui.radio_selected_hover_color)),
        xsize=gui.slider_size, ysize=gui.slider_size,
    )
