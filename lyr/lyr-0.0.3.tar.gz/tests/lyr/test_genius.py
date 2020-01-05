from lyr import genius

def test_lyrics():
    query = 'katy perry roar'
    lyrics = genius.lyrics(query)
    assert lyrics is not None