import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def polynomialRegession(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), LinearRegression(**kwargs))


def makedata(n, err=1.0, rseed=1):
    rng = np.random.RandomState(rseed)
    x = rng.rand(n, 1)**2
    y = 10-1./(x.ravel()+0.1)
    if err > 0:
        y += err*rng.randn(n)
    return x, y


x, y = makedata(40)
xtest = np.linspace(-0.1, 1.1, 500)[:, None]
plt.scatter(x.ravel(), y, color='black')
axis = plt.axis()
for degree in [1, 3, 5]:
    ytest = polynomialRegession(degree).fit(x, y).predict(xtest)
    plt.plot(xtest.ravel(), ytest, label='degree={0}'.format(degree))
from sklearn.learning_cu
plt.xlim(-0.1, 1.0)
plt.ylim(-2, 12)
plt.legend(loc='best')
plt.show()
