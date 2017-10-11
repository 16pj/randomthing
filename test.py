from subprocess import Popen, PIPE

def test_print():
	cmd = 'curl localhost:5000'
	proc = Popen(cmd, shell=True, stdout=PIPE)
	out, err = proc.communicate()
	if out == "hello_world":
		return True
	else:
		raise('wrong output')


def test_wrong_print():
        cmd = 'curl localhost:5000'
        proc = Popen(cmd, shell=True, stdout=PIPE)
        out, err = proc.communicate()
        if out != "hello_world":
                raise('wrong output')
        else:
                return True


test_print()
test_wrong_print()
