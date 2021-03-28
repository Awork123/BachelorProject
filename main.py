#!/usr/bin/env python3
import pandas as pd
import numpy as np
from sklearn import linear_model
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#df = pd.read_csv("C:\Users\andre\PycharmProjects\pythonProject\IMD_movies.csv")
#sf = pd.read_csv("C:\Users\andre\PycharmProjects\pythonProject\IMDb_ratings.csv")

df['votessq'] = df['votes'] ** 2
# print(df.genre.to_string(index=False))

# print(sf.head())

# here we have 2 input variables for multiple regression.
# If you just want to use one variable for simple linear regression,
# then use X = df['Interest_Rate'] for example.Alternatively,
# you may add additional variables within the brackets
X = df[['duration', 'votes', 'votessq']].astype(float)
# ccccX['votes'] = np.log(X['votes'])
print(X['votes'].max())
# output variable (what we are trying to predict)
Y = sf['weighted_average_vote'].astype(float)

# plt.scatter(sf['weighted_average_vote'], df['duration'], color='green', s=3)
# plt.title('average vote vs duration', fontsize=14)
# plt.xlabel('average vote', fontsize=14)
# plt.ylabel('duration', fontsize=14)
# plt.grid(True)
# plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

# GUI
root = tk.Tk()

canvas1 = tk.Canvas(root, width=500, height=300)
canvas1.pack()

Intercept_result = ('Intercept: ', regr.intercept_)
label_Intercept = tk.Label(root, text=Intercept_result, justify='center')
canvas1.create_window(260, 220, window=label_Intercept)

Coefficients_result = ('Coefficients: ', regr.coef_)
label_Coefficients = tk.Label(root, text=Coefficients_result, justify='center')
canvas1.create_window(260, 240, window=label_Coefficients)

label1 = tk.Label(root, text='Type Duration: ')
canvas1.create_window(100, 87, window=label1)

entry1 = tk.Entry(root)
canvas1.create_window(270, 90, window=entry1)

label2 = tk.Label(root, text='Type Votes: ')
canvas1.create_window(110, 120, window=label2)

entry2 = tk.Entry(root)
canvas1.create_window(270, 120, window=entry2)


def values():
    global new_duration
    new_duration = float(entry1.get())

    global new_votes
    new_votes = float(entry2.get())

    new_votes_sq = new_votes ** 2

    Prediction_result = ('Predicted rating: ', regr.predict([[new_duration, new_votes, new_votes_sq]]))
    label_Prediction = tk.Label(root, text=Prediction_result, bg='orange')
    canvas1.create_window(260, 280, window=label_Prediction)


button1 = tk.Button(root, text='Predict rating', command=values, bg='orange')
canvas1.create_window(270, 150, window=button1)

# plot 1st scatter
figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df['duration'].astype(float), sf['weighted_average_vote'].astype(float), color='r', s=2)
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax3.legend(['Average votes'])
ax3.set_xlabel('Duration')
ax3.set_title('Duration Vs. Average votes')

# plot 2nd scatter
figure4 = plt.Figure(figsize=(5, 4), dpi=100)
ax4 = figure4.add_subplot(111)
ax4.scatter(df['votes'].astype(float), sf['weighted_average_vote'].astype(float), color='g', s=2)
scatter4 = FigureCanvasTkAgg(figure4, root)
scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
ax4.legend(['Average votes'])
ax4.set_xlabel('Amount of votes')
ax4.set_title('Amount of votes Vs. Average votes')

root.mainloop()
