# Warunki minimalne projektu CSV

1. Znajdź plik csv (minimum 100 linii), pobierz go i umieść tak, żeby był widoczny dla skryptu jupytera
2. Stwórz obiekt DataFrame (używając funkcji read_csv), wykonaj metodę tail lub head
3. Dostosuj obiekt DataFrame do swoich potrzeb (używając parametrów read_csv takich jak usecols i index)
4. Wykonaj jakieś operacje na tych danych używając dowolnych metod
5. Wyświetl wykres z danymi w obiekcie DataFrame używając metody plot i dostosowując sam wykres metodami pyplot

# Warunki minimalne projektu JSON

1. Stworzyć obiekt json (co najmniej 10 pól)
2. W skrypcie Pythona stworzyć słownik na podstawie tego obiektu json
3. Na podstawie słownika stworzyć obiekt xml (bezpośrednio lub klasą wrappera)
4. Zapisać obiekt xml do pliku

# Warunki minimalne projektu XML/XML-Schema

1. Napisać pewien plik w formacie XML
  - tag główny -> tag potomny -> tag potomny
  - łącznie RÓŻNYCH tagów powinno być minimum 5
  - co najmniej trzy atrybuty na co najmniej dwóch tagach
  - plik musi istotnie różnić się od przykładowego `data.xml`
  - plik musi opisywać sensownie jakiś wycinek rzeczywistości
2. Napisać dla tego pliku definicję w XML-Schema
  - definicja musi być wystarczająco ograniczająca, co oznacza, że nie będzie
    się dało dodać nowego tagu
  - dopuszczalne są definicje, które umożliwiają zwielokrotnienie istniejących
    tagów

# Warunki minimalne projektu Protege

1. Stworzyć co najmniej 10 klas uporządkowanych w hierarchię, z czego co najmniej 3 muszą być rozłączne
2. Stworzyć co najmniej 10 własności obiektowych i co najmniej 2 własności danych; zdefiniować tym własnością domeny i zbiory wartości
3. Stworzyć co najmniej 15 instancji rozłożonych między co najmniej 5 spośród 10 klas
4. Uruchomić reasoner: ontologia ma być spójna i ma się coś wyliczać
5. Wytworzona struktura powinna opisywać jakiś wycinek rzeczywistości
