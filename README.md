# AirBnB Clone

## Description
- This is a clone of the real AirBnb web application. It is a test of my learning so far, especially concepts like Object-Oriented Programming.
- There are components that I will create which will make this project successful. These will include:
  - `A console` - Here I will play around with the classes and how things will be stored and deleted and updated and so on.
  - The different classes - These are objects that will be used to create for xample the place, the type of house and so on.
  - `unittests` - These will ensure everything is working as it should.

## The Command Interpreter
- Also known as the console, will be like a shell which I use to create, update, delete instances of objects.

- Made a console using the class `cmd`.
  - Defined the `EOF` command which will help the user quit the console when it detects end of file
  - Defined the `quit` command which also hwlps the user to quit the console.
  - On pressing `Enter` + empty line, the console does not execute anything.

- Defined different commands:
  - `create` - Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`
    - If the class name is missing, print `** class name missing **` (ex: `$ create`)
      - If the class name doesn’t exist, print `** class doesn't exist **` (ex: `$ create MyModel`)

### Class BaseModel
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

### Class FileStorage
- After creating `BaseModel` which created instances with common attributes and methods, I realised I was unable to persist the instances.
- This class which is in the folder `models/engine` is used to store instances to a file by serializing the object to `JSON` and saving to a file with extension `.json`.
- The private attributes used in this class are:
  - `__file_path`: This is used to store the file path of the `.json' file.
  - `__objects`: This is a dictionary that stores the objects. An object is stored in the form, `<obj class name>.id`
- The public instance methods used in this class are:
  - `def all(self):` - This method returns the dictionary `__objects` which contains all the objects.
  - `def new(self, obj):` - This method sets the object `obj` in the dictionary `__objects`. Key is always `<obj class name>.id` and value is the dict of `obj`.
  - `def save(self):` - This method serializes the dictionary `__obj` and saves it into the `__file_path`.
  - `def reload(self):` - This method deserializes the dictionary `__obj` from `__file_path` if `__file_path` exists. Exceptions have been suppressed.

### ---------------------------------------------------------------------------------------------------------------------------------

- After creating the `FileStorage` class, the `__init__.py` file in the `models` directory was updated to create an instance of `FileStorage`.
  - Imported `file_storage.py` and created an instance `storage`
  - The instance `storage` calls the `reload()` method.

- Imported `storage` to `BaseModel` and used it in the `save()` method by calling the `save()` method of `FileStorage` on it.
- Updated the `__init__` method of `BaseModel` such that wen there are no `**kwargs` to create a model, `storage` calls the `new()` method from `FileStorage` and creates a model.