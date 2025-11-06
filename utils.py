from pandas import DataFrame as df
import pandas as pd
import statsmodels.api as smapi
import numpy as np

def loadDataFrame(fileName: str) -> df | None:
    try:
        dFrame = pd.read_csv(fileName)
    except:
        print("ERROR loading file {fileName} into dataframe")
        return None
    
    return dFrame

def fitModel(dFrame: df, depVar: str, indVars: list[str], oset:str | None = None):
    assert len(indVars) > 0
    
    y = dFrame[depVar]
    X = smapi.add_constant(dFrame[indVars])
    if oset:
        offset = np.log(dFrame[oset])
    else:
        offset = None

    model = smapi.GLM(y, X, smapi.families.Poisson(), offset)
    result = model.fit()

    return result