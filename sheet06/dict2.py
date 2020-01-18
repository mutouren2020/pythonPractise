aliens = []

for alien_num in range(20):
    new_alien = {'color': 'green', 'point': alien_num, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['speed'] = 'fast'

for alien in aliens[:5]:
    print(alien['speed'])

print("Total number of aliens: " + str(len(aliens)))
