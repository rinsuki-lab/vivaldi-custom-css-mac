#!/usr/bin/python
import os
import glob
import shutil
import datetime

VIVALDI_APP_PATH = os.environ.get("VIVALDI_APP_PATH", "/Applications/Vivaldi.app")
VIVALDI_RESOURCE_PATH = os.path.join(VIVALDI_APP_PATH, "Contents", "Versions", "*", "Vivaldi Framework.framework", "Versions", "A", "Resources", "vivaldi")
CUSTOM_CSS_PATH = os.path.dirname(os.path.realpath(__file__))

for p in glob.glob(VIVALDI_RESOURCE_PATH):
    print("Installing to '" + p + "'...")
    shutil.copy2(os.path.join(CUSTOM_CSS_PATH, "custom.css"), os.path.join(p, "style", "custom.css"))
    shutil.copy2(os.path.join(p, "browser.html"), os.path.join(p, "browser.backup."+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".html"))
    r = open(os.path.join(p, "browser.html"), "r").read()
    if "style/custom.css" in r:
        print("[Info] already installed to this Vivaldi.app. only rewrite custom.css.")
    else:
        r = r.replace("</head>", '<link rel="stylesheet" href="style/custom.css"/></head>')
        open(os.path.join(p, "browser.html"), "w").write(r)

print("Finished! Please restart your vivaldi browser.")