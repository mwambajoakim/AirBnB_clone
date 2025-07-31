# AirBnB Clone

## Description
- This is a clone of the real AirBnb web application. It is a test of my learning so far, especially concepts like Object-Oriented Programming.
- There are components that I will create which will make this project successful. These will include:
  - `A console` - Here I will play around with the classes and how things will be stored and deleted and updated and so on.
  - The different classes - These are objects that will be used to create for xample the place, the type of house and so on.
  - `unittests` - These will ensure everything is working as it should.

## The Command Interpreter
- Also known as the console, will be like a shell which I use to create, update, delete instances of objects.

### BaseModel
- This class defines all the common attributes/methods shared by other classes. It is found in the folder/package, `models`.
- The attributes defined include:
  - `id` - This is an id of an instance created using BaseModel. It is automatically genereted by use of `UUID4()'. Once it has been generated, it is stored as a string.
  - `created_at` - This is a `datetime` attribute that shows when the instance was created.
  - `updated_at` - This is also a `datetime` attribute which shows when the instance was updated.
- The public instance methods defined include:
  - `def save (self):` - This method updates the `updated_at` attribute with the current datetime.
  - `def to_dict(self):` - Returns a dictionary of the attributes of the instance.
    - Here, the class name is a key and its value is the name of the object.
    - Both `created _at` and `updated_at` are formatted into strings using ISO format with the format, `%Y-%m-%dT%H:%M:%S.%f`
    #### `def __init__(self, *args, **kwargs):`
    - In `BaseModel`'s init method, it accepts both non-key-word argumets and key-worded arguments. This is used for creating an instance from a dict using the **kwargs parameter. Every key and value is used to make an instance except the `"__class__.name"` key.
    - If `**kwargs` do not exist, the attributes are initialized through te defined attributes.