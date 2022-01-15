import os, sys



def sorter(target_dir: str):
	try:
		all_fext = []
		all_files = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]
		new_dir = target_dir+'/sorted'
		# with_dirs = False
		# if with_dirs:
		# 	all_files = [f for f in os.listdir(target_dir) if f not in ['sorted']]

		# 'Finding files'
		for f in all_files:
			fext = (os.path.splitext(f)[1][1:]).lower()
			if fext not in all_fext:
				all_fext.append(fext)

		# 'Creating directory by file extension'
		for ext in all_fext:
			if ext:
				os.makedirs(os.path.join(new_dir, ext), exist_ok=True)

		# 'Moving files'
		for f in all_files:
			ext = (os.path.splitext(f)[1][1:]).lower()
			old_path = os.path.join(target_dir, f)
			new_path = os.path.join(new_dir, ext, f)
			os.rename(old_path, new_path)
		print(f"Files moved {len(all_files)}")
	except Exception:
		print(sys.exc_info()[0])


sorter('/home/username/Downloads')
