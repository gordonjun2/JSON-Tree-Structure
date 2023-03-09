# JSON-Tree-Structure
Take in Python dictionary or JSON and then recursively traverse it to extract all the keys. This can be useful if you want to understand the structure of a long dictionary or JSON. Coded with the help of ChatGPT (and whoever contributed to the training data of ChatGPT)...

## Expected Output
- Input:
```
{"name": "John Smith", "age": 30, "address": {"city": "New York", "state": "NY"}, "phone_numbers": [{"type": "home", "number": "555-1234"}, {"type": "work", "number": "555-5678"}]}
```
- Output:
```
name
age
address
    city
	  state
phone_numbers
	  [List]
		    type
		    number
	  ...

```

## Usage
- Run
```
python main.py -f <your .txt file that contains the dictionary or JSON>
```

## Useful Tips
- [How do I save terminal output to a file?](https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file)
