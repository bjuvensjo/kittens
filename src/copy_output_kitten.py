import subprocess
import sys

from kittens.tui.handler import result_handler
from kitty.boss import Boss


# in main, STDIN is for the kitten process and will contain
# the contents of the screen
def main(_) -> str:
    return sys.stdin.read()


# in handle_result, STDIN is for the kitty process itself, rather
# than the kitten process and should not be read from.
@result_handler(type_of_input="output")
def handle_result(args: list[str], stdin_data: str, target_window_id: int, boss: Boss) -> None:
    subprocess.run("pbcopy", text=True, input=stdin_data)
