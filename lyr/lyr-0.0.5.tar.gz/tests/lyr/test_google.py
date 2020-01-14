from lyr import google

def test_lyrics():
    query = 'ellie goulding your song'
    lyrics = google.lyrics(query)
    assert lyrics is not None