string = input("Enter any string : ")

occ_not = string.index('not')
occ_poor = string.index('poor')

new_str = ""

if occ_not < occ_poor:
    new_str = string[:occ_not] + 'good'

print(new_str)