import pandas as pd
import random

# Main code block
places = ['Akurdi', 'Nigdi', 'Chinchwad', 'Pimpri', 'Ravet', 'Talwade', 'Hinjewadi', 'Wakad', 'Dange Chowk', 'Bhosari']
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times = ['Morning', 'Afternoon', 'Evening']
events = ['Yes', 'No']
popular_routes = [('Nigdi', 'Hinjewadi'), ('Pimpri', 'Talwade'), ('Chinchwad', 'Wakad'), ('Ravet', 'Dange Chowk')]

# Boost helper
def boost_demand(base, boost):
    levels = ['Low', 'Medium', 'High']
    i = levels.index(base)
    if boost == 1 and i < 2:
        return levels[i+1]
    if boost == -1 and i > 0:
        return levels[i-1]
    return base

# Smarter demand logic
def calculate_demand(f, t, day, time, temp, event):
    base = 'Medium'

    if (f, t) in popular_routes or (t, f) in popular_routes:
        base = 'High'
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'] and time in ['Morning', 'Evening']:
        base = 'High'
    if abs(places.index(f) - places.index(t)) <= 1:
        base = 'Medium'
    if temp > 38:
        base = 'Low'
    elif temp < 25 and time == 'Morning' and day in ['Saturday', 'Sunday']:
        base = 'Medium'
    if event == 'Yes':
        base = boost_demand(base, 1)
    if time == 'Afternoon' and event == 'No' and day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
        base = 'Low'

    return base

# Generate new dataset
data = []
for _ in range(1000):
    f = random.choice(places)
    t = random.choice([p for p in places if p != f])
    day = random.choice(days)
    time = random.choice(times)
    temp = round(random.uniform(22, 42), 1)
    event = random.choice(events)
    demand = calculate_demand(f, t, day, time, temp, event)
    data.append([f, t, day, time, temp, event, demand])

df = pd.DataFrame(data, columns=['from', 'to', 'day', 'time', 'temp', 'event', 'demand'])
df.to_csv('pcmctransit.csv', index=False)
print("✅ Realistic dataset with advanced rules saved to pcmctransit.csv")
