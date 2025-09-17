# Importa as classes do seu ficheiro de solução
# Assumindo que o seu código está em app/main.py
from app.main import Car, CarWashStation

print("--- INICIANDO TESTE LOCAL ---")

# Criando as instâncias exatamente como no exemplo do PDF
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')
ws = CarWashStation(6, 8, 3.9, 11)

# --- Testando o método serve_cars ---
print("\n1. Testando serve_cars...")
income = ws.serve_cars([bmw, audi, mercedes])
print(f"   Rendimento obtido: {income} (Esperado: 41.7)")
print(f"   Limpeza BMW: {bmw.clean_mark} (Esperado: 8)")
print(f"   Limpeza Audi: {audi.clean_mark} (Esperado: 9)")
print(f"   Limpeza Mercedes: {mercedes.clean_mark} (Esperado: 8)")

# --- Testando o método calculate_washing_price ---
print("\n2. Testando calculate_washing_price...")
ford = Car(2, 1, 'Ford')
wash_cost = ws.calculate_washing_price(ford)
print(f"   Custo de lavagem Ford: {wash_cost} (Esperado: 9.1)")
print(f"   Limpeza Ford (não deve mudar): {ford.clean_mark} (Esperado: 1)")

# --- Testando o método rate_service ---
print("\n3. Testando rate_service...")
ws.rate_service(5)
print(f"   Nova contagem de avaliações: {ws.count_of_ratings} (Esperado: 12)")
print(f"   Nova avaliação média: {ws.average_rating} (Esperado: 4.0)")

print("\n--- TESTE LOCAL CONCLUÍDO ---")
