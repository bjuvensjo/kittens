import subprocess
import sys

from kittens.tui.handler import result_handler


# in main, STDIN is for the kitten process and will contain
# the contents of the screen
def main(_) -> str:
    return sys.stdin.read()


# in handle_result, STDIN is for the kitty process itself, rather
# than the kitten process and should not be read from.
@result_handler(type_of_input="output")
def handle_result(args, stdin_data, target_window_id, boss) -> None:
    subprocess.run("pbcopy", universal_newlines=True, input=stdin_data)
