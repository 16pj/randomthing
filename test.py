from subprocess import Popen, PIPE

def test_print():
	cmd = 'curl localhost:5000'
	proc = Popen(cmd, shell=True, stdout=PIPE)
	out, err = proc.communicate()
	assert out == "hello_world"


def test_wrong_print():
        cmd = 'curl localhost:5000'
        proc = Popen(cmd, shell=True, stdout=PIPE)
        out, err = proc.communicate()
        assert out != "hello_world":


def test_square():
	test_val = 2
        cmd = 'curl localhost:5000/square/' + str(test_val)
        proc = Popen(cmd, shell=True, stdout=PIPE)
        out, err = proc.communicate()
        assert out == 4:

test_print()
test_wrong_print()
test_square()
