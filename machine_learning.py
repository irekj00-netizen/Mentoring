import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# zad. 1
df_1 = pd.read_csv(r'C:\Users\irekj\Documents\Python\Mentoring\points_a.csv', sep = '_')
df_2 = pd.read_csv(r'C:\Users\irekj\Documents\Python\Mentoring\points_b.csv', sep = ';')

# zad. 2
df_combined = pd.concat([df_1, df_2], ignore_index=True)
df_combined['etykieta'] = pd.to_numeric(df_combined['etykieta'], errors='coerce')
df_clean = df_combined.dropna(subset=['etykieta'])

# X - Wektor Klasyfikujący (Cechy)
X = df_clean[['x', 'y']]
# y - Wektor Docelowy (Kolumna Klasyfikująca/Etykieta)
y = df_clean['etykieta'].astype(int)

# zad. 3
dane_trenujace, dane_testowe, etykiety_trenujace, etykiety_testowe = train_test_split(
    X,            # Wektor klasyfikujący (cechy)
    y,            # Wektor docelowy (etykiety)
    test_size = 0.2,  # 20% danych do testowania
    random_state = 42, # Ziarno losowości dla powtarzalności
    stratify = y      # Bardzo ważne! Zapewnia równy udział klas w obu zbiorach
)

# zad. 4a
model_lr = LogisticRegression(random_state=42)
model_lr.fit(dane_trenujace, etykiety_trenujace)

# zad. 4b
model_svc = LinearSVC(random_state=42, max_iter=10000)
model_svc.fit(dane_trenujace, etykiety_trenujace)

# zad. 5 i 6
# --- 1. Regresja Logistyczna (LogisticRegression) ---
# Generowanie predykcji na danych testowych
etykiety_predykowane_lr = model_lr.predict(dane_testowe)

# Obliczenie dokładności (Accuracy)
dokladnosc_lr = accuracy_score(etykiety_testowe, etykiety_predykowane_lr)

print("Wyniki: Regresja Logistyczna (LogisticRegression)")
print("--------------------------------------------------")
print(f"Dokładność (Accuracy): {dokladnosc_lr:.4f}")

# Wyświetlenie pełnego raportu klasyfikacji
print("\nRaport Klasyfikacji (Classification Report):")
print(classification_report(etykiety_testowe, etykiety_predykowane_lr, zero_division=0))

# --- 2. Liniowa Maszyna Wektorów Nośnych (LinearSVC) ---
# Generowanie predykcji na danych testowych
etykiety_predykowane_svc = model_svc.predict(dane_testowe)

# Obliczenie dokładności (Accuracy)
dokladnosc_svc = accuracy_score(etykiety_testowe, etykiety_predykowane_svc)

print("\nWyniki: Linear SVC (Support Vector Classification)")
print("--------------------------------------------------")
print(f"Dokładność (Accuracy): {dokladnosc_svc:.4f}")

# Wyświetlenie pełnego raportu klasyfikacji
print("\nRaport Klasyfikacji (Classification Report):")
print(classification_report(etykiety_testowe, etykiety_predykowane_svc, zero_division=0))