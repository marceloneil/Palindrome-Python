import os.path
import json

class Palindromes:
    'Class for importing/verifying/counting palindrome data'
    filename = None
    contents = None
    palindromes_list = []
    palindromes_sum = 0

    def set_filename(self, filename=None):
        'Get a valid filename from the user'
        if filename:
            if not os.path.isfile(filename):
                # If the file isn't in the current path, error
                print('Error: invalid filename')
            else:
                self.filename = filename
        else:
            filename = input('Please enter the name of the input file: ')
            while not os.path.isfile(filename):
                # If the file isn't in the current path, try again
                filename = input('Invalid filename, please try again: ')
            self.filename = filename

    def read_contents(self):
        'Reads contents of the specified file'
        try:
            # Read file and split into list of each line
            data = open(self.filename, 'r').read().split('\n')
            contents = []
            for i in range(len(data)):
                if data[i]: # Don't parse empty lines
                    try:
                        contents.append(json.loads(data[i]))
                    except json.decoder.JSONDecodeError:
                        pass # Skip lines that aren't JSON
                    except Exception as e:
                        print(e)
                        print('Error reading file, try again')
                        return
            self.contents = contents
        except UnicodeDecodeError:
            # File is not correctly encoded
            print('Invalid file encoding, try again.')
        except json.decoder.JSONDecodeError:
            # File not in JSON format
            print('Invalid JSON format, try again.')
        except:
            # Some other error
            print('Error reading file, try again.')

    def test_palindrome(self, string):
        'Test to see if a string is a palindrome'
        return string == string[::-1]

    def parse_palindromes(self):
        'Parse palindromes from contents'
        for data in self.contents:
            # Check if key 'key' is in the JSON
            if 'key' in data:
                # Check to see if value is a palindrome
                if self.test_palindrome(data['key']):
                    self.palindromes_list.append(data['key'])
                    self.palindromes_sum += 1


