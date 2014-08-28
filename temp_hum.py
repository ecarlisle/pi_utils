from subprocess import Popen, PIPE
import subprocess, time, sys, os, re

Pin = "12"

Args = ["./dht/DHT", "2302", Pin]

Start = time.time()

while True:
	Temp = Humi = Out = ""
	Proc = Popen(Args, stdout=PIPE)
	Out = Proc.stdout.read()
	Proc.stdout.flush()
	#print Out
	Temp = re.findall(r'[-]*[0-9]*.[0-9]* C', Out)
	Humi = re.findall(r'[-]*[0-9]*.[0-9]* %', Out)
	if len(Temp)>0 and len(Humi)>0:
		print("[{0},{1}]".format(Temp[0], Humi[0]))
		sys.exit()
	else:
		if (time.time() - Start) > 5:
			print "[0 C,0 %]"
			sys.exit()
	time.sleep(1.3)
