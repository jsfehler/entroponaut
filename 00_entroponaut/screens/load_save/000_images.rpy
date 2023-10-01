# Caret for the save slot name input
image input_confirm_caret:
    Text("_")
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.0
    repeat


define empty_saveload_thumbnail = Frame(
    Solid("#000"), xsize=config.thumbnail_width, ysize=config.thumbnail_height,
)
