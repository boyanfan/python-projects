#
# ELEC 292 Final Project - Group 53
# Created by Boyan Fan, Naman Nagia, Walker Yee on 04/02/2024
#

import tkinter as tk
import app_utility as ut
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import FeatureExtractionandMLModel as model

from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Desktop app for deploying the final model
# This app will accept an input file in CSV format and generate a CSV file as the output
# Which includes the labels for walking or jumping, for each window in the input file
# It also generates a plot which represents the outputs
class App:
    def __init__(self):
        # Initialize the app by building a root view, providing a title and a default size
        self.root = tk.Tk()
        self.root.geometry(f"{ut.DEFAULT_WIDTH}x{ut.DEFAULT_HEIGHT}")
        self.root.title("ELEC 292 Final Project")
        self.root.resizable(True, True)
        self.result = "Unknown"

        # Initialize the views
        self.file = None
        self.plot_view = None
        self.plot = None
        self.promotion = None
        self.canvas = None


        # An area for accepting a csv file to display and generate an output file
        self.file_input_view = tk.Frame(self.root)
        self.file_input_view.pack(side='left')

        # Create the file input view for asking users to provide a csv file
        self.create_file_input_view()

        # Configuration view for displaying buttons in a vertical layout
        self.configuration_view = tk.Frame(self.root, height=ut.DEFAULT_HEIGHT, width=ut.DEFAULT_WIDTH*0.2)
        self.configuration_view.pack(side='left', padx=(ut.DEFAULT_PADDING-5, 0))

        # Generate button for generating the output csv file
        self.generate_button = tk.Button(self.configuration_view, text="Generate", state='disabled')
        self.generate_button.grid(row=0, column=0, sticky=tk.W+tk.E)

        # Clear button for clearing all the input and generated output files
        clear_button = tk.Button(self.configuration_view, text="Clear")
        clear_button.grid(row=1, column=0, sticky=tk.W+tk.E)
        clear_button.bind('<Button-1>', self.clear)

        # Generate the placeholder if there is no csv to plot
        self.placeholder()

        # Create the entire interface layout
        self.root.mainloop()

    def open_file(self, event):
        file_path = filedialog.askopenfilename(title="Select a File",
                                               filetypes=[("Comma Separated Values", "*.csv"),])
        if file_path is not None:
            self.file = pd.read_csv(file_path)
            self.plot_file()

            self.predict()

            self.canvas.destroy()
            self.promotion.destroy()

            self.canvas = tk.Canvas(self.file_input_view, height=ut.DEFAULT_HEIGHT, width=ut.DEFAULT_WIDTH * 0.4)
            self.canvas.grid(row=0, column=0)
            self.canvas.bind('<Button-1>', self.open_file)

            # Create an area for accepting a csv file
            ut.rounded_rectangle(
                canvas=self.canvas, pad_x=ut.DEFAULT_PADDING, pad_y=ut.DEFAULT_PADDING, width=ut.DEFAULT_WIDTH * 0.4,
                height=ut.DEFAULT_HEIGHT - ut.DEFAULT_PADDING, radius=25, fill=ut.POSITIVE_BACKGROUND
            )

            self.promotion = tk.Label(
                self.file_input_view, text=f"Your csv file has been open. " + self.result,
                font=ut.DEFAULT_FONT, bg=ut.POSITIVE_BACKGROUND, fg=ut.POSITIVE
            )
            self.promotion.grid(row=0, column=0)

            self.generate_button.destroy()
            self.generate_button = tk.Button(self.configuration_view, text="Generate")
            self.generate_button.grid(row=0, column=0, sticky=tk.W + tk.E)
            self.generate_button.bind('<Button-1>', self.save_file)

    def predict(self):
        array = np.array(self.file)  # convert segment to array
        dataset = pd.DataFrame(array)  # convert array to dataframe
        features = ['x mean', 'y mean', 'z mean', 'x max', 'y max', 'z max', 'x min', 'y min', 'z min', 'x range',
                    'y range', 'z range', 'x median', 'y median', 'z median', 'x var', 'y var', 'z var', 'x skew',
                    'y skew', 'z skew', 'x std', 'y std', 'z std', 'isJump']
        feature_extracted_array = np.array([features])
        xmean = dataset[1].mean()
        ymean = dataset[2].mean()
        zmean = dataset[3].mean()
        xmax = dataset[1].max()
        ymax = dataset[2].max()
        zmax = dataset[3].max()
        xmin = dataset[1].min()
        ymin = dataset[2].min()
        zmin = dataset[3].min()
        xrange = (dataset[1].max() - (dataset[1].min()))
        yrange = (dataset[2].max()) - (dataset[2].min())
        zrange = (dataset[3].max()) - (dataset[3].min())
        xmed = dataset[1].median()
        ymed = dataset[2].median()
        zmed = dataset[3].median()
        xvar = dataset[1].var()
        yvar = dataset[2].var()
        zvar = dataset[3].var()
        xskew = dataset[1].skew()
        yskew = dataset[2].skew()
        zskew = dataset[3].skew()
        xstd = dataset[1].std()
        ystd = dataset[2].std()
        zstd = dataset[3].std()
        _isJump = 0
        feature_array = np.array(
            [xmean, ymean, zmean, xmax, ymax, zmax, xmin, ymin, zmin, xrange, yrange, zrange, xmed, ymed, zmed, xvar,
             yvar, zvar, xskew, yskew, zskew, xstd, ystd, zstd, _isJump])
        feature_extracted_array = np.vstack((feature_extracted_array, feature_array))
        feature_extracted_array = np.delete(feature_extracted_array, 0, 0)
        features_dataset = pd.DataFrame(feature_extracted_array)
        features_dataset.dropna(inplace=True)
        X_data = features_dataset.iloc[:, 1:-1]

        prediction = model.clf.predict(X_data)

        if prediction[0] == '1.0':
            self.result = "This file is for \"Jumping\"!"
            self.file['isJump'] = 1
        else:
            self.result = "This file is for \"Walking\"!"
            self.file['isJump'] = 0

    def plot_file(self):
        if self.file is not None:
            plot_width = ut.DEFAULT_WIDTH*0.5
            plot_height = ut.DEFAULT_HEIGHT-ut.DEFAULT_PADDING*2

            self.plot_view.destroy()

            fig, ax = plt.subplots(1, figsize=(plot_width / 100, plot_height / 100))
            ax.plot(self.file.iloc[:, 0], self.file.iloc[:, 1], c='red')
            ax.plot(self.file.iloc[:, 0], self.file.iloc[:, 2], c='blue')
            ax.plot(self.file.iloc[:, 0], self.file.iloc[:, 3], c='green')
            plot_content_view = FigureCanvasTkAgg(fig, master=self.root)
            plot_content_view.draw()
            plot_content_view.get_tk_widget().pack(padx=ut.DEFAULT_PADDING, pady=ut.DEFAULT_PADDING)

            self.plot = plot_content_view.get_tk_widget()
            self.plot.configure(width=plot_width, height=plot_height)
            self.plot.pack(padx=ut.DEFAULT_PADDING, pady=ut.DEFAULT_PADDING)

    def save_file(self, event):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Comma Separated Values", "*.csv"),])

        if file_path:
            self.file.to_csv(file_path, index=False)

    def clear(self, event):
        if self.plot_view is not None:
            self.plot_view.destroy()
        if self.plot is not None:
            self.plot.destroy()

        self.canvas.destroy()
        self.promotion.destroy()
        self.generate_button.destroy()

        self.placeholder()
        self.create_file_input_view()

        self.generate_button = tk.Button(self.configuration_view, text="Generate", state='disabled')
        self.generate_button.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.generate_button.bind('<Button-1>', self.save_file)

    def create_file_input_view(self):
        # Create the canvas for the file input view to draw the input area
        self.canvas = tk.Canvas(self.file_input_view, height=ut.DEFAULT_HEIGHT, width=ut.DEFAULT_WIDTH*0.4)
        self.canvas.grid(row=0, column=0)
        self.canvas.bind('<Button-1>', self.open_file)

        # Create an area for accepting a csv file
        ut.rounded_rectangle(
            canvas=self.canvas, pad_x=ut.DEFAULT_PADDING, pad_y=ut.DEFAULT_PADDING, width=ut.DEFAULT_WIDTH*0.4,
            height=ut.DEFAULT_HEIGHT-ut.DEFAULT_PADDING, radius=25, fill=ut.DEFAULT_BACKGROUND
        )

        # Ask user to provide a csv file
        self.promotion = tk.Label(
            self.file_input_view, text="Click to open your csv file", font=ut.DEFAULT_FONT, bg=ut.DEFAULT_BACKGROUND,
            fg=ut.SECONDARY
        )
        self.promotion.grid(row=0, column=0)

    # Create a placeholder for the plot view if there is no csv file to plot
    def placeholder(self):
        self.plot_view = tk.Frame(self.root)
        self.plot_view.pack(side='left')

        placeholder = tk.Canvas(self.plot_view, height=ut.DEFAULT_HEIGHT, width=ut.DEFAULT_WIDTH*0.6)
        placeholder.grid(row=0, column=0)

        ut.rounded_rectangle(
            canvas=placeholder, pad_x=ut.DEFAULT_PADDING, pad_y=ut.DEFAULT_PADDING, width=ut.DEFAULT_WIDTH * 0.5,
            height=ut.DEFAULT_HEIGHT - ut.DEFAULT_PADDING, radius=25, fill=ut.DEFAULT_BACKGROUND
        )

        tip = tk.Label(
            self.plot_view, text="Open a csv file to plot the figure                          ",
            bg=ut.DEFAULT_BACKGROUND, font=ut.DEFAULT_FONT, fg=ut.SECONDARY
        )
        tip.grid(row=0, column=0)

# Run the app defined above
App()