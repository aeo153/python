import pandas as pd
import numpy as np

data = pd.read_csv("D:/dsyx_doc/surgery_nav/error_result.csv")
data.groupby("target_dist_to_origin").count()