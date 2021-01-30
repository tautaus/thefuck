import re
from thefuck.utils import for_app


"Binary file abc.txt.gz matches"


@for_app('grep', 'egrep')
def match(command):
    return re.search(r"Binary file .* matches", command.output)

def get_new_command(command):
    if command.script[0] == 'e':
        command.script.replace("egrep","zgrep")
    else:
        command.script.replace("grep","zgrep")