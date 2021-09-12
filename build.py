import sys
import subprocess
import pkg_resources

#Check if we have all the required packages. If not, installs them.
reqs_file = open("requirements.txt", "r")
required = {line.strip() for line in reqs_file.readlines()}
reqs_file.close()

installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
  python = sys.executable
  subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

#Create the list of packages to exclude from our installation.
excluded = installed - required

exc_file = open("excluded.txt", "w")
for package in excluded:
  exc_file.write(package+'\n')  
exc_file.close()

subprocess.check_call([python, '-m', 'PyInstaller', 'main.spec'], stdout=subprocess.DEVNULL)
