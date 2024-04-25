# author: Yifan Mao
# date: 4/24/2024
# media class for project2 super class for Movie and TvShow

class Media:
    def __init__(self, id, title, average_rating):
        self._id = id
        self._title = title
        self._average_rating = average_rating

    def get_id(self):
        return self._id

    def get_title(self):
        return self._title

    def get_average_rating(self):
        return self._average_rating

    def set_id(self, id):
        self._id = id

    def set_title(self, title):
        self._title = title

    def set_average_rating(self, average_rating):
        self._average_rating = average_rating
