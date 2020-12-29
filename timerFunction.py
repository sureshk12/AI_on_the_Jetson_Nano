import time

tic = time.perf_counter()
time.sleep(1)
tac = time.perf_counter()
print ('Delta Time is {}'.format(tac - tic))