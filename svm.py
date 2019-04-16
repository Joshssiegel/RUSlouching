from sklearn import svm
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

def main():
    file_pre = '/home/milkkarten/Open_Pose/RU_Slouching/data/data_preSlouch2019-03-31 18:19.txt'
    file_slouch = '/home/milkkarten/Open_Pose/RU_Slouching/data/data_slouching2019-03-31 18:19.txt'
    X = []
    Y = []
    i = 0
    raw_data_pre = np.genfromtxt(file_pre, delimiter=',', unpack=True)
    for x, y in zip(raw_data_pre[0], raw_data_pre[1]):
        X.append([x,y])
        Y.append(0)
    raw_data_slouch = np.genfromtxt(file_slouch, delimiter=',', unpack=True)
    for x, y in zip(raw_data_slouch[0], raw_data_slouch[1]):
        X.append([x,y])
        Y.append(1)
    X = np.array(X)
    Y = np.array(Y)
    X[:,0] = np.divide(X[:, 0], np.max(X[:, 0]))
    X[:,1] = np.divide(X[:, 1], np.max(X[:, 1]))

    clf = svm.SVC(kernel='linear', C=1)
    clf.fit(X,Y)
    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(np.min(X[:, 0]), np.max(X[:, 0]))
    yy = a * xx - clf.intercept_[0] / w[1]

    h0 = plt.plot(xx, yy, 'k-', label="non weighted div")
    print(X[:, 0])
    print(X[:, 1])
    plt.scatter(X[:, 0], X[:, 1], c = Y)
    plt.legend()
    plt.show()
    return

if __name__ == '__main__':
    main()
