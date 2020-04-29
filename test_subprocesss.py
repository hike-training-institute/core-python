import os
import subprocess
PIPE = -1
STDOUT = -2
DEVNULL = -3

rc = subprocess.Popen(["bash", "test.sh"], stderr=STDOUT, stdout=PIPE)

out = rc.communicate()[0], rc.returncode