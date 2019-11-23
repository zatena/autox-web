from autox import run
import os
from shutil import copyfile
import autox


report = run.run("招聘")

reportDirPath = os.path.dirname(os.path.realpath("report")) + "/report/"


# path = os.path.dirname(autox.__file__)
#
# print(path)

# pipath = os.system("pip3 show autox")['Location']+"/autox/model"

# yamlPath = os.path.split(os.path.realpath(__file__))[0]

# print(pipath)








