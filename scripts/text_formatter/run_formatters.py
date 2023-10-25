import subprocess
import os
import sys

# ----------------------------------
# Remove Parentheses
# ----------------------------------

# script = os.path.join(os.getcwd(), "scripts", "text_formatter", "remove_parentheses.py")
# subprocess.call([sys.executable, script])

# ----------------------------------
# Remove/Format Line Breaks
# ----------------------------------

script = os.path.join(os.getcwd(), "scripts", "text_formatter", "remove_line_breaks.py")
subprocess.call([sys.executable, script])

# ----------------------------------
# Remove quotes, ...s, etc
# ----------------------------------

script = os.path.join(os.getcwd(), "scripts", "text_formatter", "text_formatter.py")
subprocess.call([sys.executable, script])