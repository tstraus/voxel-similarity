from sys import argv
from sys import exit
import math

r = 10


def create_empty_voxel():
    z = lambda: {i : False for i in range(0, r)}
    y = lambda: {i : z() for i in range(0, r)}
    return {i : y() for i in range(0, r)}


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


def load_from_voxelizer(filename):
    return {}


def load(filename):
    if filename[-4:] == '.txt':
        return load_from_goxel(filename)
    elif filename[-5:] == '.json':
        return load_from_voxelizer(filename)
    else:
        print('invalid file given: ' + filename)
        exit(0)


if len(argv) != 3:
    print('incorrect number of arguments given')
    exit(0)

else:
    reference_name = argv[1]
    subject_name = argv[2]

    if reference_name[-4:] == '.txt':
        reference = load_from_goxel(reference_name)

    reference = load_from_goxel(reference_name)
    subject = load_from_goxel(subject_name)

    max_voxels = math.pow(len(range(0, r)), 3)
    diff = 0

    for x, a in subject.items():
        for y, b in a.items():
            for z, v in b.items():
                if v != reference[x][y][z]:
                    diff += 1


    percent_similar = 100 - (diff / max_voxels) * 100.0

    print(percent_similar)
