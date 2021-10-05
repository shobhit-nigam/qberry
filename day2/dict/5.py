avengers = {'iron man':'suit', 'hulk':'smash',
    'captain':['shield', 'hammer'], 'natasha':'power'}

xmen = ['wolverine', 'mystique', 'magneto']

marvel = {'xmen':xmen, 'ave':avengers}


print("avengers =", avengers)
print("----")
print("marvel =", marvel)
print("----")
print("marvel['ave'] =", marvel['ave'])
print("----")
print("marvel['ave']['captain'] =", marvel['ave']['captain'])
print("----")
print("marvel['ave']['captain'][0] =", marvel['ave']['captain'][0])
print("----")
print("marvel['ave']['captain'][0][1] =", marvel['ave']['captain'][0][1])
