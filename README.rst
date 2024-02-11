- E N T R O P O N A U T -
=========================

A replacement GUI for a Ren'Py project, designed for the NVL text display format.

Live Demo: https://jsfehler.itch.io/entroponaut

.. list-table:: Features
   :widths: auto
   :header-rows: 1

   * -
     -
   * - .. image:: screenshots/nvl.png
         :width: 240
         :alt: NVL
     - Scrolling text window: The NVL window is enhanced with text that scrolls into view from the bottom.
   * - .. image:: screenshots/passive_statement.png
         :width: 240
         :alt: Passive Statement
     - Passive statement: A new statement called 'passive' darkens text and automatically advances to the next line. Useful for showing menu choices after their selection.
   * - .. image:: screenshots/options.png
         :width: 240
         :alt: Options
     - New Options screen: Rebuilt to allow for the easy addition of custom options.
   * - .. image:: screenshots/set_save_name.png
         :width: 240
         :alt: Set Save Name
     - Played-Defined Save Slot Name: Players can set custom names for their save files.
   * - .. image:: screenshots/save_load.png
         :width: 240
         :alt: Save/Load
     - New load/save screen: Reimagined to better handle user-defined slot names and slot metadata.

Installation
------------

- Download the latest release from `github. <https://github.com/jsfehler/entroponaut/releases/>`_

New Project
~~~~~~~~~~~

The Entroponaut project should be used as a template project.

1 - If open, close the Ren'Py Launcher.

2 - Unzip the release and move the `Entroponaut` folder into your Projects directory.

3 - Open the Ren'Py Launcher, create a new project and select Entroponaut as the template.


Existing Project
~~~~~~~~~~~~~~~~

Entroponaut assumes the following default files and folders are not in a project:

- ``game/gui.rpy``
- ``game/screens.rpy``
- ``game/gui/``

If they are present and unmodified, deleting them is necessary. If they have
been modified then they may require changes to work correctly with Entroponaut.

.. warning::
    When used in an existing project, it's the responsibility of the developer to
    ensure their existing assets and screens are not overwritten or made incompatible.

1 - Unzip the release and place the ``entroponaut_0.1.1/game/00_entroponaut/`` directory into your project's ``game/`` directory.

2 - The default `options.rpy` file also needs minor changes:

The following transitions should be disabled or changed, depending on your game.

.. code-block:: console

    # define config.window_show_transition = Dissolve(.2)
    # define config.window_hide_transition = Dissolve(.2)

The window icon must be changed, if you don't have your own:

.. code-block:: console

    define config.window_icon = f"{entroponaut_gui.root_directory}/gui/window_icon.svg"

Usage
-----

To enable the `Exit Save <https://www.renpy.org/doc/html/store_variables.html#var-_quit_slot>`_, insert the following line at the top of the start label:

.. code-block:: console

    $ _quit_slot = "quitsave"


Wherever possible, Entroponaut will use Ren'Py's existing GUI system and config.

New GUI properties are inside the `entroponaut_gui` namespace.

New config properties are inside the `entroponaut_config` namespace.

Known Incompatibilities
-----------------------

- ADV text display and screen variant formats are currently unsupported.

- The save/load screens remove the default pagination feature in Ren'Py.
Pagination is still available in the engine, the new UI simply removes the
buttons to toggle pages.

License
-------

The source code for this project is licensed under the GNU GPLv3, available to read here:
https://github.com/jsfehler/entroponaut/blob/master/LICENSE

The fonts used have their own, separate licenses. They're available inside the `fonts/` directory.

Development History
-------------------

Large portions of this code are originally from: https://jsfehler.itch.io/speed-metal-vimana
While working on another project I took some time to extract relevant pieces into a more reusable kit.

There are no immediate plans to add new features and requests for new features will be ignored.
Pull Requests for new features will be considered.

Contributing
------------

Pull Requests to fix known incompatibilities and/or bugs are welcome.

For filing bugs, please use the
`GitHub issue tracker <https://github.com/jsfehler/entroponaut/issues>`_

New Config Properties
---------------------

  .. code-block:: console

      # Transform used for each item in the navigation menu.
      define entroponaut_config.navigation_item_transform = alpha_easein

      # Load/Save slots
      define entroponaut_config.audio.ui.loadsave_slot_hover = None
      define entroponaut_config.audio.ui.loadsave_slot_action = None
      define entroponaut_config.audio.ui.delete_file_button_action = None

      # Buttons
      define entroponaut_config.audio.ui.button_hover = None
      define entroponaut_config.audio.ui.button_action = None

New GUI Properties
------------------

  .. code-block:: console

      # Default settings for buttons
      define entroponaut_gui.button_borders = Borders(6, 6, 6, 6)
      define entroponaut_gui.button_tile = False
      define entroponaut_gui.button_font = f"{entroponaut_gui.root_directory}/fonts/oswald/static/Oswald-ExtraLight.ttf"
      define entroponaut_gui.button_font_color = "#b9d8db"

      define entroponaut_gui.prompt_font = f"{entroponaut_gui.root_directory}/fonts/oswald/static/Oswald-ExtraLight.ttf"

      define entroponaut_gui.label_font = f"{entroponaut_gui.root_directory}/fonts/noto_sans/NotoSans-Bold.ttf"

      # Quick menu
      define entroponaut_gui.quick_button_font_idle_color = "#b9d8db"
      define entroponaut_gui.quick_button_font_hover_color = "#000"

      # Navigation buttons
      define entroponaut_gui.nav_button_font = f"{entroponaut_gui.root_directory}/fonts/oswald/static/Oswald-Light.ttf"
      define entroponaut_gui.nav_button_text_idle_color = "#b9d8db"
      define entroponaut_gui.nav_button_text_hover_color = "#000"

      # Sliders
      define entroponaut_gui.slider_idle_color = "#b9d8db"
      define entroponaut_gui.slider_thumb_idle_color = "#b9d8db"

      # Save/Load
      define entroponaut_gui.save_load_button_font = f"{entroponaut_gui.root_directory}/fonts/noto_sans/NotoSans-Light.ttf"
      define entroponaut_gui.save_load_button_font_size = 19

      # Save/Load carets
      define entroponaut_gui.save_caret = "▼"
      define entroponaut_gui.load_caret = "▲"

      # Click to Continue caret.
      define entroponaut_gui.continue_caret = "►"

      # Used as a background for the input_confirm screen.
      define entroponaut_gui.input_confirm_background = Solid('#000')

      # The expected physical height of the font. Used for scrolling calculations.
      define entroponaut_gui.menu_height_adjustment = 26

      # The colour used for passive text
      define entroponaut_gui.passive_text_colour = "#787878"

      define entroponaut_gui.frame_alpha = 0.75

      define entroponaut_gui.game_menu_frame_background = Transform(Solid('#000'), alpha=entroponaut_gui.frame_alpha)
