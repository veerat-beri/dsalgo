class DisjointSet:
    def __init__(self):
        self.sets = {}

    # def create_set(self, repr):
    #     self.sets.append(repr)
    #
    # def mergeSets(self, repr1, repr2):
    #     set1 = self.findSet(repr1)
    #     set2 = self.findSet(repr2)
    #     if set1 != set2:
    #         set1.extend(set2)
    #         self.sets.remove(set2)
    #
    # def findSet(self, repr1):
    #     for oneSet in self.sets:
    #         if repr1 in oneSet:
    #             return oneSet
    #
    #
    # def getSets(self):
    #     return self.sets
    def do_union(self, elem1, elem2):
        # path-compressed union

        if self.sets.get(elem1, None) and not self.sets.get(elem2, None):
            elem1_root = self.sets[elem1]
            self.sets[elem2] = elem1_root if elem1_root != -1 else elem1

        elif self.sets.get(elem2, None) and not self.sets.get(elem1, None):
            elem2_root = self.sets[elem2]
            self.sets[elem1] = elem2_root if elem2_root != -1 else elem2

        elif self.sets.get(elem1, None) and self.sets.get(elem2, None):
            self.sets[self.sets[elem2]] = self.sets[elem1]
            self.sets[elem2] = self.sets[elem1]


