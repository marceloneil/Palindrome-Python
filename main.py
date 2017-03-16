from palindromes import Palindromes
import server

palindromes = Palindromes()

# Retrieve file from user
while not (palindromes.filename and palindromes.contents):
    # While loop to ensure that correct file is entered
    palindromes.set_filename()
    palindromes.read_contents()
palindromes.parse_palindromes()

# Add the palindromes to the server and then start
server.set_palindromes_list(palindromes.palindromes_list)
server.set_palindromes_sum(palindromes.palindromes_sum)
server.app.run()
