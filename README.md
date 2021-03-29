RFCParser.py extract's the path of binaries executed from RecentFileCach.bcf on Windows 7 and Windows Server 2008 R2 it will provied a JSON output file.

RecentFileCache.bcf contains the path of binaries executed between the last execution date of ProgramDataUpdater and the current time.

*It's required python 3.8 and above versions. 

NOTE: Order of the paths are not stored chronological.

RecetFileCache.bcf can be found at "C:\Windows\AppCompat\Programs\RecentFileCache.bcf".


Usage
Python RFCParser.py -f "path to RecentFileCache.bcf" -o "NameOfOutputFile"
