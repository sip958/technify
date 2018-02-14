import talib as ta


# output: upperband, middleband, lowerband
def BBANDS(col, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    values = ta.BBANDS(col, timeperiod, nbdevup, nbdevdn, matype)
    return {"bbands_ub":values[0], "bbands_mb":values[1], "bbands_lb":values[2]}


def DEMA(col, timeperiod=30):
    values = ta.DEMA(col, timeperiod)
    return {"dema":values}


def EMA(col, timeperiod=30):
    values = ta.EMA(col, timeperiod)
    return {"ema":values}


def HT_TRENDLINE(col):
    return {"trendline":ta.HT_TRENDLINE(col)}


def KAMA(col, timeperiod=30):
    values = ta.KAMA(col, timeperiod)
    return {"kama": values}


def MA(col, timeperiod=30):
    values = ta.MA(col, timeperiod)
    return {"ma":values}


def MAMA(col, fastlimit=0.05, slowlimit=0.05):
    values = ta.MAMA(col, fastlimit, slowlimit)  # output mama, fama
    return {"mama":values[0], "fama":values[1]}


def MAVP(real, periods, minperiod=2, maxperiod=30, matype=0):
    values = ta.MAVP(real, periods, minperiod, maxperiod, matype)
    return {"mavp":values}


def MIDPOINT(col, timeperiod=14):
    values = ta.MIDPOINT(col, timeperiod)
    return {"midpoint":values}


def MIDPRICE(high, low, timeperiod=14):
    return {"midprice": ta.MIDPRICE(high, low, timeperiod)}


def SAR(high, low, acceleration=0.02, maximum=0.2):
    return {"sar":ta.SAR(high, low, acceleration, maximum)}


def SAREXT(high, low, startvalue=0, offsetonreverse=0, accelerationinitlong=0.02, accelerationlong=0.02,
           accelerationmaxlong=0.2, accelerationinitshort=0.02, accelerationshort=0.02, accelerationmaxshort=0.2):
    values = ta.SAREXT(high, low, startvalue, offsetonreverse, accelerationinitlong, accelerationlong,
                     accelerationmaxlong, accelerationinitshort, accelerationshort, accelerationmaxshort)
    return {"sarext":values}


def SMA(col, timeperiod=30):
    return {"sma":ta.SMA(col, timeperiod)}


def T3(col, timeperiod=5, vfactor=0.7):
    return {"t3": ta.T3(col, timeperiod, vfactor)}


def TEMA(col, timeperiod=30):
    return {"tema": ta.TEMA(col, timeperiod)}


def TRIMA(col, timeperiod=30):
    return {"trima": ta.TRIMA(col, timeperiod)}


def WMA(col, timeperiod=30):
    return {"wma": ta.WMA(col, timeperiod)}
