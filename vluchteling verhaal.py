import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.5/10)

slowprint("op een dag word je wakker")
slowprint("het begint zoals elke andere dag")
slowprint("")
slowprint("")
slowprint("dan opeens hoor je een harde knal en gaat er een alarm af")

