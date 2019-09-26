

from place import Place  # import Place class
from operator import attrgetter  # import Attribute Getter
import csv


class PlaceCollection:
    """
    initiate the self attribute PlaceCollection
    :return: None
    """

    def __init__(self):
        self.places = []

    def load_places(self, name):
        """
        Load the Places from csv file and append them to places
        """
        # open the file
        with open('places', 'r') as csvFile:
            lines = csv.reader(csvFile)
            for line in lines:
                loaded_place = Place(line[0], line[1], int(line[2]), line[3])
                self.places.append(loaded_place)
        # close the file
        csvFile.close()

    def sort(self, key):
        """
        Sort the places based on the sort_choice selected
        :param key: self, key
        :return: none
        """
        self.places = sorted(self.places, key=attrgetter(key, "priority"))

    def add_place(self, newPlaces):
        # add the inputted place to the place list
        self.places.append(newPlaces)

    def save_places(self,place):
        # save changes made to the Places and then out file

        csv_string = ""
        for each in self.places:
            csv_string += "{},{},{},{}\n".format(each.name, each.country, each.priority, each.is_visited)
        out_file = open(place, 'w')
        out_file.seek(0)
        out_file.truncate()
        out_file.write(csv_string)
        out_file.close()  # close the file

    def get_number_unvisited_places(self):
        return sum(p.is_visited == 'n' for p in self.places)

    def print(self):
        for s in self.places:
            print(s)