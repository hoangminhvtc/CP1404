"""
Name: Dam Hoang Minh
Date: 13558538
Student ID : 13358538
Brief Project Description: This project will create a Graphical User Interface program based
on the list of Place in assignment Travel Tracker 2.0.
"""

# Importing classes from each module
from kivy.app import App
from kivy.lang import Builder
from placecollection import PlaceCollection
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from place import Place
from kivy.uix.button import Button
import pathlib



# Create your main program in this file, using the PlaceApp class


class PlaceApp(App):  # Class refering to the Kivy app
    """

    Main program:
    Display a list of Place in a GUI model using Kivy app

    """

    message = StringProperty()  # Define first status text
    message2 = StringProperty()  # Define second status text
    current_sort = StringProperty()  # Define current sorting of song list
    sort_choices = ListProperty()  # Define sorting options of song list

    def __init__(self, **kwargs):
        """
        Initiate place_list to PlaceCollection class
        Initiate sort_choices as an array
        Initiate the current sorting option as "priority"
        Initiate the function load_places to load csv file
        :param kwargs:
        returns None
        """
        super(PlaceApp, self).__init__(**kwargs)
        self.place_list = PlaceCollection()
        self.sort_choices = ["name", "country", "priority", "is_visited"]
        self.current_sort = self.sort_choices[2]
        self.path = str(pathlib.Path(__file__).resolve().parent ) + "\\places.csv"
        self.place_list.load_places(self.path)

    def build(self):
        """
        Build the Kivy GUI
        :return: widgets of the GUI
        """
        self.learn___ = "TravelTracker"  # Name the GUI's name
        self.title = self.learn___
        self.root = Builder.load_file('app.kv')  # Connect to Kivy app
        self.create_widgets()  # Create widgets in Kivy GUI
        return self.root

    def change_sort(self, sorting_choice):
        """
        Function to change the sorting of the Place list
        :param sorting_choice: Based on what choice the user selects, the Place list will be sorted that way
        :return: sorted Place list
        """
        self.message = "Places have been sorted by: {}".format(sorting_choice)
        self.place_list.sort(sorting_choice)
        self.root.ids.entriesBox.clear_widgets()
        self.create_widgets()
        sort_index = self.sort_choices.index(sorting_choice)
        self.current_sort = self.sort_choices[sort_index]

    def blank(self):
        """
        Clear all inputs after clicking the Clear button
        :return: blanks at inputs
        """
        self.root.ids.place_name.text = ''  # Empty the song title input
        self.root.ids.place_country.text = ''  # Empty the song artist input
        self.root.ids.place_priority.text = ''  # Empty the song year input

    def create_widgets(self):
        """
        Create widgets that lists the Places from the csv file
        :return: Places list widgets
        """

        for place in self.place_list.places:  # Loop from the first song to the last song within the song list

            name = place.name  # Dim the name of each song
            country = place.country  # Dim the country of each song
            priority = place.priority  # Dim the priority of each song
            is_visited = place.is_visited  # Dim the Place to either be visited or not visited
            display_text = self.generateDisplayText(name, country, priority,
                                                    is_visited)  # display what should be added to the widget

            if is_visited == 'v':
                # Condition when the place is visited,  format their background color (Velvet)
                button_color = self.getColor(is_visited)
            else:
                button_color = self.getColor(is_visited)  

            # By clicking a Place, that Place will be visited/unvisited
            temp_button = Button(text=display_text, id=place.name,
                                 background_color=button_color) 
            temp_button.bind(on_press=self.press_entry)  # Display the message of the GUI status

            self.root.ids.entriesBox.add_widget(temp_button)  # Apply to the Kivy app   
        # Display the number of places still to visit      
        self.message = "Place to visit: {}.".format(self.place_list.get_number_unvisited_places())
        

    def generateDisplayText(self, name, country, priority, is_visited): #Formating any text displayed in the messages
        if is_visited == 'v':
            display_text = "{} in {}, priority {} (visited) ".format(name, country, priority)
        else:
            display_text = "{} in {}, priority {}".format(name, country, priority)

        return display_text

    def getColor(self, is_visited): #Display colors of the Place widgets
        if is_visited == 'v':
            button_color = [1, 0, 0, 1]
        else:
            button_color = [0, 0, 1, 1]
        return button_color

    def press_entry(self, button):              #Function that displays the 2nd message
        buttonID = button.id                #Determine the id on the widget buttons
        selectedPlace = Place()
        for place in self.place_list.places:
        #Loop the Place within the Place list

            if buttonID == place.name:
                selectedPlace = place
                break
           
        message ="" 
        #Mark the Place visited/unvisited 
        if selectedPlace.is_visited == 'v':
            selectedPlace.mark_unvisited()
            if selectedPlace.is_important():
                message ="You need to visited {}.Get going!".format(selectedPlace.name) 
            else:
                message= "You need to visited {}.".format(selectedPlace.name)    
        else:
            selectedPlace.mark_visited()
            if selectedPlace.is_important():
                message = "You visited {}.Great travelling!".format(selectedPlace.name)
            else:
                message = "You visited {}.".format(selectedPlace.name)    
        self.root.ids.entriesBox.clear_widgets()    #Apply to Kivy GUI
        self.create_widgets()
        self.message2 = message    

    def add_place(self):
        """
        Function allows user to add any Place they want
        :return: Add the Place inputted to the Place list
        """

        #Check for empty inputs
        if self.root.ids.place_name.text == "" or self.root.ids.place_country.text == "" or self.root.ids.place_priority.text == "":
            self.root.ids.status2.text = "All fields must be completed"
            return
        try:
            #Define Place items inputted
            place_name = str(self.root.ids.place_name.text)
            place_country = str(self.root.ids.place_country.text)
            place_priority = int(self.root.ids.place_priority.text)
            #Check If priority items inputted is less than 1 
            assert place_priority > 0
            is_visited = "n"

            #Add the Place inputted to the Place list
            self.place_list.add_place(Place(place_name, place_country, place_priority, is_visited))
            temp_button = Button(
                text=self.generateDisplayText(place_name, place_country, place_priority, is_visited))
            temp_button.bind(on_release=self.press_entry)

            #Format the new Place items
            temp_button.background_color = self.getColor(is_visited)
            self.root.ids.entriesBox.add_widget(temp_button)

            #Empty the inputs after adding the Place
            self.root.ids.place_name.text = ""
            self.root.ids.place_country.text = ""
            self.root.ids.place_priority.text = ""

        except ValueError: #Display error when priority input is not a number
            self.message2 = "Please enter a valid priority"
        except AssertionError : #Display error when priority input is less than 1 
            self.message2 = "Priority must be > 0"

    def on_stop(self): #stop the GUI and save changes
        self.place_list.save_places(self.path)

#Run the Kivy Gui
PlaceApp().run()
