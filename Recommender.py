# author: Yifan Mao
# date: 4/24/2024
# Recommender class
import os
import tkinter
from tkinter import filedialog
import tkinter.messagebox
from Book import Book
from Show import Show
from Media import Media


class Recommender:
    # An appropriate constructor that instantiates three dictionaries
    # ▪ one to store Book objects, where the book’s id is the key and the value is the object
    # ▪ one to store Show objects, where the show’s id is the key and the value is the object
    # ▪ one to store dictionaries keeping track of associations, where a show or book id is the
    # key and the value is a dictionary
    # • For the inner dictionary, the key should be a show or book id and the value is the
    # number of times the outer id and inner id are associated
    def __init__(self):
        # {id1: Book object, id2: Book object, id3: Book object}
        self.__books = {}
        # {id1: Show object, id2: Show object, id3: Show object}
        self.__shows = {}
        # {id1: {id2: 1, id3: 2}, id2: {id1: 1, id3: 3}, id3: {id1: 2, id2: 3}}
        self.__associations = {}

    def loadBooks(self):
        # Prompts the user for the name of the file using an appropriate filedialog, and if the
        # user does not choose an existing file, it should repeatedly prompt the user for a file in
        # the same way
        # ▪ Opens and reads the file one entry at a time
        # ▪ Stores the entry for each book in a Book object
        # ▪ Stores each Book object in the appropriate dictionary using the book’s ID as the key
        # and the Book object as the value
        # ▪ Close the file once all the data has been read in
        while True:
            filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Book file")
            if os.path.exists(filename):
                break
        with open(filename, 'r') as file:
            file.readline()
            for line in file:
                line = line.strip().split(',')
                self.__books[line[0]] = Book(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7],
                                             line[8], line[9], line[10])

    def loadShows(self):
        """
        Prompts the user for the name of the file using an appropriate filedialog, and if the
        :return: nothing
        """
        while True:
            filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select show file")
            if os.path.exists(filename):
                break
        with open(filename, 'r') as file:
            file.readline()
            for line in file:
                line = line.strip().split(',', 12)
                self.__shows[line[0]] = Show(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7],
                                             line[8], line[9], line[10], line[11], line[12])

    def loadAssociations(self):
        while True:
            filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select associations file")
            if os.path.exists(filename):
                break
        # {id1: {id2: 1, id3: 2}, id2: {id1: 1, id3: 3}, id3: {id1: 2, id2: 3}}
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip().split(',')
                # ▪ Using the first id as a key, determine if there is a dictionary associated with it
                if line[0] not in self.__associations:
                    # create a new dictionary and then add the second id to the new dictionary
                    # so that the second id is associated with the value 1
                    self.__associations[line[0]] = {}
                    self.__associations[line[0]][line[1]] = 1
                else:
                    if line[1] not in self.__associations[line[0]]:
                        self.__associations[line[0]][line[1]] = 1
                    else:
                        self.__associations[line[0]][line[1]] += 1
                # ▪ Using the second id as a key, determine if there is a dictionary associated with it
                if line[1] not in self.__associations:
                    # create a new dictionary and then add the first id to the new dictionary
                    # so that the first id is associated with the value 1
                    self.__associations[line[1]] = {}
                    self.__associations[line[1]][line[0]] = 1
                else:
                    if line[0] not in self.__associations[line[1]]:
                        self.__associations[line[1]][line[0]] = 1
                    else:
                        self.__associations[line[1]][line[0]] += 1
        # print(self.__associations)

    def getMovieList(self):
        """
        :return: string
        """
        return_string = ''
        title_list = []
        duration_list = []
        for key in self.__shows:
            if self.__shows[key].get_type() == 'Movie':
                title_list.append(self.__shows[key].get_title())
                duration_list.append(self.__shows[key].get_duration())
        max_len1 = max([len(title) for title in title_list])
        max_len2 = max([len(duration) for duration in duration_list])
        return_string += f"{'Title'.ljust(max_len1)}{'Duration'.ljust(max_len2)}\n"
        for i in range(len(title_list)):
            return_string += f"{title_list[i].ljust(max_len1)}{duration_list[i].ljust(max_len2)}\n"
        return return_string

    def getTVList(self):
        return_string = ''
        title_list = []
        duration_list = []
        for key in self.__shows:
            if self.__shows[key].get_type() == 'TV Show':
                title_list.append(self.__shows[key].get_title())
                duration_list.append(self.__shows[key].get_duration())
        max_len1 = max([len(title) for title in title_list])
        max_len2 = max([len(duration) for duration in duration_list])
        return_string += f"{'Title'.ljust(max_len1)}{'Duration'.ljust(max_len2)}\n"
        for i in range(len(title_list)):
            return_string += f"{title_list[i].ljust(max_len1)}{duration_list[i].ljust(max_len2)}\n"
        return return_string

    def getBookList(self):
        return_string = ''
        title_list = []
        num_pages_list = []
        for key in self.__books:
            title_list.append(self.__books[key].get_title())
            num_pages_list.append(self.__books[key].get_num_pages())
        max_len1 = max([len(title) for title in title_list])
        max_len2 = max([len(num_pages) for num_pages in num_pages_list])
        return_string += f"{'Title'.ljust(max_len1)}{'Num Pages'.ljust(max_len2)}\n"
        for i in range(len(title_list)):
            return_string += f"{title_list[i].ljust(max_len1)}{num_pages_list[i].ljust(max_len2)}\n"
        return return_string

    def getMovieStats(self):
        rate_dict = {}
        count = 0
        duration = 0
        director_dict = {}
        actor_dict = {}
        genre_dict = {}
        for key in self.__shows:
            if self.__shows[key].get_type() == 'Movie':
                count += 1
                duration += int(self.__shows[key].get_duration()[0:-4])
                if self.__shows[key].get_rating() != '':
                    if self.__shows[key].get_rating() not in rate_dict:
                        rate_dict[self.__shows[key].get_rating()] = 1
                    else:
                        rate_dict[self.__shows[key].get_rating()] += 1
                director = self.__shows[key].get_directors()
                if director != '':
                    # print(director)
                    for d in director.strip().split('\\'):
                        # print(d)
                        if d not in director_dict:
                            director_dict[d] = 1
                        else:
                            director_dict[d] += 1
                actor = self.__shows[key].get_actors()
                if actor != '':
                    for a in actor.split('\\'):
                        if a not in actor_dict:
                            actor_dict[a] = 1
                        else:
                            actor_dict[a] += 1
                genre = self.__shows[key].get_genres()
                if genre != '':
                    for g in genre.split('\\'):
                        if g not in genre_dict:
                            genre_dict[g] = 1
                        else:
                            genre_dict[g] += 1
        output = ""
        output += "Ratings:\n"
        for key in rate_dict:
            output += f"{key} {rate_dict[key] / count * 100:.2f}%\n"
        output += f"Average Duration: {duration / count}\n"
        output += f"Most Prolific Director: {max(director_dict, key=director_dict.get)}\n"
        output += f"Most Prolific Actor: {max(actor_dict, key=actor_dict.get)}\n"
        output += f"Most Popular Genre: {max(genre_dict, key=genre_dict.get)}\n"
        return output

    def getMovieRating(self):
        rate_dict = {}
        for key in self.__shows:
            if self.__shows[key].get_type() == 'Movie':
                if self.__shows[key].get_rating() not in rate_dict:
                    rate_dict[self.__shows[key].get_rating()] = 1
                else:
                    rate_dict[self.__shows[key].get_rating()] += 1

        return rate_dict.keys()

    def getMovieRatingpercount(self):
        rate_dict = {}
        for key in self.__shows:
            if self.__shows[key].get_type() == 'Movie':
                if self.__shows[key].get_rating() not in rate_dict:
                    rate_dict[self.__shows[key].get_rating()] = 1
                else:
                    rate_dict[self.__shows[key].get_rating()] += 1
        return rate_dict.values()

    def getTVStats(self):
        # Rating for tv shows (G, PG, R, etc…) and the number of times a particular rating appears
        # as a percentage of all of the ratings for tv shows, with two decimals of precision
        # ▪ Average number of seasons for tv shows, with two decimals of precision
        # The actor who has acted in the most tv shows
        # ▪ The most frequent tv show genre
        rate_dict = {}
        count = 0
        duration = 0
        actor_dict = {}
        genre_dict = {}
        for key in self.__shows:
            if self.__shows[key].get_type() == 'TV Show':
                count += 1
                # 1 Season
                duration += int(self.__shows[key].get_duration()[0:-7])
                if self.__shows[key].get_rating() != '':
                    if self.__shows[key].get_rating() not in rate_dict:
                        rate_dict[self.__shows[key].get_rating()] = 1
                    else:
                        rate_dict[self.__shows[key].get_rating()] += 1
                actor = self.__shows[key].get_actors()
                if actor != '':
                    for a in actor.split('\\'):
                        if a not in actor_dict:
                            actor_dict[a] = 1
                        else:
                            actor_dict[a] += 1
                genre = self.__shows[key].get_genres()
                if genre != '':
                    for g in genre.split('\\'):
                        if g not in genre_dict:
                            genre_dict[g] = 1
                        else:
                            genre_dict[g] += 1
        output = ""
        output += "Ratings:\n"
        for key in rate_dict:
            output += f"{key} {rate_dict[key] / count * 100:.2f}%\n"
        output += f"Average Duration: {duration / count}\n"
        output += f"Most Prolific Actor: {max(actor_dict, key=actor_dict.get)}\n"
        output += f"Most Popular Genre: {max(genre_dict, key=genre_dict.get)}\n"
        return output

    def getTVRating(self):
        rate_dict = {}
        for key in self.__shows:
            if self.__shows[key].get_type() == 'TV Show':
                if self.__shows[key].get_rating() not in rate_dict:
                    rate_dict[self.__shows[key].get_rating()] = 1
                else:
                    rate_dict[self.__shows[key].get_rating()] += 1
        return rate_dict.keys()

    def getTVRatingpercount(self):
        rate_dict = {}
        for key in self.__shows:
            if self.__shows[key].get_type() == 'TV Show':
                if self.__shows[key].get_rating() not in rate_dict:
                    rate_dict[self.__shows[key].get_rating()] = 1
                else:
                    rate_dict[self.__shows[key].get_rating()] += 1
        return rate_dict.values()

    def getBookStats(self):
        # The average page count, with two decimals of precision
        # ▪ The author who has written the most books
        # ▪ The publisher who has published the most books
        page_count = 0
        author_dict = {}
        publisher_dict = {}
        for key in self.__books:
            page_count += int(self.__books[key].get_num_pages())
            author = self.__books[key].get_authors()
            if author != '':
                for author in author.split('\\'):
                    if author not in author_dict:
                        author_dict[author] = 1
                    else:
                        author_dict[author] += 1
            publisher = self.__books[key].get_publisher()
            if publisher != '':
                if publisher not in publisher_dict:
                    publisher_dict[publisher] = 1
                else:
                    publisher_dict[publisher] += 1
        output = ""
        output += f"Average Page Count: {page_count / len(self.__books):.2f}\n"
        output += f"Most Prolific Author: {max(author_dict, key=author_dict.get)}\n"
        output += f"Most Prolific Publisher: {max(publisher_dict, key=publisher_dict.get)}\n"
        return output

    def searchTVMovie(self, type, title, director, actor, genre):
        """
        :param type:
        :param title:
        :param director:
        :param actor:
        :param genre:
        :return: return_string
        """
        result_list = []
        if type == 'TV Show':
            pass
        elif type == 'Movie':
            pass
        else:
            # spawn a
            # showerror messagebox and inform the user the need to select Movie or TV Show
            # from Type first, and return the string No Results
            tkinter.messagebox.showerror("Error", "Please select Movie or TV Show from Type first")
            return "No Results"
        # If the strings representing title, director, actor, and genre are all empty, spawn a
        # showerror messagebox and inform the user the need to enter information for the
        # Title, Directory, Actor and/or Genre first, and return the string No Results
        if title == '' and director == '' and actor == '' and genre == '':
            tkinter.messagebox.showerror("Error",
                                         "Please enter information for the Title, Director, Actor and/or Genre first")
            return "No Results"
        # Otherwise, search through the dictionary of shows and select all objects that adhere to
        # the user’s data
        for key in self.__shows:
            if self.__shows[key].get_type() == type:
                if title != '' and title.lower() not in self.__shows[key].get_title().lower():
                    continue
                if director != '' and director.lower() not in self.__shows[key].get_directors().lower():
                    continue
                if actor != '' and actor.lower() not in self.__shows[key].get_actors().lower():
                    continue
                if genre != '' and genre.lower() not in self.__shows[key].get_genres().lower():
                    continue
                result_list.append(self.__shows[key])
        #  Return a string containing the Title, Director, Actors, and Genre (with those titles at the
        # top) in neat, even columns, whose width is determined based on the length of the
        # entries in the data
        return_string = ''
        title_list = []
        director_list = []
        actor_list = []
        genre_list = []
        for show in result_list:
            title_list.append(show.get_title())
            director_list.append(show.get_directors())
            actor_list.append(show.get_actors())
            genre_list.append(show.get_genres())
        max_len1 = max([len(title) for title in title_list])
        max_len2 = max([len(director) for director in director_list])
        max_len3 = max([len(actor) for actor in actor_list])
        max_len4 = max([len(genre) for genre in genre_list])
        return_string += f"{'Title'.ljust(max_len1)}{'Director'.ljust(max_len2)}{'Actor'.ljust(max_len3)}{'Genre'.ljust(max_len4)}\n"
        for i in range(len(title_list)):
            return_string += f"{title_list[i].ljust(max_len1)}{director_list[i].ljust(max_len2)}{actor_list[i].ljust(max_len3)}{genre_list[i].ljust(max_len4)}\n"
        return return_string

    def searchBooks(self, title, author, publisher):
        result_list = []
        if title == '' and author == '' and publisher == '':
            tkinter.messagebox.showerror("Error",
                                         "Please enter information for the Title, Author and/or Publisher first")
            return "No Results"
        for key in self.__books:
            if title != '' and title.lower() not in self.__books[key].get_title().lower():
                continue
            if author != '' and author.lower() not in self.__books[key].get_authors().lower():
                continue
            if publisher != '' and publisher.lower() not in self.__books[key].get_publisher().lower():
                continue
            result_list.append(self.__books[key])
        return_string = ''
        title_list = []
        author_list = []
        publisher_list = []
        for book in result_list:
            title_list.append(book.get_title())
            author_list.append(book.get_authors())
            publisher_list.append(book.get_publisher())
        max_len1 = max([len(title) for title in title_list])
        max_len2 = max([len(author) for author in author_list])
        max_len3 = max([len(publisher) for publisher in publisher_list])
        return_string += f"{'Title'.ljust(max_len1)}{'Author'.ljust(max_len2)}{'Publisher'.ljust(max_len3)}\n"
        for i in range(len(title_list)):
            return_string += f"{title_list[i].ljust(max_len1)}{author_list[i].ljust(max_len2)}{publisher_list[i].ljust(max_len3)}\n"
        return return_string

    def getRecommendations(self, type, title):
        """
        :param type:
        :param title:
        :return: string
        """
        # ▪ If the type is Movie or TV Show, search through the shows dictionary and determine the
        # id associated with that title
        # self.__books look like {id1: Book object, id2: Book object, id3: Book object}
        # self.__shows look like {id1: Show object, id2: Show object, id3: Show object}
        # self.__associations look like {id1: {id2: 1, id3: 2}, id2: {id1: 1, id3: 3}, id3: {id1: 2, id2: 3}}
        id = ''
        output = ''
        if type == 'Movie/TV Show':
            # search through the shows dictionary and determine the id associated with that title
            if title == '':
                tkinter.messagebox.showerror("Error", "Please enter a title")
                return "No Recommendations"
            else:
                for key in self.__shows:
                    if title == self.__shows[key].get_title():
                        id = key
                        break
                if id == '':
                    tkinter.messagebox.showerror("Error", "No such title found")
                    return "No Recommendations"

                for key in self.__books:
                    if self.__books[key].get_id() in self.__associations[id].keys():
                        output += f"{self.__books[key]}\n"
                return output
        if type == 'Book':
            if title == '':
                tkinter.messagebox.showerror("Error", "Please enter a title")
                return "No Recommendations"
            else:
                for key in self.__books:
                    if title == self.__books[key].get_title():
                        id = key
                        break
                if id == '':
                    tkinter.messagebox.showerror("Error", "No such title found")
                    return "No Recommendations"
                for key in self.__shows:
                    if self.__shows[key].get_id() in self.__associations[id].keys():
                        output += f"{self.__shows[key]}\n"
                return output

        if type == "":
            tkinter.messagebox.showerror("Error", "Please select Movie/TV Show or Book")
            return "No Recommendations"
