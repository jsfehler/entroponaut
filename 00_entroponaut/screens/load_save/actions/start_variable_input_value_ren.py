import renpy.exports as renpy
from renpy.store import FieldEquality, InputValue

"""renpy
init python:
"""
@renpy.pure
class StartVariableInputValue(InputValue, FieldEquality):
    """An input value where a starting value can be specified.
    """

    identity_fields = [ ]
    equality_fields = [ "variable", "returnable" ]

    def __init__(
        self,
        variable: str,
        default: bool = True,
        returnable: bool = False,
        start_value: str = None,
    ):
        self.variable = variable

        self.default = default
        self.returnable = returnable

        self.start_value = start_value

        # Store the last text entered by the user.
        # This lets us track if the user has changed the default value.
        self.current_input = None

    def get_text(self):
        rv = ''

        if self.current_input is None:
            rv = self.start_value

            # If no user input, set default_value
            _set_field(store, self.variable, self.start_value, "variable")

        else:
            rv = _get_field(store, self.variable, "variable")

        return rv

    def set_text(self, s):
        self.current_input = s
        _set_field(store, self.variable, s, "variable")
        renpy.restart_interaction()

    def enter(self):
        renpy.run(self.Disable())
        raise renpy.IgnoreEvent()


class SaveNameOrPlaceholderInputValue(StartVariableInputValue):
    def __init__(self, default: bool = True, returnable: bool = False):
        self.variable = 'save_name'
        self.default = default
        self.returnable = returnable

        self._start_value = ''

        self.current_input = None

    @property
    def start_value(self):
        return self._start_value

    @start_value.getter
    def start_value(self):
        save_name = FileSaveName(
            entroponaut.load_save_hovered_slot_info["slot_id"],
            page=entroponaut.load_save_hovered_slot_info["page"],
            slot=entroponaut.load_save_hovered_slot_info["slot"],
        )

        return save_name or entroponaut.placeholder_save_slot_name_callable()
