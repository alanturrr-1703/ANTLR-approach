from antlr4 import *
from GosuLexer import GosuLexer
from GosuParser import GosuParser

# Example Gosu code
gosu_code = """
//parser testing
/* parser testing */
uses gw.util.*

class SQLInjectionExample1 {

    // Function to simulate user login
    function userLogin(username: String, password: String): String 
	{
        // Vulnerable SQL query without parameterization
        var sqlQuery = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "';"

        // Execute the query (just simulating here)
        var result = executeSQLQuery(sqlQuery)

        // Return the result based on the query response
        if (result == "Success") {
            return "Login successful!"
        } else {
            return "Invalid credentials!"
        }
    }

    // Function to simulate SQL execution (unsafe)
    function executeSQLQuery(query: String): String 
	{
        print("Executing SQL Query: " + query)

        // Simulating that the query always succeeds
        // In reality, here would be code that runs the SQL against a database
        if (query.contains("admin' OR '1'='1")) {
            return "Success" // Simulated result from a successful login
        } else {
            return "Failure" // Simulated result from an invalid login
        }
    }
}
"""

# Parsing the input code
input_stream = InputStream(gosu_code)
lexer = GosuLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = GosuParser(token_stream)

# Use the correct starting rule
tree = parser.start()  # Replace 'start' with the correct rule if different

# Print the parsed tree
print(tree.toStringTree(recog=parser))
