# JSON-Tree-Structure
Take in Python dictionary or JSON and then recursively traverse it to extract all the keys. This can be useful if you want to understand the structure of a long dictionary or JSON. Coded with the help of ChatGPT (and whoever contributed to the training data of ChatGPT)...

## Expected Output
- Input:
```
{
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
  },
  "phone_numbers": [
    {
      "type": "home",
      "number": "555-1234"
    },
    {
      "type": "work",
      "number": "555-5678"
    }
  ],
  "favorite_foods": [
    {
      "name": "Pizza",
      "toppings": ["pepperoni", "mushrooms", "olives"]
    },
    {
      "name": "Tacos",
      "toppings": ["beef", "lettuce", "cheese", "sour cream"]
    }
  ]
}
```
- Output:
```
name
age
address
        street
        city
        state
        zip
phone_numbers
        [List]
                type
                number
        ...
favorite_foods
        [List]
                name
                toppings
        ...

```

## Usage
- Run
```
python main.py -f <your .txt file that contains the dictionary or JSON>
```

## Useful Tips
- [How do I save terminal output to a file?](https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file)
