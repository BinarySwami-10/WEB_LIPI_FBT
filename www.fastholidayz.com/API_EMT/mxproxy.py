import sys
success = 0
importlevel = "./"

sys.path.append('../')
sys.path.append('../../')

try:
	import modulex as mx
except Exception as e:
	pass
