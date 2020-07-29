import time
import sys

product = int(sys.argv[1])

def factor_this(product):
    current_value=1
    lower_list=[]
    upper_list=[product]

    def progress(count, total, status=''):
        bar_len = 20
        filled_len = int(round(bar_len * count / float(total)))
        percents = round(100.0000 * count / float(total), 4)
        bar = '#' * filled_len + '-' * (bar_len - filled_len)
        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
        sys.stdout.flush()
        
    while current_value < upper_list[0]:
        if product % current_value == 0:
            lower_list.append(current_value)
            upper_list.insert(0, product//current_value)
            current_value += 1
            progress(current_value, upper_list[0], 'In Progress')
        else:
            current_value += 1
    full_list= lower_list + upper_list
    print(sorted(set(full_list)))

starts = time.time()
factor_this(product)
ends = time.time() - starts
print(ends)

""" starts2 = time.time()
[num for num in range(1,product+1) if product % num  == 0]
ends2 = time.time() - starts2
print(ends2) """