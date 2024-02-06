screen slot_button_hbox(slot_id, slot_number, page=None, slot=False, slot_display_name=""):
    hbox:
        yalign 0.5
        spacing 12

        frame:
            style "slot_button_hbox_frame"
            xsize 40
            ysize 40
            if slot_number:
                text str(slot_number) xalign 0.5 yalign 0.5 style "slot_time_text"

        frame:
            style "slot_button_hbox_frame"
            xsize 406
            hbox:
                text slot_display_name or FileSaveName(slot_id, page=page, slot=slot, empty=_("---")) xalign 0.0:
                    style "slot_name_text"

        frame:
            style "slot_button_hbox_frame"
            xsize 120
            text FileTime(slot_id, page=page, slot=slot, format=_("{#file_time}%Y-%m-%d"), empty=_("---")):
                style "slot_time_text"
                xalign 0.5

        frame:
            style "slot_button_hbox_frame"
            xsize 120
            text FileTime(slot_id, page=page, slot=slot, format=_("%H:%M"), empty="---"):
                style "slot_time_text"
                xalign 1.0

        key "save_delete" action FileDelete(slot_id, page=page, slot=slot)


screen slot_button_any(slot_id, slot_number=None, page=1, slot=False, action_type=None, slot_display_name=""):
    default unique_id = f"{slot_id}_{page}"

    button:
        id f"saveload_button_{unique_id}"
        style "slot_button"

        # Allows each slot button to know if it should be in a selected state or not.
        action [
            SelectedIf( (entroponaut.load_save_last_selected_slot_info['unique_id'] == unique_id) ),
            SetVariable(
                "entroponaut.load_save_last_selected_slot_info", {
                    "slot_id": slot_id,
                    "page": page,
                    "unique_id": unique_id,
                    "display_name": "",
                    "slot": slot,
                },
            ),
            SetVariable('save_name', ''),
            FileCurrent.update(slot_id=slot_id, page=page, slot=slot),
            If(
                (entroponaut.load_save_last_selected_slot_info['unique_id'] != unique_id),
                Play('sound', entroponaut_config.audio.ui.loadsave_slot_action),
            ),
        ]
        hovered [
            FileCurrent.update(slot_id=slot_id, page=page, slot=slot),
            Queue('sound', entroponaut_config.audio.ui.loadsave_slot_hover),
            ]
        # on unhovered, if the visible slot is not the select slot, revert to selected slot
        unhovered [
            If(
                (entroponaut.load_save_last_selected_slot_info['unique_id'] != unique_id),
                FileCurrent.revert(),
            ),
        ]

        use slot_button_hbox(slot_id=slot_id, slot_number=slot_number, page=page)

# Slot button that will be disabled when the load_save screen is being used for saving.
screen slot_button_load(slot_id, slot_number=None, page=None, slot=False, action_type=None, slot_display_name="", focus=None):
    default unique_id = f"{slot_id}_{page}"

    button:
        id f"saveload_button_{unique_id}"
        style "slot_button"
        focus focus

        if action_type == 'save':
            at transform:
                alpha 0.5

        if action_type == 'load':
            action [
                SelectedIf( (entroponaut.load_save_last_selected_slot_info['unique_id'] == unique_id) ),
                SetVariable(
                    "entroponaut.load_save_last_selected_slot_info", {
                        "slot_id": slot_id,
                        "page": page,
                        "unique_id": unique_id,
                        "display_name": slot_display_name,
                        "slot": slot,
                    },
                ),
                FileCurrent.update(slot_id=slot_id, page=page, slot=slot),
                If(
                    (entroponaut.load_save_last_selected_slot_info['unique_id'] != unique_id),
                    Play('sound', entroponaut_config.audio.ui.loadsave_slot_action),
                ),
            ]
            hovered [
                FileCurrent.update(slot_id=slot_id, page=page, slot=slot),
                Queue('sound', entroponaut_config.audio.ui.loadsave_slot_hover),
            ]
            # on unhovered, if the visible slot is not the select slot, revert to selected slot
            unhovered [
                If(
                    (entroponaut.load_save_last_selected_slot_info['unique_id'] != unique_id),
                    FileCurrent.revert(),
                ),
            ]

        default _slot_display_name = slot_display_name or FileSaveName(slot_id, page=page, slot=slot)
        use slot_button_hbox(slot_id=slot_id, slot_number=slot_number, slot=slot, page=page, slot_display_name=_slot_display_name)
