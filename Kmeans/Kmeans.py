import copy
import random


class Kmeans:

    data = []
    groups = []
    centroids = []
    groupsChanged = True
    def __init__(self, fileName: str, k: int):
        self.readFile(fileName)
        self.groups = [[] for _ in range(k)]
        self.initializeGroups(k)
        # for group in self.groups:
        #     for vec in group:
        #         print(vec)
        #     print()
    def readFile(self, filename):
        file = open(filename)
        for line in file:
            splitStr = line.split(",")
            self.vecLength = len(splitStr)
            row = []
            for val in splitStr:
                row.append(float(val))
            self.data.append(row)
            # print(row)

    def initializeGroups(self, k):
        for idx, group in enumerate(self.groups):
            group.append(self.data[idx])
        for row in self.data[k:]:
            randNum = random.randint(0, k-1)
            for i in range(k):
                if i == randNum:
                    self.groups[i].append(row)

    def calculateCentroid(self, group):
        transposedGroup = [[group[j][i] for j in range(len(group))] for i in range(len(group[0]))]
        centroid = []
        for vec in transposedGroup:
            sum = 0
            for val in vec:
                sum += val
            mean = sum / len(vec)
            centroid.append(mean)
        return centroid

    def assignGroup(self, vec):
        distances = []
        for centroid in self.centroids:
            distance = 0.
            for idx, val in enumerate(centroid):
                valSquared = (vec[idx] - centroid[idx]) ** 2
                distance += valSquared
            distances.append(distance)
            # print(distances)
        idx = distances.index(min(distances))
        self.groups[idx].append(vec)

    def run(self, k):
        while (self.groupsChanged):
            groupsBefore = copy.deepcopy(self.groups)
            print(groupsBefore)
            for group in self.groups:
                self.centroids.append(self.calculateCentroid(group))
            # print(self.centroids)
            for group in self.groups:
                group.clear()
            for vec in self.data:
                self.assignGroup(vec)
            for group in self.groups:
                if len(group) == 0:
                    self.initializeGroups(k)
            # print("Assigning groups.")
            groupsAfter = copy.deepcopy(self.groups)
            print(groupsAfter)
            if groupsBefore == groupsAfter:
                self.groupsChanged = False
                # print("End of clustering")
            self.centroids.clear()





