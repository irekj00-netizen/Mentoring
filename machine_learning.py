import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report

# zad. 1
df_1 = pd.read_csv(r'C:\Repozytoria\Mentoring\points_a.csv', sep = '_')
df_2 = pd.read_csv(r'C:\Repozytoria\Mentoring\points_b.csv', sep = ';')

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

# zad. 7
# Współczynniki z modelu Regresji Logistycznej
w1_lr, w2_lr = model_lr.coef_[0]
b_lr = model_lr.intercept_[0]

print(f"Współczynnik w1 RL (dla x): {w1_lr:.4f}")
print(f"Współczynnik w2 RL (dla y): {w2_lr:.4f}")
print(f"Wyraz wolny b RL: {b_lr:.4f}\n")

# Wartości x (od 0 do 100)
x_linia = np.linspace(0, 100, 100)

# Obliczanie y dla RL
y_linia_lr = (-b_lr - w1_lr * x_linia) / w2_lr

# Współczynniki w modelu SVC
w1_svc, w2_svc = model_svc.coef_[0]
b_svc = model_svc.intercept_[0]

# Obliczanie y dla SVC
y_linia_svc = (-b_svc - w1_svc * x_linia) / w2_svc

print(f"Współczynnik w1 SVC (dla x): {w1_svc:.4f}")
print(f"Współczynnik w2 SVC (dla y): {w2_svc:.4f}")
print(f"Wyraz wolny b SVC: {b_svc:.4f}")

# zad. 8
plt.figure(figsize=(10, 7))

# 1. Wykres punktowy
scatter = plt.scatter(
    X['x'],
    X['y'],
    c=y,
    cmap='coolwarm',
    s=50,
    alpha=0.8
)

# Linia decyzyjna Regresji Logistycznej
plt.plot(
    x_linia,
    y_linia_lr,
    color='blue',
    linestyle='-',
    linewidth=2,
    label='Regresja Logistyczna (LR)'
)

# Linia decyzyjna Linear SVC
plt.plot(
    x_linia,
    y_linia_svc,
    color='green',
    linestyle='--',
    linewidth=2,
    label='Linear SVC'
)

# 4. Ustawienia wykresu
plt.title('Punkty Danych z Liniami Decyzyjnymi LR i Linear SVC')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(X['x'].min() - 5, X['x'].max() + 5)
plt.ylim(X['y'].min() - 5, X['y'].max() + 5)
plt.legend(title='Model / Klasa')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# zad. 9
# Punkty klasy 0 - lewy dół
np.random.seed(42) # Dla powtarzalności
X1_x = np.random.uniform(10, 30, 50)
X1_y = np.random.uniform(10, 30, 50)
y1 = np.zeros(50)

# Punkty klasy 1 - prawy góra
X2_x = np.random.uniform(60, 80, 50)
X2_y = np.random.uniform(60, 80, 50)
y2 = np.ones(50)

# Łączenie w końcowe DataFrames
X_new = pd.DataFrame({
    'x': np.concatenate([X1_x, X2_x]),
    'y': np.concatenate([X1_y, X2_y])
})
y_new = pd.Series(np.concatenate([y1, y2])).astype(int)

# Trening
model_new = LogisticRegression()
model_new.fit(X_new, y_new)

# Współczynniki i wyraz wolny z wytrenowanego modelu
w1, w2 = model_new.coef_[0]
b = model_new.intercept_[0]

# Generowanie wartości X
x_linia_new = np.linspace(0, 100, 100)

# Obliczanie Y
y_linia_new = (-b - w1 * x_linia_new) / w2

# Rysujemy wykres
plt.figure(figsize=(9, 7))

# Wykres punktowy
scatter = plt.scatter(
    X_new['x'],
    X_new['y'],
    c=y_new,
    cmap='viridis',  # Inna mapa kolorów dla kontrastu
    s=70,
    alpha=0.8
)

# Linia decyzyjna
plt.plot(
    x_linia_new,
    y_linia_new,
    color='red',
    linestyle='-',
    linewidth=2,
    label='Granica Decyzyjna (Regresja Logistyczna)'
)

plt.title('Własny Zbiór Liniowo Separowalny i Granica Decyzyjna')
plt.xlabel('Współrzędna X')
plt.ylabel('Współrzędna Y')
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.legend(title='Klasa / Linia')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()