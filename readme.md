Dokumentacja techniczna: Interfejs użytkownika

1. Wprowadzenie

Interfejs użytkownika systemu służy do zarządzania procesem monitorowania dostępności stron internetowych, w tym serwisów w sieci TOR oraz w otwartej sieci (clearnet). 
Użytkownik ma możliwość wprowadzania adresów URL,  sprawdzenia ich statusu oraz czasu, kiedy strona ostatni raz została sprawdzona.

Panel klienta
- możliwość rejestracji
- możliwość zalogowania

Panel zarządznia adresami URL:
- możliwość dodania nowych adresów url
- możliwośc usunięcia dodanych wcześniej adresow url
- wyświetlanie aktualnego statusu strony
- wyświetlanie czasu, kiedy strona została sprawdzona

Interfejs:
[x] strona główna
[x] sekcja zarządzania adresami URL
[] panel konfiguracji
[] sekcja powiadomień
[] sekcja raportów

Zastosowane technologie:
Frontend:
- TBD
Backend
- Python + Django

Przykład ekranów interfejsu:
- TBD


Odpalanie:
1. pip install -r requirements.txt
2. (w folderze gdzie jest manage.py) python manage.py runserver

Testy:
1. (w folderze gdzie jest manage.py) python mange.py test