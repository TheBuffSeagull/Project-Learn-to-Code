aliens = []

# make 30 green aliens
for alien_number in range(31):
    new_alien = { #dictionary to be replicated
    'color': 'green',
    'points': '5',
    'speed': '5',
    }

    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien.get("color") == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = "10"
    elif alien.get("color") == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = "15"

#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

print("...")

#show how many aliens have been created.
print(f"\nTotal number of aliens: {len(aliens)}")