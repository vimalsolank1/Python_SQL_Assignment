'''
Task 3 - FastAPI - Write a python code to create the following API using fastAPI
a) To accept 2 numbers and return their sum. Ensure the API is able to give proper error value when string is
entered in place of numbers
b) To accept lower case string and return the string in all capital letters'''


from fastapi import FastAPI

app = FastAPI()

# --> a) To accept 2 numbers and return their sum. 
#   API to add two numbers
@app.get("/add")
def add_numbers(a: float, b: float):
    return {"sum": a + b}
    
# -->  b) To accept lower case string and return the string in all capital letters
@app.get("/uppercase")
def convert_to_upper(text: str):
    return {"uppercase_text": text.upper()}
    
