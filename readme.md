Podstawowe dane pomagające w zapoznaniu się z projektem:

1. Struktura:

Plik główny
	1. main.py -> przykład wykorzystania algorytmu (zawiera wszystkie zmienne i dane niezbędne do konfiguracji algorytmu)

Serwisy (klasy nie wymagające instancji):
	1. converter.py -> Służy do konwersji dec -> gray_code, gray_code -> dec
	2. mutator.py -> Służy do zastosowania jednej bądź wielu mutacji na genotypie dziecka (zaimplementowane zostały różne rodzaje mutacji)
	
Klasy:
	1. probe.py -> Definicja poszczególnego osobnika
	2. plotter.py -> Odpowiada za animację procesu ewolucyjnego
	3. simulation.py -> Algorytm ewolucyjny
	
2. Opis zmiennych zastosowanych w algorytmie:
	1.bounds -> określa przestrzeń na której wyszukiwane jest minimum lokalne.
	2.bit_size -> określa ilość bitów przypadającą na każdy chromosom.
	3.population_size -> określa ilość osobników w populacji
	4.generations -> określa ile pokoleń ma trwać algorytm genetyczny
	5.tournament_size = -> określa ile osobników jest wybierane do turnieju (turniej to wybieranie najlepszego osobnika z losowo wybranej puli turniejowej).
	6.settings = {
	"single_point_mutation": True,
	"swap_mutation": False,
	"scramble_mutation": False,
	"reverse_mutation": False, 
	"full_random_mutation": False,
	} -> Określa które mutacje mają zostać wykonane na osobniku potomnym.
	
3. Opis mutatorów:
	https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_mutation.htm 

4. Opis funkcjonalności algorytmu ewolucyjnego:
    1. Wykonanie procesu ewolucyjnego dla początkowej puli osobników
    2. Wyświetlanie procesu w formie animacji
    3. Export danych procesu ewolucyjnego do formatu json
