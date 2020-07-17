# fstabber
A minimalistic tool to automate the process of generating fstab lines to mount many network shares at once

This script allows you to create dozens of network mount fstab entries without tediously "copy, paste, change"ing them.

## How to use

Ideally, this tool will be run on a personal computer and you'll SSH into the remote server and paste the output.

To use this tool, modify the fstabber.py file to meet your needs. By default, it has a general template for CIFS shares.

Then, run fstabber.py on your local computer, copy the output, and paste it into /etc/fstab on the remote server.

## Sample output:

//192.168.X.X/backup /mnt/backup cifs credentials=/path/to/credentials/file,(additional options) 0 0

//192.168.X.X/media /mnt/media cifs credentials=/path/to/credentials/file,(additional options) 0 0

//192.168.X.X/nicholas /mnt/nicholas cifs credentials=/path/to/credentials/file,(additional options) 0 0
