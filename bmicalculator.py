# This is BMI calculator
print("Jeśli chcesz obliczyć swoje BMI podaj ")
kg = float(input("swoją wagę w kilogramach: "))
metry = float(input("swój wzrost w metrach: "))

bmi = kg / metry ** 2
print(bmi)

if bmi < 18.5:
    print("Ważysz za mało.")
elif (bmi >= 18.5) and (bmi < 24.5):
    print("Twoja waga jest optymalna.")
elif (bmi >= 24.5) and (bmi < 30):
    print("Masz nadwagę.")
elif bmi <= 30:
    print("To już otyłość. ")
else:
    print("Coś poszło nie tak.")