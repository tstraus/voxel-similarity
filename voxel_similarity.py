import math

r = 10

def create_empty_voxel():
    z = lambda: {i : False for i in range(0, 10)}
    y = lambda: {i : z() for i in range(0, 10)}
    return {i : y() for i in range(0, 10)}


def load_from_goxel(filename):
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


reference = load_from_goxel('./voxel_spaces/goxel/10.txt')
subject = load_from_goxel('./voxel_spaces/goxel/not10.txt')

max_voxels = math.pow(len(range(0, r)), 3)
diff = 0

for x, a in subject.items():
    for y, b in a.items():
        for z, v in b.items():
            if v != reference[x][y][z]:
                diff += 1


percent_similar = 100 - (diff / max_voxels) * 100.0

print(percent_similar)
