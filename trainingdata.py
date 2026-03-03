import csv

# Load training data
data = []
with open('trainingdata.csv') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        data.append(row)

num_attr = len(data[0]) - 1

# Initialize S and G
S = ['0'] * num_attr
G = [['?'] * num_attr]


def is_consistent(h, x):
    for i in range(len(h)):
        if h[i] != '?' and h[i] != x[i]:
            return False
    return True


for row in data:
    x = row[:-1]
    label = row[-1]

    if label == "Yes":  # Positive Example

        # Remove inconsistent hypotheses from G
        G = [g for g in G if is_consistent(g, x)]

        # Generalize S if needed
        for i in range(num_attr):
            if S[i] == '0':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'

    else:  # Negative Example

        new_G = []

        for g in G:
            if is_consistent(g, x):

                for i in range(num_attr):
                    if g[i] == '?':

                        if S[i] != x[i]:
                            new_h = g.copy()
                            new_h[i] = S[i]
                            new_G.append(new_h)
            else:
                new_G.append(g)

        G = new_G

# Remove duplicates
G_unique = []
for g in G:
    if g not in G_unique:
        G_unique.append(g)

# Output
print("Final Specific Hypothesis S:")
print(S)

print("\nFinal General Hypotheses G:")
for g in G_unique:
    print(g)
