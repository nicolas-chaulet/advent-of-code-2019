def validate_increase(seq):
    for i in range(len(seq)-1):
        if seq[i+1] < seq[i]:
            return False

    return True

def validate_dup(seq):
    counts = {}
    for i in range(len(seq) - 1):
        if seq[i+1] == seq[i]:
            if seq[i] in counts:
                counts[seq[i]] += 1
            else:
                counts[seq[i]] = 2
    return 2 in counts.values()

class Code:
    def __init__(self,lower, upper):
        self.lower = lower
        self.upper = upper
        self.number = lower

    def is_correct(self):
        dup = False
        num_as_list = [a for a in str(self.number)]
        return validate_increase(num_as_list) and validate_dup(num_as_list)

    def increment(self):
        if self.number > self.upper:
            return False
        self.number+=1
        return True

if __name__ == "__main__":
    print(validate_dup('222133'))
    print(validate_dup('122133'))
    print(validate_dup('122233'))
    print(validate_dup('222222'))
    c = Code(128888, 599999)
    count = int(c.is_correct())
    while c.increment():
        if c.is_correct():
            count += 1
    print(count)
