from InstFetch import Fetch
from InstDecode import Decode
from InstExec import Execute
from InstMem import Memory 
from InstWB import Writeback

fetch = Fetch('file2.txt')
decode = Decode(fetch.output, fetch.counter)
exe = Execute(decode.output, decode.counter)
mem = Memory(exe.counter)
wb = Writeback(mem.counter)

for i in range(0, 2):
    fetch.counter = i
    fetch.next()
    decode.next()
    exe.next()
    mem.next()
    wb.next()
    print 'first instruction completes in ',wb.counter, ' cycles'

# print decode.output
# print decode.counter
