from renpy.store import FileLoad, FileSave, FileDelete

"""renpy
init python:
"""
class FileCurrent:
    """Base override class for File Action.

    Uses the items in entroponaut.load_save_hovered_slot_info to determine
    which file to use.
    """
    @property
    def name(self) -> str:
        """Compatibility layer for File Actions.

        Don't access directly, it's slower than calling
        `entroponaut.load_save_hovered_slot_info` directly.
        """
        return entroponaut.load_save_hovered_slot_info['slot_id']

    @property
    def page(self) -> str:
        """Compatibility layer for File Actions.

        Don't access directly, it's slower than calling
        `entroponaut.load_save_hovered_slot_info` directly.
        """
        return entroponaut.load_save_hovered_slot_info['page']

    @classmethod
    def update(cls, **kwargs):
        """Update the external cache."""
        def inner() -> None:
            for k, v in kwargs.items():
                entroponaut.load_save_hovered_slot_info[k] = v
        return inner

    @classmethod
    def revert(cls):
        """Revert the external cache to the previous state."""
        def inner() -> None:
            for k, v in entroponaut.load_save_hovered_slot_info.items():
                entroponaut.load_save_hovered_slot_info[k] = entroponaut.load_save_last_selected_slot_info[k]
            renpy.restart_interaction()
        return inner


class FileLoadCurrent(FileLoad, FileCurrent):
    """Like FileLoad, but for the current file."""
    def __init__(self, confirm: bool = True, newest: bool = True, cycle: bool = False):
        self.confirm = confirm
        self.newest = newest
        self.cycle = cycle

        try:
            self.alt = __(f"Load slot {self.name}: [text]")
        except Exception:
            self.alt = f"Load slot {self.name}: [text]"

    def get_sensitive(self):
        self.slot = entroponaut.load_save_hovered_slot_info['slot']
        return super().get_sensitive()

    def __call__(self) -> None:
        self.slot = entroponaut.load_save_hovered_slot_info['slot']
        super().__call__()


class FileSaveCurrent(FileSave, FileCurrent):
    """Like FileSave, but for the current file."""
    def __init__(
        self,
        confirm: bool = True,
        newest: bool = True,
        cycle: bool = False,
        action=None,
    ):
        self.confirm = confirm
        self.newest = newest
        self.cycle = cycle
        self.action = action

        try:
            self.alt = __(f"Save slot {self.name}: [text]")
        except Exception:
            self.alt = f"Save slot {self.name}: [text]"

    def get_selected(self):
        return False


class FileDeleteCurrent(FileDelete, FileCurrent):
    """Like FileDelete, but for the current file."""

    def __init__(self, confirm: bool = True):
        self.confirm = confirm
