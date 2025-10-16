from app.web import apka #importuje naszą aplikację apka z pliku web.py

def test_strona_glowna():
    klient = apka.test_client() #tworzymy testowego klienta Flaska
    odpowiedz = klient.get('/') #wysyłamy zapytanie GET na "/"
    assert odpowiedz.status_code == 200
    assert b"Hello" in odpowiedz.data