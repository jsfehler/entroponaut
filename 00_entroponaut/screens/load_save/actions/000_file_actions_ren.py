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
            renpy.restart_interaction()
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

    @property
    def slot(self) -> str:
        """Compatibility layer for File Actions."""
        return entroponaut.load_save_hovered_slot_info['slot']

    @slot.setter
    def slot(self, new_value):
        pass

    def get_sensitive(self) -> bool:
        if not entroponaut.load_save_last_selected_slot_info['slot_id']:
            return False

        return super().get_sensitive()

    def get_selected(self) -> bool:
        return False


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

    def get_sensitive(self) -> bool:
        if not entroponaut.load_save_last_selected_slot_info['slot_id']:
            return False

        return super().get_sensitive()

    def get_selected(self) -> bool:
        return False


class FileDeleteCurrent(FileDelete, FileCurrent):
    """Like FileDelete, but for the current file."""

    def __init__(self, confirm: bool = True):
        self.confirm = confirm

    @property
    def slot(self) -> str:
        """Compatibility layer for File Actions."""
        return entroponaut.load_save_hovered_slot_info['slot']

    def get_sensitive(self) -> bool:
        if not entroponaut.load_save_last_selected_slot_info['slot_id']:
            return False

        return super().get_sensitive()

    def get_selected(self) -> bool:
        return False


class ClearLastSaveLoadSlotInfo(Action, DictEquality):
    """Clear the record of the last load_save slot that was selected."""
    def __call__(self):
        entroponaut.load_save_last_selected_slot_info = {
            "slot_id": None,
            "page": None,
            "unique_id": "",
            "display_name": "",
            "slot": None,
        }
        renpy.restart_interaction()
