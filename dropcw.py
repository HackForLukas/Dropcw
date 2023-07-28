import os, socket
def banner():
	print("""\033[92m   ___                  ______      __
  / _ \_______  ___    / ___/ | /| / /
 / // / __/ _ \/ _ \  / /__ | |/ |/ / 
/____/_/  \___/ .__/  \___/ |__/|__/  
             /_/ \033[93m Dropper Tool For Crewinux\033[0m""")
def drop(ip):
	try:
		print(f"\033[92m[ \033[93mDrop: {ip} || Please Use Kali Linux\033[92m ]\033[30m")
		os.system(f"iptables -A INPUT -s {ip} -j DROP")
		print("\033[0m")
	except:
		pass
def dropwithnum(ip, num):
	for _ in range(num):
		drop(ip)
def getip(target):
	return socket.gethostbyname(target)
def exit():
	os.system("exit")
def menu():
	try:
		os.system("clear	")
		banner()
		print("\n\033[92m[ 1 ] \033[93mStart Drop")
		print("\033[92m[ 2 ] \033[93mExit")
		cho = input("\n\033[92mChoice: \033[93m")
		if cho == "1":
			target = input("Enter Target (Website/IP): ")
			num = int(input("Enter Drop Count: "))
			ip = getip(target)
			print(f"Target IP: {ip}")
			dropwithnum(ip, num)
			enter = input("[ Enter to menu ]")
			menu()
		elif cho == "2":
			exit()
		else:
			menu()
	except:
		menu()
menu()
