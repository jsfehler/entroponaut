# JSON metadata to pull from a save file and display on the Saveload screen.
# Expected to be a list of (name, variable name) tuples.
# The variables must be present in the save metadata.
# list[Tuple[str, str]]
define entroponaut.load_save_json_metadata_display = []

# Cache of the last selected slot on the save/load screens' variables.
# Dict[str, int]
define entroponaut.load_save_hovered_slot_info = {
    'slot_id': 0,
    'page': 0,
    'slot': 0,
}

# Record the last slot_id used. This allows the saveload buttons to maintain a selected state.
default entroponaut.load_save_last_selected_slot_info = {
    "slot_id": None,
    "page": None,
    "unique_id": "",
    "display_name": "",
    "slot": None,
}

init python:
    def _get_placeholder_save_slot_name():
        return str(entroponaut.load_save_last_selected_slot_info['slot_id'])

    entroponaut.placeholder_save_slot_name_callable = _get_placeholder_save_slot_name

init python in saveload_store:
    min_slots = 9
    # Will always be + 1 for max_slots
    max_slots = 24
    slots_to_show = min_slots
