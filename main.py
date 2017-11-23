from InstFetch import Fetch
from InstDecode import Decode
from InstExec import Execute
from InstMem import Memory
from InstWB import Writeback
from memReg import RegClass

registers = RegClass(64)

fetch = Fetch('file3.txt')
decode = Decode(fetch.output)
exe = Execute(decode.output)
mem = Memory(exe.output)
wb = Writeback(mem.output)

for i in range(0, 10):

	fetch.next()
	decode.next()
	exe.next()
	mem.next()
	wb.next()
#print('first instruction completes in ', wb.counter, ' cycles')

# print(decode.output)
# print(decode.counter)
