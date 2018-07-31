from numpy import arange, array, ones
from numpy.linalg import lstsq
import time
def leastsquareslinefit(sequence,seq_range):
    """Return the parameters and error for a least squares line fit of one segment of a sequence"""
    x = arange(seq_range[0],seq_range[1]+1)
    y = array(sequence[seq_range[0]:seq_range[1]+1])
    A = ones((len(x),2),float)
    A[:,0] = x
    (p,residuals, rank, s) = lstsq(A,y)
    try:
        error = residuals[0]
    except IndexError:
        error = 0.0
    return (p,error)

def stats(name, mse, start_time, segments, points):
    print("\n\n",'-'*len(name),sep='')
    print(name)
    print('-'*len(name),sep='')
    print("MSE\t\t\t: %.2f" % mse)
    print("Segments\t\t: %d" % len(segments))
    print("Run time\t\t: %.2f" % (time.time()-start_time))
    print("MSE\t\t\t: %.2f" % mse_calculator(segments, points))
    print('-'*len(name),sep='')

def mse_calculator(segments, points):
    mse = 0
    for segment in segments:
        mse = mse +  leastsquareslinefit(points, (int(segment[0]), int(segment[2])))[1]
    return mse/len(segments)

