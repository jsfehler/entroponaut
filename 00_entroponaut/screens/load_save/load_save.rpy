## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    # When showing the screen, clear the last selected slot.
    # This makes the assumption that it's better UX to assume:
    # 1. The player doesn't want to save or load the last selected slot.
    # 2. They'll want to select a new slot.
    # 3. They're at risk of accidentially saving over the last selected slot.
    on ["show", "replace"] action ClearLastSaveLoadSlotInfo()

    tag menu

    use file_slots(_("SAVE"))


screen load():
    on ["show", "replace"] action ClearLastSaveLoadSlotInfo()

    tag menu

    use file_slots(_("LOAD"))


screen file_slots(title):
    # Minimum shown slots is min_slots, maximum is max_slots
    # Up to the max, add +1 when the bottom slot is filled
    python:
        saved_games_list = renpy.list_saved_games(regexp="(1-)(.)", fast=True)
        sorted_slots = sorted(saved_games_list, key=lambda x: int(x.split("-")[1]))
        try:
            last_slot = sorted_slots[-1]
            last_slot_number = int(last_slot.split("-")[1])
        except IndexError:
            last_slot_number = 0

        saveload_store.slots_to_show = min(saveload_store.max_slots, max(saveload_store.min_slots, last_slot_number))

        action_type = CurrentScreenName()

        if action_type == 'save':
            file_type_label = _("SAVE")
            file_action_caret = entroponaut_gui.save_caret
        else:
            file_type_label = _("LOAD")
            file_action_caret = entroponaut_gui.load_caret

    use game_menu(title):

        frame:
            style "v_save_load_file_slots_frame"
            background None
            ymaximum 0.9

            vbox:
                xsize 766
                spacing 10

                # File info
                hbox:
                    spacing 16
                    add FileScreenshot(
                        entroponaut.load_save_hovered_slot_info["slot_id"],
                        page=entroponaut.load_save_hovered_slot_info["page"],
                        slot=entroponaut.load_save_hovered_slot_info["slot"],
                        empty=empty_saveload_thumbnail
                    ) xalign 0.5

                    vbox:
                        for metadata in entroponaut.load_save_json_metadata_display:
                            hbox:
                                spacing 16
                                text metadata[0] font gui.interface_text_font
                                text FileJson(
                                    entroponaut.load_save_hovered_slot_info["slot_id"],
                                    metadata[1],
                                    empty="---",
                                    missing="",
                                    page=entroponaut.load_save_hovered_slot_info["page"],
                                    slot=entroponaut.load_save_hovered_slot_info["slot"],
                                ):
                                    style "file_info_frame_text" font gui.interface_text_font

                # Slot header
                frame:
                    background "entroponaut_frame_xthin"

                    hbox:
                        style_prefix "v_preferences_save_slot_header"
                        spacing 12
                        xalign 0.0

                        frame:
                            style "entroponaut_save_slot_header_frame"
                            xsize 40
                            ysize 20

                        frame:
                            style "entroponaut_save_slot_header_frame"
                            xsize 406
                            label _("SLOT") style "entroponaut_save_slot_label" xalign 0.3 text_size 19
                        frame:
                            style "entroponaut_save_slot_header_frame"
                            xsize 120
                            label _("DATE") style "entroponaut_save_slot_label" text_size 19
                        frame:
                            style "entroponaut_save_slot_header_frame"
                            xsize 120
                            label _("TIME") style "entroponaut_save_slot_label" xalign 1.0 text_size 19


                ## The grid of file slots.
                viewport id "manual_save_vp":
                    mousewheel 'vertical'
                    scrollbars "vertical"
                    edgescroll (20, 320)
                    spacing 10

                    # Scrolling via keyboard/gamepad is handled automatically.
                    vscrollbar_keyboard_focus False

                    vbox:
                        style_prefix "slot"
                        spacing 6

                        use slot_button_load("quitsave", slot_number='Ex', page="exit", slot=True, action_type=action_type, slot_display_name=_("EXIT SAVE"), focus='load')

                        vbox:
                            spacing 6
                            use slot_button_load(1, slot_number='A', page="auto", action_type=action_type, slot_display_name=_("CURRENT AUTO-SAVE"))
                            use slot_button_load(2, slot_number='A', page="auto", action_type=action_type, slot_display_name=_("PREVIOUS AUTO-SAVE"))

                        for slot in range(1, saveload_store.slots_to_show + 2):
                            python:
                                slot_number = slot
                                #slot_number = ((int(persistent._file_page) - 1) * 3) + slot

                            use slot_button_any(slot, slot_number, page=persistent._file_page, action_type=action_type)

        hbox:
            xalign 0.5
            yalign 0.96
            spacing 4
            xsize config.thumbnail_width

            # Set save_name to ensure the save file gets the name in the input
            button:
                hbox:
                    spacing 12
                    text file_type_label style "confirm_button_text"
                    text file_action_caret style "confirm_button_caret"

                hover_sound entroponaut_config.audio.ui.button_hover
                activate_sound entroponaut_config.audio.ui.button_action
                action [
                    If(
                        action_type == 'load',
                        true=FileLoadCurrent(),
                        false=InputConfirm(
                            prompt=_("Confirm Save Slot Name"),
                            yes=[FileSaveCurrent()],
                            input_action=SaveNameOrPlaceholderInputValue(
                                default=False,
                            ),
                        )
                    ),
                ] xalign 0.0 style "confirm_button"

            textbutton _("DELETE SELECTED"):
                hover_sound entroponaut_config.audio.ui.button_hover
                activate_sound entroponaut_config.audio.ui.delete_file_button_action
                action FileDeleteCurrent()
                xalign 1.0 style "confirm_button"
