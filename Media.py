# author: Yifan Mao,Praneeth Nadella
# date: 4/24/2024
# media class for project2 super class for Movie and TvShow

class Media:
    def __init__(self, id, title, average_rating):
        self._id = id
        self._title = title
        self._average_rating = average_rating

    # Accessor methods
    def get__id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_average_rating(self):
        return self._average_rating

    # Mutator methods
    def set__id(self, id):
        """
        Set the media ID.

        Args:
            _id (int or str): The media ID to set.
        """
        self._id = id

    def set_title(self, title):
        """
        Set the title of the media.

        Args:
            title (str): The title to set.
        """
        self._title = title

    def set_average_rating(self, average_rating):
        self._average_rating = average_rating
