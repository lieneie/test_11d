import math
a=float(input("Kvadrāta malas garums: "))
if a<5:
  a=float(input("Kvadrāta malas garumu, kas ir lielāks par 5 cm: ")) 
kv1=math.pow(a,2)
kv2=math.pow(a+5,2)
proc1=(kv2/kv1)*100
print("Procenti:",round(proc1))