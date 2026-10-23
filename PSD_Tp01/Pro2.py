total_s = 9875

hour = total_s // 3600
mn = (total_s % 3600) // 60
s = total_s % 60 

print (f"{hour}h {mn}mn {s}s")
print ((2 * 3600 + 44 * 60 + 35) == total_s)
