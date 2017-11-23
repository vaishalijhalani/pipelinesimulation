import copy


class Decode:
    inst_count = 0


def __init__(self, Input):
    self.input = Input
    self.output = []
    #self.reg_dict = registers.reg_dict
    self.prev_buf = [None, None, None]


def next(self):
    inst = self.input.pop()
    inst = inst[:-1]
    inst_list = inst.split(" ")

    inst_dict = {'opcode': inst_list[0]}
    if inst_dict['opcode'] == 'sw':
        inst_dict['src_reg'] = inst_list[1:]
    else:
        inst_dict['dest_reg'] = inst_list[1]
        inst_dict['src_reg'] = inst_list[2:]

    self.output.append(inst_dict)

    if self.prev_buf[1] is not None:  # copy value from 1 to 2
        self.prev_buf[2] = copy.deepcopy(self.prev_buf[1])
    else:
        self.prev_buf[2] = None

    if self.prev_buf[0] is not None:  # copy value from 0 to 1
        self.prev_buf[1] = copy.deepcopy(self.prev_buf[0])
    else:
        self.prev_buf[1] = None

    if inst_dict.opcode != 'sw':  # copy value to 0
        self.prev_buf[0] = copy.deepcopy(inst_dict)
    else:
        self.prev_buf[0] = None
