if __name__ == '__main__':
	# Sample configuration for CIFS shares
	separator = ", "
	# List of CIFS share names separated by "separator" (paste the output of 'ls -m' once the mount points are created):
	share_names = "backup, media, nicholas"
	# General layout for one entry:
	template = "//192.168.X.X/{share_name} /mnt/{share_name} cifs credentials=/path/to/credentials/file,(additional options) 0 0"
	for sn in share_names.split(separator):
		entry = template.format(share_name=sn)
		print(entry)
