from InstFetch import Fetch
from InstDecode import Decode
from InstExec import Execute
from InstMem import Memory
from InstWB import Writeback

fetch = Fetch('file2.txt')
decode = Decode(fetch.output)
exe = Execute(decode.output)
mem = Memory(exe.output)
wb = Writeback(mem.output)

for i in range(0, 50):
	inst = wb.next(i)
	if inst is not None:
		print(inst)
	mem.next(i)
	exe.next(i)
	decode.next(i)
	inst_fetch = fetch.next(i)
	# if inst_fetch:
	# 	print('fetch:',inst_fetch,i)