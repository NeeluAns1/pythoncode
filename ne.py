import pexpect
#start a child process with spawn
#It just echos geeksforgeeks
print(pexpect.run('echo hello'))
child = pexpect.spawn("echo mywolrd")
print(child.expect(["Hello","welcome","myworld"]))