import time
start = time.time()
a = [i for i in range (3, 1001) if i%3==0 or i%5==0]
print(sum(a))
print(time.time()-start)
