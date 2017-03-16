import pytest
from palindromes import Palindromes
import server

@pytest.fixture()
def client():
    palindromes = Palindromes()
    palindromes.set_filename('tests/files/valid.json')
    palindromes.read_contents()
    palindromes.parse_palindromes()
    server.set_palindromes_list(palindromes.palindromes_list)
    server.set_palindromes_sum(palindromes.palindromes_sum)
    return server.app.test_client()

class TestServer:

    def test_palindromes(self, client):
        rv = client.get('/palindromes')
        assert b'racecar' in rv.data
        assert b'lol' in rv.data

    def test_palindromes_count(self, client):
        rv = client.get('/palindromes/count')
        assert b'2' in rv.data
