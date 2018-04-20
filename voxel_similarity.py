import math

r = 10

def create_empty_voxel():
    z = lambda: {i : False for i in range(-r, r + 1)}
    y = lambda: {i : z() for i in range(-r, r + 1)}
    return {i : y() for i in range(-r, r + 1)}


def load_voxel(filename):
    with open(filename, 'r') as file:
        data = file.read().split('\n')[3:]
        for i, l in enumerate(data):
            data[i] = l.split(' ')[:3]

        data = data[:len(data) - 1]

        for i, l in enumerate(data):
            data[i] = [int(s) for s in l]

        v = create_empty_voxel()

        for d in data:
            v[d[0]][d[1]][d[2]] = True

    return v


reference = load_voxel('1.txt')
subject = load_voxel('2.txt')

max_voxels = math.pow(len(range(-r, r + 1)), 3)
diff = 0

for x, a in subject.items():
    for y, b in a.items():
        for z, v in b.items():
            if v != reference[x][y][z]:
                diff += 1


percent_similar = 100 - (diff / max_voxels) * 100.0

print(percent_similar)
