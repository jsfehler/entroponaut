import renpy.exports as renpy
from renpy.store import config, DictEquality, Hide
from renpy.ui import Action

"""renpy
init python:
"""
def input_confirm_screen(
    message: str,
    yes: list[Action] | None = None,
    no: list[Action] | None = None,
    input_action: Action = None,
) -> None:
    """Show the `input_confirm` screen."""
    screen = 'input_confirm'

    default_yes: list[Action] = [
        Hide(screen, transition=config.exit_yesno_transition),
    ]

    default_no: list[Action] = [
        Hide(screen, transition=config.exit_yesno_transition),
    ]

    yes_actions = default_yes
    if yes:
        yes_actions = [*default_yes, *yes]

    no_actions = default_no
    if no:
        no_actions = [*default_no, *no]

    if config.enter_yesno_transition:
        renpy.transition(config.enter_yesno_transition)

    renpy.show_screen(
        screen,
        message=message,
        yes_action=yes_actions,
        no_action=no_actions,
        input_action = input_action,
    )

    renpy.restart_interaction()


@renpy.pure
class InputConfirm(Action, DictEquality):
    """
    :doc: other_action

    Prompts the user for confirmation of an action. If the user
    clicks yes, the yes action is performed. Otherwise, the `no`
    action is performed.

    `prompt`
        The prompt to display to the user.

    `confirm_selected`
        If true, the prompt will be displayed even if the `yes` action
        is already selected. If false (the default), the prompt
        will not be displayed if the `yes` action is selected.

    The sensitivity and selectedness of this action match those
    of the `yes` action.

    See :func:`renpy.confirm` for a function version of this action.
    """

    def __init__(
        self,
        prompt: str,
        yes: list[Action],
        no: list[Action] | None = None,
        input_action: Action = None,
        confirm_selected: bool = False,
    ):
        self.prompt = prompt
        self.yes = yes
        self.no = no
        self.input_action = input_action
        self.confirm_selected = confirm_selected

    def __call__(self):
        if self.get_selected() and not self.confirm_selected:
            return renpy.run(self.yes)

        return input_confirm_screen(
            self.prompt,
            self.yes,
            self.no,
            self.input_action,
        )

    def get_sensitive(self) -> bool:
        if self.yes is None:
            return False

        return renpy.is_sensitive(self.yes)

    def get_selected(self) -> bool:
        return renpy.is_selected(self.yes)

    def get_tooltip(self):
        return renpy.display.behavior.get_tooltip(self.yes)
