class Place:
    #Determine items a Place would help
    def __init__(self, name="", country="", priority=0, is_visited=False):
        self.name  = name
        self.country  = country
        self.priority  = priority
        self.is_visited = is_visited

    #Display a string when a Place is inputted
    def __str__(self):
        if self.is_visited == 'v':
            return ("You have visited {} City, {} ".format(self.name,self.country))
        else:
            is_priority = "not important"
            if self.is_important():
                is_priority = "important"
            return ("You have not visited {} City, {}. That's {} ".format(self.name,self.country, is_priority))

    def is_important(self):
        #determine if a place is considered "important"
        if self.priority <= 2:
            return True
        return False
        
    def mark_visited(self):
        #Mark the Place as visited
        self.is_visited = "v"
        return self.is_visited
        
    def mark_unvisited(self):
        #Mark the Place as unvisited
        self.is_visited = "n"
        return self.is_visited