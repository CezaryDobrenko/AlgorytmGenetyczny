<b>Pierwsze uruchomienie projektu:</b>

a) Z użyciem pip<br />
Jeśli pip nie jest zainstalowany:
https://pip.pypa.io/en/stable/installation/
pip install --upgrade pip<br />
pip install -r requirements.txt<br />
python3 main.py<br />

b) bez użycia pip<br />
Niezbędne biblioteki do prawidłowego funkcjonowania:<br />
matplotlib<br />
numpy<br />
imageio<br />



<b>Przykładowa animacja procesu ewolucyjnego:</b>

![Screenshot](example.gif)


<b>Podstawowe dane pomagające w zapoznaniu się z projektem:</b>

1. Struktura:<br />

Plik główny<br />
  main.py -> Przykład wykorzystania algorytmu (zawiera wszystkie zmienne i dane niezbędne do konfiguracji algorytmu)<br />

Serwisy (klasy nie wymagające instancji):<br />
  converter.py -> Służy do konwersji dec -> gray_code, gray_code -> dec<br />
  mutator.py -> Służy do zastosowania jednej bądź wielu mutacji na genotypie dziecka (zaimplementowane zostały różne rodzaje mutacji)<br />

Klasy:<br />
  probe.py -> Definicja poszczególnego osobnika<br />
  plotter.py -> Odpowiada za animację procesu ewolucyjnego<br />
  simulation.py -> Algorytm ewolucyjny<br />

2. Opis zmiennych zastosowanych w algorytmie:

bounds -> określa przestrzeń na której wyszukiwane jest minimum lokalne<br />
bit_size -> określa ilość bitów przypadającą na każdy chromosom<br />
population_size -> określa ilość osobników w populacji<br />
generations -> określa ile pokoleń ma trwać algorytm genetyczny<br />
tournament_size -> określa ile osobników jest wybierane do turnieju (turniej to wybieranie najlepszego osobnika z losowo wybranej puli turniejowej)<br />
settings -> Określa które mutacje mają zostać wykonane na osobniku potomnym.<br />

3. Opis mutatorów:<br />

https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_mutation.htm 

4. Opis funkcjonalności algorytmu ewolucyjnego:<br />

Wykonanie procesu ewolucyjnego dla początkowej puli osobników<br />
Wyświetlanie procesu w formie animacji<br />
Export danych procesu ewolucyjnego do formatu json<br />
Zapis aniamcji w formie pliku .gif<br />
Zapis poszczególnych klatek animacji<br />
