import numpy as np
from scipy.optimize import newton
from scipy.integrate import quad
# Acceleration Due to Gravity.
# Final Position of the Bead.
x2, y2 = 1, 0.7
def setGravity(gravity):
    """ Sets the Value of the Gravity. """
    # Sets the variable "g" to Global, to be used by other Functions.
    global g
    g = gravity

def Brachistochrone(x2, y2, N=100):
    """ Returns a Brachistochrone Curve from point (0,0) to (x2, y2). """
    # Find the value of Theta.
    def findTheta(theta):
        return y2/x2 - (1-np.cos(theta))/(theta-np.sin(theta))
    theta2 = newton(findTheta, np.pi/2)

    # Find the Radius of Circle Generating the Brachistochrone.
    R = y2 / (1 - np.cos(theta2))

    theta = np.linspace(0, theta2, N)
    x = R * (theta - np.sin(theta))
    y = R * (1 - np.cos(theta))

    # Find the Time of Travel of Brachistochrone & Prints It.
    T = theta2 * np.sqrt(R / g)
    print('T(Brachistochrone) = {:.4f}'.format(T))
    return x, y, T

def Linear(x2, y2, N=100):
    """ Return a Straight Line from (0,0) to (x2, y2). """

    # Gradient of Equation
    m = y2 / x2
    x = np.linspace(0, x2, N)
    # Linear Equation
    y = m*x

    # Find the Time of Travel of a Linear Equation.
    T = np.sqrt(2*(1+m**2)/g/m * x2)
    print('T(Linear) = {:.4f}'.format(T))
    return x, y, T

def Func(x, f, fp):
    """ The Integrand of the Time Integral that Minimizes in Respect to f(x). """

    return np.sqrt((1+fp(x)**2) / (2 * g * f(x)))

def Circle(x2, y2, N=100):
    """ Returns a Circle Curve from point (0,0) to (x2, y2). """

    # Find the Circle's Radius
    r = (x2**2 + y2**2)/2/x2

    def F(x):
        return np.sqrt(2*r*x - x**2)
    def Fp(x):
        return (r-x)/F(x)

    x = np.linspace(0, x2, N)
    y = F(x)

    # Calcualte the Time of Travel by Numerical Inetegration.
    T = quad(Func, 0, x2, args=(F, Fp))[0]
    print('T(Circle) = {:.4f}'.format(T))
    return x, y, T

def Parabola(x2, y2, N=100):
    """ Returns a Parabolic Curve from point (0,0) to (x2, y2). """

    # Set the Constant for the Curve
    c = (y2/x2)**2

    def F(x):
        return np.sqrt(c*x)
    def Fp(x):
        return c/2/F(x)

    x = np.linspace(0, x2, N)
    y = F(x)

    # Calculate the time of travel by numerical integration.
    # Print T(parabola) in 3 significant figures points.
    T = quad(Func, 0, x2, args=(F, Fp))[0]
    print('T(Parabola) = {:.4f}'.format(T))
    return x, y, T
