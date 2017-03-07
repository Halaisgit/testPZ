import matplotlib.pyplot as plt
from sklearn import svm

def load_data(filename):
    X = []
    for line in open(filename):
        tokens = line.split()
        X.append([float(tokens[0]),float(tokens[1]),float(tokens[2])])
    return(X)

def draw_data(X):
    for [x,y,c] in X:
        if c == 1:
            plt.plot(x, y, 'ro', color='red')
        elif c == -1:
            plt.plot(x, y, 'ro', color='yellow')
        else:
            plt.plot(x, y, 'ro', color='blue')
    plt.axis([-10, 10, -10, 10])
    plt.show()

def classify(X):
    clf = svm.SVC()
    Xs = []
    Ys = []
    for [x,y,c] in X:
        if c == 0 or c == 1:
            Xs.append([x,y])
            Ys.append(c)
    clf.fit(Xs,Ys)
    for i in range(len(X)):
        if X[i][2] == -1:
            X[i][2] = clf.predict([X[i][0],X[i][1]])
    return(X)


def main():
    X = load_data('train')
    draw_data(X)
    X = classify(X)
    draw_data(X)

main()

