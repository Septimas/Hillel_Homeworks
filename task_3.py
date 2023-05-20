casino_blacklist = {'Allan Backer', 'Patric Jane', 'Kim Lee'}
poker_blacklist = {'Kim Lee', 'Jim Levinstein', 'Adam Sandler'}
alcohol_blacklist = {'Lara Croft', 'Kim Lee', 'John Dow'}
result = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(result)
