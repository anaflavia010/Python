metro = float(input('Digite uma distância em metros (m): '))
cm = metro * 100
mm = metro * 1000
dm = metro * 10
dam = metro / 10
hm = metro / 100
km = metro / 1000

print(f'A medida de {metro}m é:')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')