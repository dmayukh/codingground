# Hello World program in Python
    
print "Hello World!\n"
mylist =   [1,2, 3, 4,5 ]
print mylist
print mylist[3:5]
mylist[3:4] = [0,1]
print mylist[:]


ll = [1,3,4,4,6,10,11,8]
print ll

              
def sort(ll): 
    for i in range(len(ll)):
        for j in range(len(ll) - 1):
            if( ll[i] < ll[j] ):
                t = ll[i]
                ll[i] = ll[j]
                ll[j] = t
    return ll            
ls = sort(ll)                
print ls  
