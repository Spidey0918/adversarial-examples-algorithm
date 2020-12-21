from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import numpy as np
from dataAnalysis import file2matrix


def showdatas(datingDataMat, datingLabels):
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    fig, axs = plt.subplots(nrows=2, ncols=2, sharex=False,
                            sharey=False, figsize=(13, 8))

    numberOfLabels = len(datingLabels)
    LabelsColors = []
    for i in datingLabels:
        if i == 1:
            LabelsColors.append('black')
        elif i == 2:
            LabelsColors.append('orange')
        elif i == 3:
            LabelsColors.append('red')

    axs[0][0].scatter(x=datingDataMat[:, 0], y=datingDataMat[:,
                                                             1], color=LabelsColors, s=15, alpha=0.5)
    axs0_title_text = axs[0][0].set_title(
        u'每年获得的飞行常客里程数与玩视频游戏所消耗时间占比', FontProperties=font)
    axs0_xlabel_text = axs[0][0].set_xlabel(
        u'每年获得的飞行常客里程数', FontProperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel(
        u'玩视频游戏所消耗时间占', FontProperties=font)
    plt.setp(axs0_title_text, size=9, weight='bold', color='red')
    plt.setp(axs0_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs0_ylabel_text, size=7, weight='bold', color='black')

    axs[0][1].scatter(x=datingDataMat[:, 0], y=datingDataMat[:,
                                                             2], color=LabelsColors, s=15, alpha=0.5)
    axs1_title_text = axs[0][1].set_title(
        u'每年获得的飞行常客里程数与每周消费的冰激凌公升数', FontProperties=font)
    axs1_xlabel_text = axs[0][1].set_xlabel(
        u'每年获得的飞行常客里程数', FontProperties=font)
    axs1_ylabel_text = axs[0][1].set_xlabel(
        u'每周消费的冰激凌公升数', FontProperties=font)
    plt.setp(axs1_title_text, size=9, weight='bold', color='red')
    plt.setp(axs1_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs1_ylabel_text, size=7, weight='bold', color='black')

    axs[1][0].scatter(x=datingDataMat[:, 1], y=datingDataMat[:,
                                                             2], color=LabelsColors, s=15, alpha=0.5)
    axs2_title_text = axs[1][0].set_title(
        u'玩视频游戏所消耗时间占比与每周消费的冰激凌公升数', FontProperties=font)
    axs2_xlabel_text = axs[1][0].set_xlabel(
        u'玩视频游戏所消耗时间占比', FontProperties=font)
    axs2_ylabel_text = axs[1][0].set_ylabel(
        u'每周消费的冰激凌公升数', FontProperties=font)
    plt.setp(axs2_title_text, size=9, weight='bold', color='red')
    plt.setp(axs2_xlabel_text, size=7, weight='bold', color='black')
    plt.setp(axs2_ylabel_text, size=7, weight='bold', color='black')

    didntLike = mlines.Line2D([], [], color='black',
                              marker='.', markersize=6, label='didntLike')
    smallDoses = mlines.Line2D(
        [], [], color='orange', marker='.', markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D(
        [], [], color='red', marker='.', markersize=6, label='largeDoses')

    axs[0][0].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[0][1].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[1][0].legend(handles=[didntLike, smallDoses, largeDoses])

    plt.show()


if __name__ == '__main__':
    filename = r"C:\Users\86180\Desktop\ML in actionVS\KNN\datingTestSet.txt"

    datingDataMat, datingLabels = file2matrix(filename)
    showdatas(datingDataMat, datingLabels)
