def calculate_midpoint(points):
    if len(points) == 0:
        print("Empty list.")
        return None
    elif len(points) == 1:
        return points[0]

    import numpy
    try:
        length = max([len(point) for point in points])
        return tuple(numpy.divide([sum(x) for x in zip(*points)], length))
    except ValueError:
        print("Points must have same number of dimensions.")
        return None


def get_centroid_minimum_distance(point, centroids):
    try:
        import numpy
        distances = [numpy.sqrt(sum(numpy.power(numpy.subtract(point, centroid), 2))) for centroid in centroids]
        return centroids[distances.index(min(distances))]
    except ValueError:
        print("Points must have same number of dimensions.")
        return None


def create_initial_centroids(data, number_of_clusters=3):
    # shuffle points
    import random
    random.shuffle(data)

    # create empty clusters
    clusters = []
    for i in range(number_of_clusters):
        clusters.append([])

    # distribute points in clusters
    i = 0
    for point in data:
        clusters[i].append(point)
        i += 1
        if i == number_of_clusters:
            i = 0

    return [calculate_midpoint(cluster) for cluster in clusters]


def internal_kmeans(data, centroids, old_clusters={}):
    # iterate over data, setting each observation to the nearest cluster, based on its distance of the centroid.
    centroids_markers = [get_centroid_minimum_distance(point, centroids) for point in data]

    clusters = {}
    for i, centroid in enumerate(centroids_markers):
        if centroid in clusters:
            clusters[centroid].append(data[i])
        else:
            clusters[centroid] = [data[i]]

    # calculate the new centroids locations based on the mean of the cluster points.
    centroids = [centroid for centroid in [calculate_midpoint(cluster) for cluster in clusters.values()]
                 if centroid is not None]

    if old_clusters != clusters:
        return internal_kmeans(data, centroids, clusters)
    else:
        return clusters


def kmeans(data, number_of_clusters=3):
    # check number of clusters
    if len(data) < number_of_clusters:
        print("Number of points must be greater than number of clusters.")
        return None

    return internal_kmeans(data, create_initial_centroids(data, number_of_clusters))
