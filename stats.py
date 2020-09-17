import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import read_csv

def doStatistics(results):
    writeCSV(toCSV(results))
    doBoxPlot()
    doDistributionPlot()
    printStats()

def exampleDoStatistics():
    print(len(getData()))
    writeCSV(toCSV(getData()))
    doBoxPlot()
    doDistributionPlot()
    printStats()

def doBoxPlot():
    #filePath = getCurrDirPath()+"\\"+'acc_anns.csv'
    
    data = pd.read_csv("outInfo/acc_anns.csv")
    x, y ='ann_name', 'accuracy'
    bplot = sns.boxplot(x=x, y=y, 
                 data=data, 
                 width=0.5,
                 palette="colorblind")
                 
    bplot=sns.swarmplot(x=x, y=y, data=data, color='gray', alpha=0.75)
    #bplot=sns.stripplot(x=x, y=y, data=data, jitter=True, marker='o', alpha=0.5, color='black')
    bplot.get_figure().savefig('outInfo/boxplot.png')

def doDistributionPlot():
    data = pd.read_csv("outInfo/acc_anns.csv")
    
def printStats():
    data = pd.read_csv("outInfo/acc_anns.csv")
    
    maxs = data.groupby(['ann_name']).max()
    means = data.groupby(['ann_name']).mean()
    medians = data.groupby(['ann_name']).median()
    stds = data.groupby(['ann_name']).std()
    vars = data.groupby(['ann_name']).var()
    
    maxs = maxs.rename(index=str, columns={"accuracy": "acc max"})
    means = means.rename(index=str, columns={"accuracy": "acc mean"})
    medians = medians.rename(index=str, columns={"accuracy": "acc median"})
    stds = stds.rename(index=str, columns={"accuracy": "acc std"})
    vars = vars.rename(index=str, columns={"accuracy": "acc var"})
    
    df = pd.concat([maxs, means], axis=1, ignore_index=False)
    df = pd.concat([df, medians], axis=1, ignore_index=False)
    df = pd.concat([df, stds], axis=1, ignore_index=False)
    df = pd.concat([df, vars], axis=1, ignore_index=False)
    
    print(df) 
    
    
def toCSV(data):
    data = list(map(lambda d:d[1], data))
    rows = [["ann_name", "accuracy"],]
    for iteration in data[1:]:
        for i in range(len(iteration)):
            rows.append([data[0][i], iteration[i]])
    return rows

def writeCSV(csvData):
    with open('outInfo/acc_anns.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)

    csvFile.close()


def getData():
    return [
        ['epochs', ['cnn1', 'dnn_huConv', 'dnn_conv', 'cnn2', 'dnn_conv2'], ['descSortedIndexes']],
        [1, [0.9539, 0.9609, 0.9568, 0.9665, 0.9717], [4, 3, 1, 2, 0]],
        [1, [0.9543, 0.9624, 0.9607, 0.9641, 0.9678], [4, 3, 1, 2, 0]],
        [1, [0.9538, 0.9649, 0.9686, 0.9644, 0.9746], [4, 2, 1, 3, 0]],
        [1, [0.9569, 0.9641, 0.9618, 0.959, 0.9699], [4, 1, 2, 3, 0]],
        [1, [0.9607, 0.9659, 0.9668, 0.9536, 0.9644], [2, 1, 4, 0, 3]],
        [1, [0.9594, 0.9726, 0.9698, 0.962, 0.9709], [1, 4, 2, 3, 0]],
        [1, [0.9469, 0.9622, 0.9614, 0.9619, 0.9689], [4, 1, 3, 2, 0]],
        [1, [0.9658, 0.9736, 0.9731, 0.9685, 0.9759], [4, 1, 2, 3, 0]],
        [1, [0.9447, 0.9632, 0.9695, 0.9635, 0.9692], [2, 4, 3, 1, 0]],
        [1, [0.9579, 0.9667, 0.9654, 0.9652, 0.9675], [4, 1, 2, 3, 0]],
        [1, [0.9493, 0.9617, 0.9611, 0.9639, 0.9696], [4, 3, 1, 2, 0]],
        [1, [0.9629, 0.9652, 0.9649, 0.9622, 0.9684], [4, 1, 2, 0, 3]],
        [1, [0.9366, 0.9582, 0.9563, 0.9596, 0.9701], [4, 3, 1, 2, 0]],
        [1, [0.9333, 0.9597, 0.952, 0.9606, 0.9718], [4, 3, 1, 2, 0]],
        [1, [0.925, 0.9598, 0.9609, 0.9589, 0.9667], [4, 2, 1, 3, 0]],
        [1, [0.9598, 0.971, 0.9712, 0.9552, 0.9664], [2, 1, 4, 0, 3]],
        [1, [0.965, 0.9673, 0.9741, 0.9565, 0.9668], [2, 1, 4, 0, 3]],
        [1, [0.9525, 0.9605, 0.9607, 0.9619, 0.9751], [4, 3, 2, 1, 0]],
        [1, [0.9639, 0.9684, 0.9698, 0.9553, 0.9716], [4, 2, 1, 0, 3]],
        [1, [0.9484, 0.9607, 0.9586, 0.9625, 0.9704], [4, 3, 1, 2, 0]],
        [1, [0.9576, 0.9668, 0.9654, 0.9571, 0.9709], [4, 1, 2, 0, 3]],
        [1, [0.9568, 0.9632, 0.9666, 0.9662, 0.9769], [4, 2, 3, 1, 0]],
        [1, [0.9616, 0.9696, 0.9696, 0.9556, 0.9662], [2, 1, 4, 0, 3]],
        [1, [0.9642, 0.9659, 0.9676, 0.9628, 0.9682], [4, 2, 1, 0, 3]],
        [1, [0.9444, 0.9589, 0.9565, 0.9638, 0.9735], [4, 3, 1, 2, 0]],
        [1, [0.9586, 0.9632, 0.9636, 0.9626, 0.9675], [4, 2, 1, 3, 0]],
        [1, [0.9495, 0.9623, 0.9609, 0.959, 0.9691], [4, 1, 2, 3, 0]],
        [1, [0.9632, 0.9655, 0.9679, 0.9592, 0.9663], [2, 4, 1, 0, 3]],
        [1, [0.9048, 0.9376, 0.9396, 0.9682, 0.9747], [4, 3, 2, 1, 0]],
        [1, [0.9607, 0.966, 0.9674, 0.966, 0.976], [4, 2, 3, 1, 0]],
        [1, [0.96, 0.9678, 0.9684, 0.9674, 0.969], [4, 2, 1, 3, 0]],
        [1, [0.9616, 0.9685, 0.9697, 0.9621, 0.9682], [2, 1, 4, 3, 0]],
        [1, [0.9488, 0.9651, 0.9608, 0.9691, 0.9761], [4, 3, 1, 2, 0]],
        [1, [0.9544, 0.9659, 0.9668, 0.9657, 0.973], [4, 2, 1, 3, 0]],
        [1, [0.9397, 0.9547, 0.9543, 0.9487, 0.9664], [4, 1, 2, 3, 0]],
        [1, [0.9352, 0.9666, 0.9664, 0.9607, 0.9683], [4, 1, 2, 3, 0]],
        [1, [0.9547, 0.9648, 0.966, 0.9659, 0.9753], [4, 2, 3, 1, 0]],
        [1, [0.9599, 0.9659, 0.9658, 0.9527, 0.9705], [4, 1, 2, 0, 3]],
        [1, [0.9571, 0.9626, 0.9647, 0.9592, 0.9747], [4, 2, 1, 3, 0]],
        [1, [0.9441, 0.9575, 0.9599, 0.9534, 0.962], [4, 2, 1, 3, 0]],
        [1, [0.9599, 0.9671, 0.9639, 0.9568, 0.9717], [4, 1, 2, 0, 3]],
        [1, [0.9616, 0.9744, 0.974, 0.9703, 0.9771], [4, 1, 2, 3, 0]],
        [1, [0.9532, 0.9635, 0.9653, 0.9563, 0.9708], [4, 2, 1, 3, 0]],
        [1, [0.9671, 0.9711, 0.9735, 0.9608, 0.9699], [2, 1, 4, 0, 3]],
        [1, [0.8999, 0.9241, 0.9337, 0.9677, 0.9715], [4, 3, 2, 1, 0]],
        [1, [0.9526, 0.9634, 0.9608, 0.9713, 0.9776], [4, 3, 1, 2, 0]],
        [1, [0.9415, 0.9621, 0.9596, 0.9656, 0.9755], [4, 3, 1, 2, 0]],
        [1, [0.9581, 0.9645, 0.9647, 0.9677, 0.9743], [4, 3, 2, 1, 0]],
        [1, [0.9516, 0.9645, 0.9644, 0.9447, 0.9666], [4, 1, 2, 0, 3]],
        [1, [0.9622, 0.97, 0.9698, 0.969, 0.9744], [4, 1, 2, 3, 0]],
        [1, [0.9482, 0.9526, 0.9652, 0.9679, 0.9725], [4, 3, 2, 1, 0]],
        [1, [0.9592, 0.9698, 0.9731, 0.9579, 0.9666], [2, 1, 4, 0, 3]],
        [1, [0.9415, 0.9533, 0.9549, 0.9644, 0.9698], [4, 3, 2, 1, 0]],
        [1, [0.9516, 0.9648, 0.9623, 0.9657, 0.97], [4, 3, 1, 2, 0]],
        [1, [0.9661, 0.9734, 0.971, 0.956, 0.9651], [1, 2, 0, 4, 3]],
        [1, [0.9505, 0.9577, 0.9612, 0.9545, 0.9672], [4, 2, 1, 3, 0]],
        
        [1, [0.9613, 0.9714, 0.9685, 0.9642, 0.9717], [4, 1, 2, 3, 0]],
        [1, [0.9627, 0.9665, 0.968, 0.9515, 0.9635], [2, 1, 4, 0, 3]],
        [1, [0.9426, 0.953, 0.9558, 0.9449, 0.9589], [4, 2, 1, 3, 0]],
        [1, [0.9324, 0.9458, 0.9483, 0.9652, 0.9721], [4, 3, 2, 1, 0]],
        [1, [0.9424, 0.9557, 0.9552, 0.9544, 0.9665], [4, 1, 2, 3, 0]],
        [1, [0.9529, 0.9641, 0.9634, 0.9591, 0.962], [1, 2, 4, 3, 0]],
        [1, [0.9161, 0.9367, 0.9379, 0.9634, 0.9706], [4, 3, 2, 1, 0]],
        [1, [0.9534, 0.9663, 0.965, 0.9573, 0.9679], [4, 1, 2, 3, 0]],
        [1, [0.9519, 0.965, 0.9673, 0.9672, 0.9672], [2, 4, 3, 1, 0]],
        [1, [0.959, 0.9633, 0.9644, 0.9543, 0.9702], [4, 2, 1, 0, 3]],
        [1, [0.9612, 0.968, 0.9685, 0.9669, 0.9697], [4, 2, 1, 3, 0]],
        [1, [0.9562, 0.9606, 0.9633, 0.9665, 0.9725], [4, 3, 2, 1, 0]],
        [1, [0.9463, 0.9628, 0.9604, 0.9555, 0.9641], [4, 1, 2, 3, 0]],
        [1, [0.9553, 0.9627, 0.9644, 0.9589, 0.9704], [4, 2, 1, 3, 0]],
        [1, [0.9626, 0.9679, 0.9723, 0.9628, 0.9728], [4, 2, 1, 3, 0]],
        [1, [0.9518, 0.9584, 0.9597, 0.9608, 0.9716], [4, 3, 2, 1, 0]],
        [1, [0.9526, 0.9626, 0.9647, 0.9643, 0.971], [4, 2, 3, 1, 0]],
        [1, [0.9607, 0.9709, 0.9719, 0.9595, 0.9719], [4, 2, 1, 0, 3]],
        [1, [0.9564, 0.9644, 0.9654, 0.9676, 0.9724], [4, 3, 2, 1, 0]],
        [1, [0.9578, 0.9699, 0.9684, 0.9581, 0.9693], [1, 4, 2, 3, 0]],
        [1, [0.9327, 0.9507, 0.9392, 0.9638, 0.9699], [4, 3, 1, 2, 0]],
        [1, [0.9642, 0.9705, 0.9699, 0.9616, 0.9645], [1, 2, 4, 0, 3]],
        [1, [0.9494, 0.9646, 0.9663, 0.9584, 0.9634], [2, 1, 4, 3, 0]],
        [1, [0.9535, 0.9611, 0.9624, 0.9641, 0.9722], [4, 3, 2, 1, 0]],
        [1, [0.9572, 0.9638, 0.9644, 0.9633, 0.9699], [4, 2, 1, 3, 0]],
        [1, [0.964, 0.9696, 0.9703, 0.9696, 0.9753], [4, 2, 3, 1, 0]],
        [1, [0.9579, 0.9704, 0.9717, 0.9652, 0.972], [4, 2, 1, 3, 0]],
        [1, [0.9515, 0.9623, 0.958, 0.9567, 0.964], [4, 1, 2, 3, 0]],
        [1, [0.9634, 0.9709, 0.9715, 0.9586, 0.973], [4, 2, 1, 0, 3]],
        [1, [0.9627, 0.9686, 0.9622, 0.9649, 0.9739], [4, 1, 3, 0, 2]],
        [1, [0.954, 0.9614, 0.9656, 0.9466, 0.9551], [2, 1, 4, 0, 3]],
        [1, [0.9532, 0.9664, 0.9655, 0.959, 0.9702], [4, 1, 2, 3, 0]],
        [1, [0.967, 0.9713, 0.9733, 0.9615, 0.9709], [2, 1, 4, 0, 3]],
        [1, [0.9584, 0.9649, 0.9654, 0.9633, 0.9703], [4, 2, 1, 3, 0]],
        [1, [0.9621, 0.9675, 0.9654, 0.9498, 0.9673], [1, 4, 2, 0, 3]],
        [1, [0.9639, 0.9698, 0.9698, 0.8945, 0.9429], [2, 1, 0, 4, 3]],
        [1, [0.963, 0.9697, 0.9701, 0.9662, 0.9727], [4, 2, 1, 3, 0]],
        [1, [0.9594, 0.9712, 0.9738, 0.9654, 0.9746], [4, 2, 1, 3, 0]],
        [1, [0.9568, 0.9596, 0.9663, 0.9595, 0.9711], [4, 2, 1, 3, 0]],
        [1, [0.9273, 0.9582, 0.9541, 0.9677, 0.9739], [4, 3, 1, 2, 0]],
        [1, [0.9483, 0.9583, 0.9587, 0.9622, 0.9716], [4, 3, 2, 1, 0]],
        [1, [0.9529, 0.9655, 0.9558, 0.962, 0.9739], [4, 1, 3, 2, 0]],
        [1, [0.9526, 0.963, 0.9644, 0.9432, 0.957], [2, 1, 4, 0, 3]],
        [1, [0.9524, 0.9604, 0.9632, 0.9633, 0.9703], [4, 3, 2, 1, 0]],
        [1, [0.9401, 0.9538, 0.9564, 0.9581, 0.9688], [4, 3, 2, 1, 0]],
        [1, [0.9202, 0.9408, 0.9393, 0.9648, 0.9702], [4, 3, 1, 2, 0]],
        [1, [0.9582, 0.9625, 0.9634, 0.9605, 0.9657], [4, 2, 1, 3, 0]],
        [1, [0.9555, 0.9584, 0.9612, 0.961, 0.9676], [4, 2, 3, 1, 0]],
        [1, [0.9587, 0.9627, 0.9623, 0.962, 0.9728], [4, 1, 2, 3, 0]],
    ]