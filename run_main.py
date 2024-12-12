import subprocess
import os

# dynamically add the current project directory to the Python `site-packages` path.
subprocess.run(["python", "set_pth.py"])

# start up main restful api service
main_script = os.path.join("OSUCS461", "main.py")
subprocess.run(["python", main_script])
