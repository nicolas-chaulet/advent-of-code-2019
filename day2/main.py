import numpy as np

INPUT_CODE=np.loadtxt('day2/input.txt',delimiter=',')

ADD_OP_CODE=1
MUTL_OP_CODE=2
END_CODE=99

class integer_code:
    def __init__(self,start_code):
        self._code = start_code.astype(np.uint32)
        self._current_loc = 0
    
    def add_op(self,pos1, pos2, result):
        self._code[result] =  self._code[pos1] +  self._code[pos2]
    
    def mult_op(self,pos1, pos2, result):
        self._code[result] =  self._code[pos1] *  self._code[pos2]

    def step(self):
        if self._current_loc >= len(self._code):
            return False
        current_op  = self._code[self._current_loc]
        if current_op == ADD_OP_CODE:
            self.add_op(self._code[self._current_loc+1], self._code[self._current_loc+2], self._code[self._current_loc+3])
        elif current_op == MUTL_OP_CODE:
            self.mult_op(self._code[self._current_loc+1], self._code[self._current_loc+2], self._code[self._current_loc+3])
        else:
            return False
        self._current_loc += 4
        return True
    
    def run(self):
        running = True
        while running: 
            running = self.step()

    def get_result(self):
        return self._code[0]
    
    def get_answer(self):
        print("Noun is %i, verb is %i" % (self._code[1],self._code[2]))
        return 100* self._code[1] +self._code[2]

def main():
    TO_FIND = 19690720
    for i in range(100):
        for j in range(100):
            input_code = INPUT_CODE.copy()
            input_code[1] = i
            input_code[2] = j
            programme = integer_code(input_code)
            programme.run()
            if programme.get_result() == TO_FIND:
                print(programme.get_answer())
                break

if __name__ == "__main__":
    main()