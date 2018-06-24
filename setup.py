import cx_Freeze

executables = [cx_Freeze.Executable("letsrace.py")]

cx_Freeze.setup(
	name="Let's Race",
	options={"build_exe":{"packages":["pygame"],"include_files":["bgimg.png","img.png","img1.png","jazz.wav","crash.wav"]}},
	executables = executables
	)
input()
