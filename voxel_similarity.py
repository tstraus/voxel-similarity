from pprint import pprint


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


pprint(load_voxel('1.txt'))