#! /usr/bin/python3
import time
import os
import sys
import shutil
import select

# Error management and helper
if len(sys.argv) != 4 or sys.argv[1] == "-h":
  print("Usage:\n\t./main [Path1] [Path2] [Time]\n")
  print("Path1 = Path of the source\nPath2 = Path of the replica")
  print("Time = Time of the synchronization intervale (In seconds)")
  exit (84)

# Define the paths to the two folders
source = sys.argv[1]
replica = sys.argv[2]

while True:
  # Get a list of the files and directories in each folder
  files_and_dirs_source = os.listdir(source)
  files_and_dirs_replica = os.listdir(replica)

  # Iterate through the files and directories in source
  for item in files_and_dirs_source:
    # Check if the item exists in replica
    if item not in files_and_dirs_replica or item in files_and_dirs_replica:
      # If it does not exist, copy it from source to replica
      shutil.copy(os.path.join(source, item), replica)

  # Iterate through the files and directories in source
  for item in files_and_dirs_replica:
    # Check if the item exists in source
    if item not in files_and_dirs_source:
      # If it does exist, remove it from replica
      os.remove(os.path.join(replica , item))

  # Check for the key press to stop the program
  if select.select([sys.stdin], [], [], 0)[0]:
    key_pressed = sys.stdin.read(1)
    if key_pressed == 'q':
        break

  # Sleep to wait the next synchronization
  time.sleep(float(sys.argv[3]))

  
    
