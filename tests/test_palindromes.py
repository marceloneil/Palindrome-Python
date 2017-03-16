import pytest
from palindromes import Palindromes

@pytest.fixture()
def palindromes():
    return Palindromes()

class TestPalindromes:
    
    def test_set_filename(self, palindromes):
        'Test case for Palindromes.set_filename'
        palindromes.set_filename('tests/files/valid.json')
        assert palindromes.filename == 'tests/files/valid.json'

    def test_set_filename_invalid(self, palindromes, capsys):
        'Failing test case for Palindromes.set_filename'
        palindromes.set_filename('invalid')
        out, err = capsys.readouterr()
        assert out == 'Error: invalid filename\n'
        assert not err
        assert not palindromes.filename

    def test_read_contents(self, palindromes):
        'Test case for Palindromes.read_contents'
        palindromes.set_filename('tests/files/valid.json')
        palindromes.read_contents()
        assert palindromes.contents

    def test_read_contents_unicode_error(self, palindromes, capsys):
        'Failing test case for Palindromes.read_contents'
        palindromes.set_filename('tests/files/binary.json')
        palindromes.read_contents()
        out, err = capsys.readouterr()
        assert out == 'Invalid file encoding, try again.\n'
        assert not err
        assert not palindromes.contents

    def test_read_contents_other_error(self, palindromes, capsys):
        'Failing test case for Palindromes.read_contents'
        palindromes.filename = 'invalid' # Writing directly to filename
        palindromes.read_contents()
        out, err = capsys.readouterr()
        assert out == 'Error reading file, try again.\n'
        assert not err
        assert not palindromes.contents

    def test_test_palindrome(self, palindromes):
        'Test case for Palindromes.test_palindrome'
        assert palindromes.test_palindrome('racecar')
        assert not palindromes.test_palindrome('not a palindrome')

    def test_parse_palindromes(self, palindromes):
        'Test case for Palindromes.parse_palindromes'
        palindromes.set_filename('tests/files/valid.json')
        palindromes.read_contents()
        palindromes.parse_palindromes()
        assert palindromes.palindromes_list == ['racecar', 'lol']
        assert palindromes.palindromes_sum == 2


