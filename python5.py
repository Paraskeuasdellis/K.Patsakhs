
x = raw_input("Enter date (ex. dd//mm//yyyy) \n")
y = x.split("//")
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

d = y[0] 
m = y[1]
y = y[2]

d = int(d)
m = int(m)
y = int(y)

def Hmer(day, month, year):
     d = day
     m = month
     y = year
     if m < 3:
        z = y-1
     else:
         z = y
     dayofweek = ( 23*m//9 + d + 4 + y + z//4 - z//100 + z//400 )
     if m >= 3:
         dayofweek -= 2
     dayofweek = dayofweek%7
     return dayofweek


dayofweek  =  days[Hmer(d, m, y)-1]
print dayofweek

        
            

        


 



 







