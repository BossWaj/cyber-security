import os
import time

for i in range(1,6):
  print("System will logout in " + i)
  time.sleep(1)

os.system("shutdown -l")
