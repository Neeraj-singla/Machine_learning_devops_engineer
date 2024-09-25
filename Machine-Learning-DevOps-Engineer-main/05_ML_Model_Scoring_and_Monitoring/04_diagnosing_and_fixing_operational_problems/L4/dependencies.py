
import subprocess

broken = subprocess.check_output(['pip', 'check'])
with open('broken.txt', 'w') as f:
    f.write(broken)


installed = subprocess.check_output(['pip', 'list'])
with open('installed.txt', 'w') as f:
    f.write(installed)

requirements = subprocess.check_output(['pip', 'freeze'])
with open('requirements.txt', 'w') as f:
    f.write(requirements)

sklearninfo = subprocess.check_output(['python', '-m', 'pip', 'show', 'scikit-learn'])
with open('sklearninfo.txt', 'w') as f:
    f.write(sklearninfo)