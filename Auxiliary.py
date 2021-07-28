def BootstrapLinearRegression(xdata, ydata, bootstrapIterations=1e5, getDistribtion=False):
    '''Linear Regression with Parametric Bootstrapping.
========
Attributes:
xdata: List, 1d np.array; Sample points.
ydata: 2d np.array; Observed values for each sample point for each column.
bootstrapIterations: int; Number of bootstrapping iterations to be conducted.
getDistribtion: Bool; Option to return array of regression parameters from bootstrapping procedure.
========
Return: Tuble of polynormial parameters (mean, slope). If `getDistribtion=True` the tuble will also contain
numpy array of parameters from the individual bootstrapping iterations.
========
References:
https://bit.ly/3xHB1H1 # Bootstrap for dummies.
https://bit.ly/32WHIXd # Towards data science.
'''
    from copy import deepcopy
    import numpy as _np
    
    assert _np.shape(xdata)[0] == _np.shape(ydata)[1], 'xdata axis=0 size must equal ydata axis=1 size!'
    
    slopes = []; intercepts = []
    origin = deepcopy(ydata)
    for __ in range(int(bootstrapIterations)):
        for i, point in enumerate(origin.T):
            ydata.T[i] = _np.random.choice(point, size=len(point), replace=True)
            
        fit = _np.polyfit(xdata, ydata.mean(axis=0), 1)
        slopes.append(fit[0]); intercepts.append(fit[1])
        
    slopes = _np.array(slopes); meanSlope = slopes.mean(); stdSlope = slopes.std()
    intercepts = _np.array(intercepts); meanIntercept = intercepts.mean(); stdIntercept = intercepts.std()
        
    if getDistribtion:
        return ((meanSlope, stdSlope, slopes), (meanIntercept, stdIntercept, intercepts))
        
    
    return ((meanSlope, stdSlope), (meanIntercept, stdIntercept))

def getAvgVolume(filename, Nruns=25, volcolumn=4, returning='print'):
    '''Return the average volume from independent simulations in Ångstrom.
The function will search in the folders /#run/filename
========
Attributes:
filename: String; filename out output.
Nruns: Int; Number of independent runs.
volcolumn: Ont; Index of the column containing volmetric data (starting index is 0).
returning: String; Option to return the result as a print statement or as a float.
           If `returning='print'` return is a print statement, if `returning='float'` return is a float.
========
Return: Print statement or float depending on value of `returning`.
========
'''
    import numpy as _np
    volume_sum = 0
    for run in range(Nruns):
        volume = _np.loadtxt('{run}/{filename}'.format(run=run, filename=filename),
                             usecols=volcolumn, skiprows=1, unpack=True)
        volume_sum += volume.mean()
    if returning == 'print':
        print('{volume}'.format(volume=volume_sum/Nruns*1000))
    elif returning =='float':
        return volume_sum/Nruns*1000
    else:
        raise ValueError('Illegal value of `returning`.')
