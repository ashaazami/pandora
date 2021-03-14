from pandora import distribution as dis
import pandas as pd
import numpy as np

if __name__ == "__main__":
    data = pd.DataFrame()
    bucket_size = 10
    data["Type"] = np.random.randint(0, 3, size=3 * bucket_size).astype(str)
    data["Price"] = np.random.rand(3 * bucket_size)
    data.loc[data["Type"] == "0", "Price"] = np.random.rand(sum(data["Type"] == "0")) * 3 + 7
    data.loc[data["Type"] == "1", "Price"] = np.random.rand(sum(data["Type"] == "1")) * 7
    data.loc[data["Type"] == "2", "Price"] = np.random.rand(sum(data["Type"] == "2")) * 5 + 3
    data["Temperature"] = np.random.rand(3 * bucket_size)
    data["Parity"] = np.random.randint(0, 2, size=3 * bucket_size).astype(str)

    plot = dis.plot_vs_discrete(data, "Type", "Price", "Parity", "Price per Type for each Parity")
    print(plot)

    plot = dis.plot_vs_continuous(data, "Temperature", [0, .5, 1], "Price", "Parity",
                                  "Price per Temperature for each Parity")
    print(plot)

    plot = dis.plot_continuous_distribution(data, "Temperature", "Parity", "Temperature distribution for each Parity")
    print(plot)
