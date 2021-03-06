# -*- coding: utf-8 -*-`
"""This example demonstrates how to fully customize violin plots.

This code is copy and revised from https://cloud.tencent.com/developer/article/1486970

"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

class ViolinPlot(object):
    """This class is used to plot violin
    """

    def plot(self, data, xlabel=None, ylabel=None, xlabelsize=10, ylabelsize=10, xticklabel=None, yticklabel=None, xticklabel_rotation=45):
        """Plot

        Parameters:
        ----------
            data: list
                data to plot
            xlabel: str
                xlabel
            ylabel: str
                ylabel
            ....
        """

        fig, self.ax = plt.subplots(nrows=1, ncols=1, figsize=(5, 6), sharey=True)
        
        # ax.set_title('')
        data = list([np.array(d) for  d in data])
        sns.violinplot(data=data, linewidth=1, ax=self.ax)
        # set style for the axes
        self.set_axis_style(xlabel, ylabel, xlabelsize, ylabelsize, xticklabel, yticklabel, xticklabel_rotation)
        plt.subplots_adjust(bottom=0.15, wspace=0.05)
        # plt.show()

    def set_axis_style(self, xlabel, ylabel, xlabelsize, ylabelsize, xticklabel, yticklabel, xticklabel_rotation):
        self.ax.get_xaxis().set_tick_params(direction='out')
        self.ax.xaxis.set_ticks_position('bottom')
        if xticklabel:
            self.ax.set_xticks(np.arange(0, len(xticklabel) ))
            self.ax.set_xticklabels(xticklabel, rotation=xticklabel_rotation, ha="right")
            # self.ax.set_xlim(0.25, len(xlabel) + 0.75)
        if xlabel:
            self.ax.set_xlabel(xlabel, fontsize=xlabelsize)
        if yticklabel:
            self.ax.set_yticks(np.arange(0, len(yticklabel)))
            self.ax.set_yticklabels(yticklabel)
            # self.ax.set_ylim(0.25, len(ylabel) + 0.75)
        if ylabel:
            self.ax.set_ylabel(ylabel, fontsize=ylabelsize)

class ViolinPlotMatplotlib(object):
    """ ViolinPlot customization 

    """


    def adjacent_values(self, vals, q1, q3):
        upper_adjacent_value = q3 + (q3 - q1) * 1.5
        upper_adjacent_value = np.clip(upper_adjacent_value, q3, vals[-1])
    
        lower_adjacent_value = q1 - (q3 - q1) * 1.5
        lower_adjacent_value = np.clip(lower_adjacent_value, vals[0], q1)
        return lower_adjacent_value, upper_adjacent_value

    def plot(self, data, **kwargs):
        """ Plot violin

        Parameters:
        ----------
            data: list
                each item in list is a array
            **kwargs: matplotlib kwargs
        """

        # Sorted data so that adjacent_values method can get sorted array
        data = [sorted(d) for d in data]

        parts = plt.violinplot(data, showmeans=False, showmedians=False, showextrema=False, **kwargs)

        quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
        whiskers = np.array([
            self.adjacent_values(sorted_array, q1, q3)
            for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
        whiskersMin, whiskersMax = whiskers[:, 0], whiskers[:, 1]

        if 'positions' in kwargs.keys():
            inds = kwargs['positions']
        else:
            inds = np.arange(1, len(medians) + 1)
        
        plt.scatter(inds, medians, marker='o', color='white', s=10, zorder=3)
        plt.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
        plt.vlines(inds, whiskersMin, whiskersMax, color='k', linestyle='-', lw=1)

if __name__ == "__main__":
    np.random.seed(666)
    data = [np.random.randn(100,), np.random.randn(100,)]
    violin = ViolinPlotMatplotlib()
    violin.plot(data)
    plt.show()
