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
