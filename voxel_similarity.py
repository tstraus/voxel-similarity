#import math

def create_empty_voxel():
    z = lambda: {i: False for i in range(-10, 10 + 1)}
    y = lambda: {i:z() for i in range(-10, 10 + 1)}
    return {i:y() for i in range(-10, 10 + 1)}


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


def get_total_voxels(v):
    count = 0

    for x, a in v.items():
        for y, b in a.items():
            for z, c in b.items():
                if c:
                    count += 1

    return count


reference = load_voxel('1.txt')
subject = load_voxel('0.75.txt')

#max_num_voxels = math.pow(len(range(-10, 10 + 1)), 3)
diff = 0

for x, a in subject.items():
    for y, b in a.items():
        for z, v in b.items():
            if v != reference[x][y][z]:
                diff += 1


reference_total = get_total_voxels(reference)
percent_diff = (diff / reference_total) * 100.0
#percent_diff = (diff / max_num_voxels) * 100.0

print(percent_diff)
