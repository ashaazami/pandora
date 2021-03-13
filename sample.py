import distribution as dis
import pandas as pd
import numpy as np

if __name__ == "__main__":
    data = pd.DataFrame()
    data["Type"] = np.random.randint(0, 3, size=3000)
    data["Price"] = np.random.rand(3000)
    data.loc[data["Type"] == 0, "Price"] = np.random.rand(sum(data["Type"] == 0)) * 3 + 7
    data.loc[data["Type"] == 1, "Price"] = np.random.rand(sum(data["Type"] == 1)) * 7
    data.loc[data["Type"] == 2, "Price"] = np.random.rand(sum(data["Type"] == 2)) * 5 + 3
    data["Parity"] = np.random.randint(0, 2, size=3000).astype(str)

    plot = dis.plot_vs_discrete(data, "Type", "Price", "Parity", "Price per Type for each Parity", None)

    print(plot)
