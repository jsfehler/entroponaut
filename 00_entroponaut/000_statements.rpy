python early:
    # Create the 'passive' statement. When used before a line, that line
    # is then given the color of entroponaut_gui.passive_colour and the script
    # will automatically progress to the next line.

    def parse_smartline(lexer):
        who = lexer.simple_expression()
        what = lexer.rest()
        return (who, what)

    def execute_smartline(parsed_object):
        who, what = parsed_object
        if not what:
            what = who
            who = None

        what = f"{{=passive_text}}{what}{{/color}}{{nw}}"

        renpy.say(who, what)

    def lint_smartline(parsed_object):
        who, what = parsed_object
        try:
            eval(who)
        except Exception:
            renpy.error(f"Character not defined: {who}")

        tte = renpy.check_text_tags(what)
        if tte:
            renpy.error(tte)

    renpy.register_statement(
        'passive',
        parse=parse_smartline,
        execute=execute_smartline,
        lint=lint_smartline,
    )
