import pandas as pd

# plik z przecinkami:
file_path = r"C:\Users\irekj\Documents\Python\Mentoring\klienci.csv"
# plik ze średnikami:
file_path2 = r"C:\Users\irekj\Documents\Python\Mentoring\klienci2.csv"

def pt_1(fp):
    klienci = pd.read_csv(fp)
    return klienci

def pt_2(fp):
    klienci = pd.read_csv(fp, index_col = 0)
    return klienci

def pt_3(klienci):
    # info() drukuje informacje o DataFrame
    klienci.info()
    # head() bez podanej wartości zwraca domyśnie 5 pierwszych wierszy DataFrame'a
    # describe() zwraca liczbę niepustych wierszy, średnią, odchylenie std, minimum, percentyle i maksimum
    return klienci.head(), klienci.head(3), klienci.describe()

def pt_4(fp):
    # typy mozna zadeklarować za pomocą parametru dtype
    klienci = pd.read_csv(fp, dtype = {"name":"str", "age":"int", "city":"str","total_spend":"float",
                                       "last_purchase":"str"}, index_col=0)
    return klienci

def pt_5(fp):
    klienci = pd.read_csv(fp, sep = ";", index_col = 0)
    return klienci

def pt_6(fp):
    klienci = pd.read_csv(fp, dtype={"name": "str", "age": "int", "city": "str", "total_spend": "float"},
                                     parse_dates = ["last_purchase"], dayfirst=True, index_col=0)
    return klienci

def pt_7(fp):
    klienci = pd.read_csv(fp, dtype={"name": "str", "age": "int", "city": "str", "total_spend": "float"},
                                     parse_dates = ["last_purchase"], dayfirst=True, index_col=0)
    return klienci.head(3), klienci.tail(2)

def pt_8(fp):
    klienci = pd.read_csv(fp, index_col=0)
    return klienci["age"].mean()

def pt_9(fp):
    klienci = pd.read_csv(fp, index_col=0)
    return klienci["total_spend"].min(), klienci["total_spend"].max()

def pt_10(fp):
    klienci = pd.read_csv(fp, index_col=0)
    return klienci[["name", "city"]]

def pt_11(fp):
    klienci = pd.read_csv(fp, index_col=0)
    return klienci.sort_values("total_spend")

def pt_12(fp):
    klienci = pd.read_csv(fp, index_col=0)
    return klienci[klienci["age"] > 30]

def pt_13(fp):
    klienci = pd.read_csv(fp, index_col=0)
    return klienci[klienci["city"].isin(["Gdansk", "Warszawa"])]

def pt_14(fp):
    klienci = pd.read_csv(fp, index_col=0)
    return klienci[klienci["total_spend"] > 1000]

def pt_15(fp):
    klienci = pd.read_csv(fp, index_col=0)
    klienci["spend_category"] = pd.cut(klienci["total_spend"],
                                       bins = [0, 1000, 2000, float("inf")],
                                       labels=["mało", "średnio", "dużo"])
    return klienci

def pt_16(fp):
    klienci = pd.read_csv(fp, index_col=0)
    klienci["spend_category"] = pd.cut(klienci["total_spend"],
                                       bins = [0, 1000, 2000, float("inf")],
                                       labels=["mało", "średnio", "dużo"])
    return klienci["spend_category"].value_counts()

def pt_17(fp):
    klienci = pd.read_csv(fp, index_col=0)
    klienci["city"] = klienci["city"].str.lower()
    return klienci

def pt_18(fp):
    klienci = pd.read_csv(fp, index_col=0)
    klienci["last_purchase"] = pd.to_datetime(klienci["last_purchase"], dayfirst=True)
    klienci["days_since_last_purchase"] = (pd.Timestamp("25/11/2025") - klienci["last_purchase"]).dt.days
    return klienci

def pt_19(fp):
    klienci = pd.read_csv(fp, index_col=0)
    klienci["last_purchase"] = pd.to_datetime(klienci["last_purchase"], dayfirst=True)
    ost_zakup = klienci["last_purchase"].idxmax()
    return klienci.loc[ost_zakup]

def pt_20(fp):
    klienci = pd.read_csv(fp, index_col=0)
    return klienci.groupby("city")["total_spend"].sum()

def pt_21(fp):
    klienci = pd.read_csv(fp, index_col=0)
    klienci[['first_name', 'last_name']] = klienci['name'].str.split(' ', n=1, expand=True)
    return klienci

def pt_22a(fp):
    klienci = pd.read_csv(fp, index_col=0)
    klienci.loc[2, "city"] = None
    klienci.loc[4, "total_spend"] = None
    klienci.loc[1, "age"] = None
    return klienci

def pt_22(klienci):
    return klienci.columns[klienci.isna().any()].tolist()

def pt_23(klienci):
    return klienci.isna().sum()

def pt_24(klienci):
    return klienci.isna().sum().sum() / klienci.size * 100

def pt_25(klienci):
    return klienci[klienci.isna().any(axis=1)]

def pt_26(klienci):
    return klienci.dropna()

def pt_27(klienci):
    klienci['age'] = klienci['age'].fillna(klienci['age'].mean())
    return klienci

def pt_28(klienci):
    klienci['city'] = klienci['city'].fillna('nieznane')
    return klienci

def pt_29(klienci):
    klienci['is_missing_city'] = ~klienci['city'].isna()
    return klienci


# print(pt_1(file_path))
# print(pt_2(file_path))
# print(pt_3(pt_2(file_path))[2])
# print(pt_4(file_path))
# print(pt_5(file_path2))
# print(pt_7(file_path)[1])
# print(pt_8(file_path))
# print(pt_9(file_path))
# print(pt_10(file_path))
# print(pt_11(file_path))
# print(pt_12(file_path))
# print(pt_13(file_path))
# print(pt_14(file_path))
# print(pt_15(file_path))
# print(pt_16(file_path))
# print(pt_17(file_path))
# print(pt_18(file_path))
# print(pt_19(file_path))
# print(pt_20(file_path))
# print(pt_21(file_path))
# print(pt_22a(file_path))
# print(pt_22(pt_22a(file_path)))
# print(pt_23(pt_22a(file_path)))
# print("Procent brakujących danych:",pt_24(pt_22a(file_path)))
# print(pt_25(pt_22a(file_path)))
# print(pt_26(pt_22a(file_path)))
# print(pt_27(pt_22a(file_path)))
# print(pt_28(pt_22a(file_path)))
print(pt_29(pt_22a(file_path)))