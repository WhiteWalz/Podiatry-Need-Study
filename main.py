from tkinter.filedialog import askopenfilename as getFileName
import utils
from pandas import DataFrame

DEPENDENT_VARIABLE: str = ""
INDEPENDENT_VARIABLES: list[str] = list()

def run():
    fileName = getFileName(defaultextension="csv")
    df = None
    try:
        df = utils.loadDataFrameFromCSV(fileName)
    except Exception as e:
        print("Error loading file \"{{fileName}}\" into dataframe.")
        print(e)

    try:
        assert df is DataFrame
        overDispersed = utils.isOverdispersed(df, depVar=DEPENDENT_VARIABLE)
        print(f'Dataset is overdispersed? {{overDispersed}}')
        results = utils.fitModel(df, depVar=DEPENDENT_VARIABLE, indVars=INDEPENDENT_VARIABLES)
    except:
        print("Error generating model from dataset and variable assignments.")

    utils.showModelSummary(results)
    
    # Plot model/dataset below.


if __name__ == "__main__":
    run()