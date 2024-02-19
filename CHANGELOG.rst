Changelog
=========


[0.1.2] - 2024-02-18
--------------------

Changed
~~~~~~~

- The following styles: `nvl_break_button_text`, `vscrollbar`, `vslider`, `check_button`, `radio_button` now use entroponaut_gui variables for determining colour.

Added
~~~~~

- `entroponaut_gui.checkbox_<state>_color` and `entroponaut_gui.radio_<state>_color` variables have been added to control the color of the checkboxes and radio buttons. Valid states are `idle`, `hover`, `selected_idle`, `selected_hover`.

[0.1.1] - 2024-02-11
--------------------

Changed
~~~~~~~

- Entroponaut is now distributed as a Ren'Py template project.

[0.1.0] - 2024-02-08
--------------------

Fixed
~~~~~

- On the Load/Save screen, the Exit save can now be deleted.
- Init blocks now use a number within the engine's approved range.
- Removed unused styles `v_save_load_file_slots_frame`, `v_choice`, and `v_choice_text`.

Changed
~~~~~~~

- On the Load game screen, slots with no data are insensitive.
- Styling for insensitive state on Load/Save Slot buttons now uses Styles instead of Screen state.
- Background image for insensitive state on Load/Save Slot buttons.

Added
~~~~~

- New Styling for insensitive state on Load/Save/Delete buttons.

[0.0.2] - 2023-11-09
--------------------

Changed
~~~~~~~

- Cleanup Frame construction for easier customisation.

- Tweak Options menu for cleaner display of custom options.

[0.0.1] - 2023-11-01
--------------------

Initial release.
