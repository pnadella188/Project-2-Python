# author: Yifan Mao,Praneeth Nadella
# date: 4/24/2024
# Show class subclass of Media

from Media import Media


class Show(Media):
    def __init__(self, id, type, title, directors, actors, average_rating, country, date_added, release_year, rating,
                 duration, genres, description):
        """
        :param id:
        :param type:
        :param title:
        :param directors:
        :param actors:
        :param average_rating:
        :param country:
        :param date_added:
        :param release_year:
        :param rating:
        :param duration:
        :param genres:
        :param description:
        """
        super().__init__(id, title, average_rating)
        self.__type = type
        self.__directors = directors
        self.__actors = actors
        self.__country = country
        self.__date_added = date_added
        self.__release_year = release_year
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description

    def get_type(self):
        return self.__type

    def get_directors(self):
        return self.__directors

    def get_actors(self):
        return self.__actors

    def get_country(self):
        return self.__country

    def get_date_added(self):
        return self.__date_added

    def get_release_year(self):
        return self.__release_year

    def get_rating(self):
        return self.__rating

    def get_duration(self):
        return self.__duration

    def get_genres(self):
        return self.__genres

    def get_description(self):
        return self.__description

    def set_type(self, type):
        self.__type = type

    def set_directors(self, directors):
        self.__directors = directors

    def set_actors(self, actors):
        self.__actors = actors

    def set_country(self, country):
        self.__country = country

    def set_date_added(self, date_added):
        self.__date_added = date_added

    def set_release_year(self, release_year):
        self.__release_year = release_year

    def set_rating(self, rating):
        self.__rating = rating

    def set_duration(self, duration):
        self.__duration = duration

    def set_genres(self, genres):
        self.__genres = genres

    def set_description(self, description):
        self.__description = description

    def __str__(self):
        output = 'type: \n' + self.get_type() + '\n'
        output += 'title: \n' + self.get_title() + '\n'
        output += 'directors: \n' + self.get_directors() + '\n'
        output += 'actors: \n' + self.get_actors() + '\n'
        output += 'average_rating: \n' + self.get_average_rating() + '\n'
        output += 'country: \n' + self.get_country() + '\n'
        output += 'date_added: \n' + self.get_date_added() + '\n'
        output += 'release_year: \n' + self.get_release_year() + '\n'
        output += 'rating: \n' + self.get_rating() + '\n'
        output += 'duration: \n' + self.get_duration() + '\n'
        output += 'genres: \n' + self.get_genres() + '\n'
        output += 'description: \n' + self.get_description() + '\n'
        return output
