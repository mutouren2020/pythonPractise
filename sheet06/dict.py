aliens = []

for alien_num in range(20):
    new_alien = {'color': 'green', 'point': alien_num, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[-3:]:
    print(alien)

print("Total number of aliens: " + str(len(aliens)))