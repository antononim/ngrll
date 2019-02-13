import os
from time import sleep as t
from sys import exit as e

logoseeker = """
                             d8                    
 d88~\  e88~~8e   e88~~8e  _d88__  e88~~8e  888-~\ 
C888   d888  88b d888  88b  888   d888  88b 888    
 Y88b  8888__888 8888__888  888   8888__888 888    
  888D Y888    , Y888    ,  888   Y888    , 888    
\_88P   "88___/   "88___/   "88_/  "88___/  888 

  /01/ - Install seeker
  /02/ - Remove seeker
  /03/ - Exit
"""

def install():
	os.system("cd $HOME && rm -rf seeker")
	os.system("git clone https://github.com/thewhiteh4t/seeker.git && cd seeker/termux")
	os.system("./install.sh && seeker.py")
	os.system("clear")

def remove():
	os.system("cd $HOME && rm -rf seeker")
	os.system("clear")

def clear():
	os.system("clear")

def main():
	clear()
	print(logoseeker)
	wtf = input("seeter > ")
	if wtf == "1" or wtf == "01":
		install()
		clear()
		main()
	elif wtf == "2" or wtf == "02":
		remove()
		clear()
		main()
	elif wtf == "3" or wtf == "03":
		print("\nExiting...")
		t(1)
		e()
	else:
		print("\nERROR: Check your command!")
		t(1)
		clear()
		main()

if __name__ == '__main__':
	main()

#####################
# PRIVET FROM OTX2S #
#####################