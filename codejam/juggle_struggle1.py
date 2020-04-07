from math import atan2, degrees

def get_angles(p, allpoints, excluded):
    angles = []
    for i, otherp in allpoints:
        if i not in excluded:
            new_angle = degrees(atan2(otherp[0]-p[0], otherp[1]-p[1]))
            angles.append((i, new_angle))
    return angles

def run_test():
    npairs = int(input())
    points = []
    for i in range(npairs*2):
        newp = list(map(int, input().split(' ')))
        points.append((i+1, newp))

    points = sorted(points, key=lambda x: x[1][0])
    excluded = set() 
    pairs = list(range(len(points)))
    for i, p in points: 
        if i in excluded:
            continue
        excluded.add(i)
        angles = get_angles(p, points[i-1:], excluded)
        otheri = sorted(angles, key=lambda x: x[1])[len(angles)//2][0]
        excluded.add(otheri)
        pairs[i-1] = otheri
        pairs[otheri-1] = i
    return pairs

for i in range(int(input())):
    print("Case #{}: {}".format(i+1, run_test()))