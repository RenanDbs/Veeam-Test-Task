# Veeam-Test-Task
### Installation

1. Clone the repo
   ```sh
   git clone git@github.com:RenanDbs/Veeam-Test-Task.git
   ```
2. Go to the repo location
   ```sh
   cd Veeam-Test-Task
   ```
3. Use Make to make the program executable
     ```sh
   make
   ```
4. Run the program
   ```sh
   sudo ./main [Path1] [Path2] [Time]
   ```

Tips:

You can use '-h' arguments to get information on the usage
   ```sh
  ./main -h
Usage:
	sudo ./main [Path1] [Path2] [Time]

Path1 = Path of the source
Path2 = Path of the replica
Time = Time of the synchronization intervale (In seconds)
   ```
