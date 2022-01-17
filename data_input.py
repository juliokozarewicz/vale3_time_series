from pandas import to_datetime
from pandas import read_csv
from config import date_train_init, date_train_end
from config import date_predict_init

# data input {
# =============================================================================

# training data {
# -----------------------------------------------------------------------------
data_entry = read_csv("3_working/0_data_base.csv", sep=",", decimal=".")
data_entry["index_date"] = to_datetime(data_entry["index_date"])
data_entry = data_entry.sort_values("index_date")

# date filter
data_select = data_entry[ (data_entry.iloc[:,0] >= date_train_init) &
                          (data_entry.iloc[:,0] <= date_train_end) ]

# variable for executing the model estimation
data_select = data_select.set_index("index_date")

# variables
data_endog = data_select.iloc[ : , 0 : 1 ]
data_exogs = data_select.iloc[ : , 1 :   ]
# -----------------------------------------------------------------------------
#   }

# exogs for forecast {
# -----------------------------------------------------------------------------
data_exogs_fore = read_csv("3_working/0_forecast.csv", sep=",", decimal=".")
data_exogs_fore["index_date"] = to_datetime(data_exogs_fore["index_date"])
data_exogs_fore = data_exogs_fore.sort_values("index_date")

data_exogs_fore = data_exogs_fore.iloc[ : , 2 :   ]
# -----------------------------------------------------------------------------
#   }

# variables {
# -----------------------------------------------------------------------------
variable_ = list(data_endog.columns.values.tolist())[0]
variable = variable_.replace("_", ' ').upper()
# -----------------------------------------------------------------------------
#   }

# =============================================================================
# }
