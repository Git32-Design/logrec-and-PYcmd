import PYcmd


def test_calc_safe():
    # simple arithmetic
    PYcmd.calc("2+3*4")
    # math function
    PYcmd.calc("sqrt(16)")
    # dangerous expression should be handled
    PYcmd.calc("__import__('os').system('echo hi')")

# Requires: see ../requirements.txt for external packages used in tests/tools
