import os, sys
currentdir = os.path.dirname(os.path.relpath("../../"))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from pkg import create_app

app = create_app()
if __name__ == "__main__":
    app.run(port=5000)