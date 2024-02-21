def maxpoints(points):
    h = {}

    for point in points:
        x = point[0]
        y = point[1]

        m = y/x

        print(y//x)

        if m in h:
            h[m] += 1

        else:
            h[m] = 1

    return max(h.values())

point1 = [[1,1],[2,2],[3,3]]
point2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]

output = maxpoints(point2)
print(output)