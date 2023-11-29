from antlr4 import InputStream, CommonTokenStream
from antlr.ShellGrammarLexer import ShellGrammarLexer
from antlr.ShellGrammarParser import ShellGrammarParser
from converter import Converter
from expressions import Commmand, Call, Atom, Argument

command = "echo hello"
print(f"Input Command: {command}")

input_stream = InputStream(command)

lexer = ShellGrammarLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ShellGrammarParser(token_stream)

print("Parsing command...")
parse_tree = parser.command()
print("Parse Tree:")
print(parse_tree.toStringTree(recog=parser))

converter = Converter()
print("Converting parse tree...")
actual_output = converter.visit(parse_tree)

print("Converted Result:")
print(actual_output)

expected_output = Commmand(Call((Argument("echo")), Atom(Argument("hello"))))

print("Expected Result:")
print(expected_output)

if actual_output == expected_output:
    print("Success: The outputs match.")
else:
    print("Failure: The outputs do not match.")
