import random

random.seed(10)
output_lines = []

users = ['Alice', 'Bob', 'Trudy', 'Fido']
actions = ['performed a payment of {}', 'checked their balance', 'received {}']

# Logging everyone in
for user in users:
    output_lines.append(f"{user}; logged in; {random.randint(0, 100)}")

# Doing actions:
for inc in range(0,300,100):
    for _ in range(200):
        output_lines.append(f"{random.choice(users)}; {random.choice(actions).format(random.randint(10,300))}; {random.randint(100 + inc, 1000 - inc)}")

# logging everyone out
for user in users:
    output_lines.append(f"{user}; logged out; {random.randint(1000,1200)}")

random.shuffle(output_lines)

with open('log.txt', 'w') as f:
    f.write('\n'.join(output_lines))

print(f"{len(output_lines)} lines were written to log.txt")