# AirBnB Clone

## Description
- This is a clone of the real AirBnb web application. It is a test of my learning so far, especially concepts like Object-Oriented Programming.
- There are components that I will create which will make this project successful. These will include:
  - `A console` - Here I will play around with the classes and how things will be stored and deleted and updated and so on.
  - The different classes - These are objects that will be used to create for xample the place, the type of house and so on.
  - `unittests` - These will ensure everything is working as it should.

## The Console
- This will be like a shell which I use to create, update, delete instances of objects.

- Made a console using the class `cmd`.
  - Defined the `EOF` command which will help the user quit the console when it detects end of file
  - Defined the `quit` command which also hwlps the user to quit the console.
  - On pressing `Enter` + empty line, the console does not execute anything.

- Defined different commands:
  - `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`
      - If the class name is missing, prints `** class name missing **` (ex: `$ create`)
      - If the class name doesn’t exist, prints `** class doesn't exist **` (ex: `$ create MyModel`)
  - `show`: Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234`.
      - If the class name is missing, prints `** class name missing **` (ex: `$ show`)
      - If the class name doesn’t exist, prints `** class doesn't exist **` (ex: `$ show MyModel`)
      - If the `id` is missing, prints `** instance id missing **` (ex: `$ show BaseModel`)
      - If the instance of the class name doesn’t exist for the `id`, prints `** no instance found **` (ex: `$ show BaseModel 121212`)
  - `destroy`: Deletes an instance based on the class name and 	id` (saves the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`.
      - If the class name is missing, prints `** class name missing **` (ex: `$ destroy`)
      - If the class name doesn’t exist, prints ** class doesn't exist ** (ex: `$ destroy MyModel`)
      - If the `id` is missing, prints `** instance id missing **` (ex: `$ destroy BaseModel`)
      - If the instance of the class name doesn’t exist for the `id`, prints `** no instance found **` (ex: `$ destroy BaseModel 121212`)
  - `all`: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` or `$ all`.
      - If the class name doesn’t exist, prints `** class doesn't exist **` (ex: `$ all MyModel`)
  - `update`: Updates an instance based on the class name and `id` by adding or updating attribute (saves the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
  - Usage: `update <class name> <id> <attribute name> "<attribute value>"`
  - Only one attribute can be updated at the time
  - Assuming the attribute name is valid (exists for this model)
  - The attribute value is cast to the attribute type
  - If the class name is missing, prints `** class name missing **` (ex: `$ update`)
  - If the class name doesn’t exist, prints `** class doesn't exist **` (ex: `$ update MyModel`)
  - If the `id` is missing, prints `** instance id missing **` (ex: `$ update BaseModel`)
  - If the instance of the class name doesn’t exist for the `id`, prints `** no instance found **` (ex: `$ update BaseModel 121212`)
  - If the attribute name is missing, prints `** attribute name missing **` (ex: `$ update BaseModel existing-id`)
  - If the value for the attribute name doesn’t exist, prints `** value missing **` (ex: `$ update BaseModel existing-id first_name`)
  
### models/__init__.py
- In this file all the classes that will be used in the different files for example the console and FileStorage classes to access the classes BaseModel and its children are defined in a dictionary.
- The instance storage is also in here.

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

### Class User
- This class creates a user and it inherits from BaseModel.
- Its public class attributes are:
  - `email`: An empty string to store the email.
  - `password`: An empty string to store the password.
  - `first_name`: An empty string to store the first name.
  - `last_name`: An empty string to store the last name.

### Class State
- This is the state location.
- The public class attribute is:
  - `name`: An empty string to store the name of the state.

### Class City
- This is the city location.
- The public class attributes are:
  - `state_id`: An empty string which will be `State.id`.
  - `name`: An empty string to store the name of the city.

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

### --------------------------------------------------------------------------------------------------------------------------------

- After creating the `FileStorage` class, the `__init__.py` file in the `models` directory was updated to create an instance of `FileStorage`.
  - Imported `file_storage.py` and created an instance `storage`
  - The instance `storage` calls the `reload()` method.

- Imported `storage` to `BaseModel` and used it in the `save()` method by calling the `save()` method of `FileStorage` on it.
- Updated the `__init__` method of `BaseModel` such that wen there are no `**kwargs` to create a model, `storage` calls the `new()` method from `FileStorage` and creates a model.