# Opis
Działający projekt hostowany jest na serwisie AWS i dostępny pod adresem http://13.53.108.199
Jest to prosty projekt bloga zbudowany w oparciu o Django. Użytkownicy mogą rejestrować się, logować, tworzyć, edytować i usuwać posty. Blog umożliwia również przeglądanie postów innych użytkowników.

## Instalacja
1. Klonowanie repozytorium
```bash
git clone https://github.com/djdudus/django_blog/tree/main/strona_druga
cd strona_druga
```
2. Ustawienie wirtualnego środowiska
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Instalacja wymaganych bibliotek
```bash
pip install -r requirements.txt
```
4. Konfiguracja bazy danych
Ustaw odpowiednie połączenie z bazą danych (domyślnie ustawiony jest silnik PostgreSQL) w pliku settings.py i następnie uruchom:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Uruchomienie serwera
```bash
python manage.py runserver
```
Otwórz przeglądarkę i przejdź do http://localhost:8000 aby zobaczyć działający blog.

## Funkcje
- Rejestracja i logowanie użytkowników
- Tworzenie, edytowanie i usuwanie postów
- Przeglądanie postów innych użytkowników
