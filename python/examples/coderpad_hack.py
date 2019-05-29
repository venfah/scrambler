import os
print (os.getcwd())
print (os.getcwd() + os.sep + __file__)

print (os.listdir("/home/coderpad"))

with open("README_IF_YOU_ARE_HACKING_ME") as fd:
    for line in fd:
        print (line)



'''
OUTPUT

/home/coderpad
/home/coderpad/solution.py
['.profile', '.bashrc', 'README_IF_YOU_ARE_HACKING_ME', '.bash_logout', '.ipython', 'solution.py', 'ipython_config.py', 'pytest.ini']
 ______   ______   _____    ______   ______   ______  ______   _____

/\  ___\ /\  __ \ /\  __-. /\  ___\ /\  == \ /\  == \/\  __ \ /\  __-.

\ \ \____\ \ \/\ \\ \ \/\ \\ \  __\ \ \  __< \ \  _-/\ \  __ \\ \ \/\ \

 \ \_____\\ \_____\\ \____- \ \_____\\ \_\ \_\\ \_\   \ \_\ \_\\ \____-

  \/_____/ \/_____/ \/____/  \/_____/ \/_/ /_/ \/_/    \/_/\/_/ \/____/



Hello! Hope you are enjoying CoderPad. I've added this file because a

lot of people have emailed me voicing security concerns. Usually these

concerns are to the tune of "programming language X lets me run Y

system call."



They're not wrong, you can run any system call! Security in CoderPad

happens at the LXC sandbox layer. You are currently in an ephemeral

container that will be destroyed upon your departure. You are welcome

to run any privileged operation you can get your hands on. CoderPad

is, after all, the highest fidelity programming interview tool there

is.



That said, if you do manage to uncover something like privilege

escalation or data created by other users, I want to hear about it.

You can email me at vincent@coderpad.io or tweet at @fulligin, and I

look forward to hearing from you.



Happy hunting!


'''
