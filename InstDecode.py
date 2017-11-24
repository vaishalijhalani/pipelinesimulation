import copy


class Decode:
    inst_count = 0

    def __init__(self, Input):
        self.input = Input
        self.output = []
        #self.reg_dict = registers.reg_dict
        self.prev_buf = [None, None]

    def next(self, counter):
        if len(self.input) != 0:
            inst = self.input[0].strip()
            inst_list = inst.split(" ")

            inst_dict = {'opcode': inst_list[0]}
            if inst_dict['opcode'] == 'sw':
                inst_dict['src_reg'] = inst_list[1:]
            else:
                inst_dict['dest_reg'] = inst_list[1]
                inst_dict['src_reg'] = inst_list[2:]

            stall_flag = False
            for inst in self.prev_buf:
                if inst is not None:
                    if inst['opcode'] != 'sw': 
                        if inst['dest_reg'] not in inst_dict['src_reg']:
                            continue
                        else:
                            stall_flag = True
                            break
                    else:
                        continue

            if not stall_flag:
                self.output.append(inst_dict)
                self.input.pop()
                    
            
            if self.prev_buf[0] is not None:  # copy value from 0 to 1
                self.prev_buf[1] = copy.deepcopy(self.prev_buf[0])
            else:
                self.prev_buf[1] = None

            self.prev_buf[0] = copy.deepcopy(inst_dict)

