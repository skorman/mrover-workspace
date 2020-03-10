import csv

class KDTree:
    def  __init__(self, point_file):
        self.CSV = csv.reader(open(point_file, 'r'))

    def create_tree(self):
        # Read in all of the points from the point_file:
        for row in self.CSV:
            x = float(row[0])
            y = float(row[1])
            z = float(row[2])
            alpha = float(row[3])
            beta = float(row[4])
            gamma = float(row[5])

    
    def traverse_tree(self):
        pass