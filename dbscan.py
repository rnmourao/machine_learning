def neighbors_of(point, data, radius):
    from scipy.spatial import distance
    return [p for p in data if distance.euclidean(p, point) <= radius and p != point]


def dbscan(data, radius=1, min_points=3):
    clusters = []
    visited = []
    noise = []

    for point in data:
        if point not in visited:
            visited.append(point)
            neighbors = neighbors_of(point, data, radius)
            if len(neighbors) < min_points:
                noise.append(point)
            else:
                cluster = [point]
                for n in neighbors:
                    if n not in visited:
                        visited.append(n)
                        neighbors_of_my_neighbor = neighbors_of(n, data, radius)
                        if len(neighbors_of_my_neighbor) >= min_points:
                            neighbors += neighbors_of_my_neighbor
                    if len([cluster for cluster in clusters if n in cluster]) == 0:
                        cluster.append(n)
                clusters.append(cluster)

    return {'clusters': clusters, 'noise': noise}
