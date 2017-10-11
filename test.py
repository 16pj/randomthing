from subprocess import Popen, PIPE

def test_print():
	cmd = 'curl localhost:5000'
	proc = Popen(cmd, shell=True, stdout=PIPE)
	out, err = proc.communicate()
	if out == "hello_world":
		return True
	else:
		raise('wrong output')



test_print()
