import numpy as np
import random
# 1. Sukurti ir spausdinti masyvus
# 	1.1 Sukurkite 1D NumPy masyvą su reikšmėmis nuo 1 iki 10 ir jį atspausdinkite.
# 	1.2 Sukurkite 2D NumPy masyvą, kurio forma (3, 3) užpildyta reikšme 7, ir jį išspausdinkite.

# fromzerotohero = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# fromherototwo = np.array([[7, 7, 7], [7, 7, 7], [7, 7, 7]])
# print(fromherototwo)

# 2. Pagrindinės aritmetinės operacijos
# 	2.1 Sukurkite du 1D masyvus su reikšmėmis nuo 1 iki 5. Sudėkite, atimkite, padauginkite ir padalykite elementus iš 2.

# arrtask1 = np.array([1, 3, 4, 2, 5])
# arrtask2 = np.array([[2, 3, 4, 5, 1]])
# print(arrtask2 + 2)
# print(arrtask2 - 2)
# print(arrtask1 * 2)
# print(arrtask1 / 2)

# 3. Masyvo indeksavimas ir pjaustymas
# 	3.1 Sukurkite 1D masyvą su reikšmėmis nuo 10 iki 20. Išspausdinkite pirmuosius 5 elementus ir paskutinius 5 elementus.

# arr = np.arange(10, 21)
# print(arr[:5])
# print(arr[-5:])

# 4. Masyvo pertvarkymas
# 	4.1 Sukurkite 1D masyvą su 12 elementų ir pertvarkykite jį į 2D masyvą, kurio forma (3, 4).
# arr2 = np.random.randint(1, 100, 12)
# print(arr2)
# sorted = arr2.reshape(3, 4)
# print(sorted)

# 5. Masyvų generavimas naudojant integruotas funkcijas
# 	5.1 Naudodami linspace sukurkite 10 tolygiai išdėstytų reikšmių nuo 0 iki 1 masyvą.
# 	5.2 Sukurkite 1D masyvą su reikšmėmis nuo 1 iki 10. Apskaičiuokite ir išspausdinkite sumą, vidurkį ir standartinį nuokrypį.

# arr = np.linspace(0, 1, 10)
# print(arr)
# suma = np.sum(arr)
# vidurkis = np.mean(arr)
# standartinis_nuokrypis = np.std(arr)
# print(suma)
# print(vidurkis)
# print(standartinis_nuokrypis)
#
# 6. Operacijos su matricomis
# 	6.1 Sukurkite dvi 2D formos (3, 3) matricas. Atlikite matricų sudėties, atimties ir matricų daugybos veiksmus.
# 	6.2 Sukurkite 1D matricą su reikšmėmis [0, π/2, π, 3π/2, 2π]. Apskaičiuokite šių reikšmių sinusą ir kosinusą.

# arr = np.random.randint(1, 10, (3, 3))
# arr2 = np.random.randint(1, 10, (3, 3))
# print('Pirma matrica', arr)
# print('Antra matrica', arr2)
# print('Atimam',arr - arr2)
# print('Sudedam', arr + arr2)
# print('Dauginam',arr * arr2)

# pi = np.pi
#
# arr = np.array([0, pi/2, pi, 3*pi/2, 2*pi])
#
# sin_values = np.sin(arr)
# cos_values = np.cos(arr)
#
# print("Angles in radians:", arr)
# print("Sine values:", sin_values)
# print("Cosine values:", cos_values)



#7
arr = np.random.randint(0, 2, 100)
median = np.median(arr)
variance = np.var(arr)
#
# print(arr)
# print(median)
# print(variance)

#8
arr = np.random.randint(1, 10, (3, 3))
arr2 = np.random.randint(1, 10, (3, 3))
print(arr)
print(arr2)

# 9. Loginis indeksavimas
# 	9.1 Sukurkite 1D masyvą su reikšmėmis nuo 1 iki 10. Išskirkite visus lyginius skaičius naudodami loginį indeksavimą.
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# even_numbers = arr[arr % 2 == 0]
# print("Lyginiai skaičiai", even_numbers)

# 10. Masyvų rūšiavimas
# 	10.1 Sukurkite 1D masyvą su 10 atsitiktinių sveikųjų skaičių nuo 0 iki 50. Surūšiuokite masyvą didėjančia tvarka.
arr = np.random.randint(0, 50, 10)
didit = np.sort(arr)
print(didit)

# 11. Tiesinės algebros operacijos
# 	11.1 Sukurkite 2D formos (2, 2) masyvą A ir kitą 2D formos (2, 2) masyvą B. Apskaičiuokite A ir B sandaugą ir A matricos determinantą.
A = np.array([[2, 4], [3, 5]])
B = np.array([[4, 5], [1, 3]])

SUMA = np.sum(A)
SUMB = np.sum(B)
print(SUMA * SUMB)

determinantas_A = np.linalg.det(A)

print("Matricos A determinantas:", determinantas_A)

#12. Išplėstinis indeksavimas
	#12.1 Sukurkite 4x4 masyvą ir naudodami išplėstinį indeksavimą įstrižainės elementams nustatykite reikšmę 1.
arr = np.random.randint(0, 15, (4, 4))
arr[np.diag_indices(4)] = 1

# 13. Tikimybių skaičiavimas
# 	13.1 Naudodami "NumPy" imituokite dviejų šešiabriaunių kauliukų metimo procesą 1000 kartų. Apskaičiuokite tikimybę, kad metant bus gauta suma 7.
import numpy as np

num_rolls = 1000

dice1 = np.random.randint(1, 7, num_rolls)
dice2 = np.random.randint(1, 7, num_rolls)

sums = dice1 + dice2
count_sum_7 = np.count_nonzero(sums == 7)
probability_sum_7 = count_sum_7 / num_rolls

print(f"Probability of getting a sum of 7: {probability_sum_7:.4f}")


