import pexpect

#start a child proces with spawn
#this process waits for the input
#form usr

child = pexpect.spawn("cat")

#the input to the cat proces is sent
#by the sendline()

child.sendline("Welcome World")

#prints the index of matched string
#expressing with child process

print(child.expect(["hello","Welcome World"],timeout=120))