import time
def count(number) :
    for i in range(number):
        print (i)
        
   

cas_pred_funkci = time.time()
result = count (10000000)
print (result)
cas_po_funkci = time.time()
trvani = cas_po_funkci - cas_pred_funkci
print (trvani)
 