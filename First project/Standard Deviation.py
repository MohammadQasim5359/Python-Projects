import math
a = 9
b = 8
c = 12
d = 33
e = 5

totalss = a+b+c+d+e



meaning = (a+b+c+d+e)/5

subtracta = (meaning - a)**2
subtractb = (meaning - b)**2
subtractc = (meaning - c)**2
subtractd = (meaning - d)**2
subtracte = (meaning - e)**2

newtotal = subtracta+subtractb+subtractc+subtractd+subtracte

variance = newtotal/5

standardd = math.sqrt(variance)

print(standardd)



