#Augustine
#Assignment topic8_temperatures
temps = [24, 27, 22, 30, 25, 28, 21]
days = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
print(temps[0], temps[-1], temps[1:4], len(temps), days[3])

temps.append(26)
temps.remove(22)
print(temps)

print(sorted(temps))
temps.sort(reverse=True)
print(temps[:3])
temps.sort()
print (max(temps), min(temps), sum(temps), round(sum(temps) / len(temps), 2))

hot_days = [t for t in temps if t >= 27]
print(hot_days, len(hot_days))

fahrenheit = [round(t * 9 / 5 + 32, 1) for t in temps]
print(fahrenheit)
city = ("Nairobi", -1.286, 36.817)
name, lat, lon = city
print(name, lat, lon)
print (temps.count(25), 30 in temps, 35 in temps, temps.index(30))
