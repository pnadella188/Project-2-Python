# author: Yifan Mao
# date: 4/24/2024
# RecommenderGUI

import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from PIL import Image, ImageTk
import os
from Recommender import Recommender


class RecommenderGUI:
    def __init__(self):
        self.recommender = Recommender()
        self.root = Tk()
        self.root.title('Recommender System')
        self.root.geometry('1200x800')

        # One notebook for both Movies and Books tabs
        self.notebook = ttk.Notebook(self.root)
        # self.notebook.pack()

        # Movie tab
        self.movie_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.movie_frame, text='Movies')
        self.movie_list_text = ScrolledText(self.movie_frame, wrap=WORD)
        self.movie_list_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.movie_list_text.config(state=DISABLED)
        self.movie_list_text.pack(expand=True, fill='both')
        self.movie_stats_text = ScrolledText(self.movie_frame, wrap=WORD)
        self.movie_stats_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.movie_stats_text.config(state=DISABLED)
        self.movie_stats_text.pack(expand=True, fill='both')

        # Show tab
        self.show_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.show_frame, text='Shows')
        self.show_list_text = ScrolledText(self.show_frame, wrap=WORD)
        self.show_list_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.show_list_text.config(state=DISABLED)
        self.show_list_text.pack(expand=True, fill='both')
        self.show_stats_text = ScrolledText(self.show_frame, wrap=WORD)
        self.show_stats_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.show_stats_text.config(state=DISABLED)
        self.show_stats_text.pack(expand=True, fill='both')

        # Book tab
        self.book_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.book_frame, text='Books')
        self.book_list_text = ScrolledText(self.book_frame, wrap=WORD)
        self.book_list_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.book_list_text.config(state=DISABLED)
        self.book_list_text.pack(expand=True, fill='both')
        self.book_stats_text = ScrolledText(self.book_frame, wrap=WORD)
        self.book_stats_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.book_stats_text.config(state=DISABLED)
        self.book_stats_text.pack(expand=True, fill='both')

        # search movies or tv tab
        self.search_media_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.search_media_frame, text='Search Media')
        self.search_area = ttk.Frame(self.search_media_frame)
        self.result_area = ttk.Frame(self.search_media_frame)
        self.search_media_text = ScrolledText(self.result_area, wrap=WORD)
        self.search_media_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.search_media_text.config(state=DISABLED)
        self.search_media_type_label = Label(self.search_area, text='Media Type')
        self.search_media_type_label.grid(row=0, column=0)
        self.search_media_type = Combobox(self.search_area, values=['Movie', 'TV Show'])
        self.search_media_type.grid(row=0, column=1)
        self.search_media_title_label = Label(self.search_area, text='Title')
        self.search_media_title_label.grid(row=1, column=0)
        self.search_media_title = Entry(self.search_area, width=50)
        self.search_media_title.grid(row=1, column=1)
        self.search_media_director_label = Label(self.search_area, text='Director')
        self.search_media_director_label.grid(row=2, column=0)
        self.search_media_director = Entry(self.search_area, width=50)
        self.search_media_director.grid(row=2, column=1)
        self.search_media_actor_label = Label(self.search_area, text='Actor')
        self.search_media_actor_label.grid(row=3, column=0)
        self.search_media_actor = Entry(self.search_area, width=50)
        self.search_media_actor.grid(row=3, column=1)
        self.search_media_genre_label = Label(self.search_area, text='Genre')
        self.search_media_genre_label.grid(row=4, column=0)
        self.search_media_genre = Entry(self.search_area, width=50)
        self.search_media_genre.grid(row=4, column=1)
        self.search_media_button = Button(self.search_area, text='Search Media', command=self.search_media)
        self.search_media_button.grid(row=5, column=0, columnspan=2)
        self.search_media_text.pack(expand=True, fill='both')
        self.search_area.pack()
        self.result_area.pack(expand=True, fill='both')

        # search books tab
        self.search_books_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.search_books_frame, text='Search Books')
        self.search_area = ttk.Frame(self.search_books_frame)
        self.result_area = ttk.Frame(self.search_books_frame)
        self.search_books_title_label = Label(self.search_area, text='Title')
        self.search_books_title_label.grid(row=0, column=0)
        self.search_books_title = Entry(self.search_area, width=50)
        self.search_books_title.grid(row=0, column=1)
        self.search_books_author_label = Label(self.search_area, text='Author')
        self.search_books_author_label.grid(row=1, column=0)
        self.search_books_author = Entry(self.search_area, width=50)
        self.search_books_author.grid(row=1, column=1)
        self.search_books_publisher_label = Label(self.search_area, text='Publisher')
        self.search_books_publisher_label.grid(row=2, column=0)
        self.search_books_publisher = Entry(self.search_area, width=50)
        self.search_books_publisher.grid(row=2, column=1)
        self.search_books_button = Button(self.search_area, text='Search Books', command=self.search_books)
        self.search_books_button.grid(row=3, column=0, columnspan=2)
        self.search_books_text = ScrolledText(self.result_area, wrap=WORD)
        self.search_books_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.search_books_text.config(state=DISABLED)
        self.search_books_text.pack(expand=True, fill='both')
        self.search_area.pack()
        self.result_area.pack(expand=True, fill='both')

        # recommender tab
        self.recommend_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.recommend_frame, text='Recommendations')
        self.search_area = ttk.Frame(self.recommend_frame)
        self.search_type_label = Label(self.search_area, text='Type')
        self.search_type = Combobox(self.search_area, values=['Movie/TV Show', 'Book'])
        self.search_type_label.grid(row=0, column=0)
        self.search_type.grid(row=0, column=1)
        self.search_title_label = Label(self.search_area, text='Title')
        self.search_title = Entry(self.search_area, width=50)
        self.search_title_label.grid(row=1, column=0)
        self.search_title.grid(row=1, column=1)
        self.search_recommend_button = Button(self.search_area, text='Recommend', command=self.search_recommend)
        self.search_recommend_button.grid(row=2, column=0, columnspan=2)
        self.result_area = ttk.Frame(self.recommend_frame)
        self.recommend_text = ScrolledText(self.result_area, wrap=WORD)
        self.recommend_text.insert(INSERT, 'default text informing the user that no data has been loaded yet\n')
        self.recommend_text.config(state=DISABLED)
        self.recommend_text.pack(expand=True, fill='both')
        self.search_area.pack()
        self.result_area.pack(expand=True, fill='both')

        # bottom buttons
        self.bottom_frame = ttk.Frame(self.root)
        self.load_show_button = Button(self.bottom_frame, text='Load Shows', command=self.load_shows)
        self.load_show_button.grid(row=0, column=0, padx=80)
        self.load_book_button = Button(self.bottom_frame, text='Load Books', command=self.load_books)
        self.load_book_button.grid(row=0, column=1, padx=80)
        self.load_recommend_button = Button(self.bottom_frame, text='Load Recommendations',
                                            command=self.load_recommendations)
        self.load_recommend_button.grid(row=0, column=2, padx=80)
        self.info_button = Button(self.bottom_frame, text='Info', command=self.show_info)
        self.info_button.grid(row=0, column=3, padx=80)
        self.quit_button = Button(self.bottom_frame, text='Quit', command=self.root.quit)
        self.quit_button.grid(row=0, column=4, padx=80)

        # Run the main application loop
        self.bottom_frame.pack(expand=True, fill='both', side='bottom')
        self.notebook.pack(expand=True, fill='both')
        self.root.mainloop()

    def load_shows(self):
        self.recommender.loadShows()
        movie = self.recommender.getMovieList()  #str
        # print(movie)
        show = self.recommender.getTVList()  #str
        movie_stats = self.recommender.getMovieStats()  #str
        show_stats = self.recommender.getTVStats()  #str
        self.movie_stats_text.config(state=NORMAL)
        self.movie_list_text.config(state=NORMAL)
        self.show_list_text.config(state=NORMAL)
        self.show_stats_text.config(state=NORMAL)

        self.movie_list_text.delete(1.0, END)
        self.show_list_text.delete(1.0, END)
        self.movie_stats_text.delete(1.0, END)
        self.show_stats_text.delete(1.0, END)

        self.movie_list_text.insert(INSERT, movie)
        self.show_list_text.insert(INSERT, show)
        self.movie_stats_text.insert(INSERT, movie_stats)
        self.show_stats_text.insert(INSERT, show_stats)

        self.movie_stats_text.config(state=DISABLED)
        self.movie_list_text.config(state=DISABLED)
        self.show_list_text.config(state=DISABLED)
        self.show_stats_text.config(state=DISABLED)
        data1 = self.recommender.getMovieRatingpercount()
        data2 = self.recommender.getTVRatingpercount()
        label1 = self.recommender.getMovieRating()
        label2 = self.recommender.getTVRating()
        pie_frame = ttk.Frame(self.notebook)
        self.notebook.add(pie_frame, text='pie')
        fig1 = Figure(figsize=(12,12), dpi=50)
        ax1 = fig1.add_subplot(111)
        ax1.pie(data1, labels=label1, autopct='%1.2f%%', startangle=140)
        ax1.set_title("movie rating")

        # Create a figure for the second pie chart
        fig2 = Figure(figsize=(12, 12), dpi=50)
        ax2 = fig2.add_subplot(111)
        ax2.pie(data2, labels=label2, autopct='%1.2f%%', startangle=140)
        ax2.set_title("tv rating")

        # Function to draw matplotlib figures on Tkinter canvas
        def draw_figure(canvas, figure):
            figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
            figure_canvas_agg.draw()
            figure_canvas_agg.get_tk_widget().pack(side=LEFT)
            return figure_canvas_agg

        # Create the Tkinter canvas
        canvas = Canvas(pie_frame, width=1200, height=500)
        canvas.pack()

        # Draw figures on the canvas
        draw_figure(canvas, fig1)
        draw_figure(canvas, fig2)

    def load_books(self):
        self.recommender.loadBooks()
        book = self.recommender.getBookList()  #str
        book_stats = self.recommender.getBookStats()  #str

        self.book_list_text.config(state=NORMAL)
        self.book_stats_text.config(state=NORMAL)

        self.book_list_text.delete(1.0, END)
        self.book_stats_text.delete(1.0, END)

        self.book_list_text.insert(INSERT, book)
        self.book_stats_text.insert(INSERT, book_stats)

        self.book_list_text.config(state=DISABLED)
        self.book_stats_text.config(state=DISABLED)

    def load_recommendations(self):
        self.recommender.loadAssociations()

    def show_info(self):
        messagebox.showinfo('Info', 'This is a recommender system')

    def search_media(self):
        media_type = self.search_media_type.get()
        title = self.search_media_title.get()
        director = self.search_media_director.get()
        actor = self.search_media_actor.get()
        genre = self.search_media_genre.get()

        self.search_media_text.config(state=NORMAL)

        self.search_media_text.delete(1.0, END)
        searched_media_list = self.recommender.searchTVMovie(media_type, title, director, actor, genre)  #str
        self.search_media_text.insert(INSERT, searched_media_list)

        self.search_media_text.config(state=DISABLED)

    def search_books(self):
        title = self.search_books_title.get()
        author = self.search_books_author.get()
        publisher = self.search_books_publisher.get()
        searched_books_list = self.recommender.searchBooks(title, author, publisher)  #str

        self.search_books_text.config(state=NORMAL)

        self.search_books_text.delete(1.0, END)
        self.search_books_text.insert(INSERT, searched_books_list)

        self.search_books_text.config(state=DISABLED)

    def search_recommend(self):
        type = self.search_type.get()
        title = self.search_title.get()
        recommendations = self.recommender.getRecommendations(type, title)  #str

        self.recommend_text.config(state=NORMAL)

        self.recommend_text.delete(1.0, END)
        self.recommend_text.insert(INSERT, recommendations)

        self.recommend_text.config(state=DISABLED)


def main():
    RecommenderGUI()


if __name__ == '__main__':
    main()
