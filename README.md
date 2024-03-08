![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)

# Important information

Read the following guidelines before doing the exercises.

## How do you begin?

1. [*Fork*](https://guides.github.com/activities/forking/) the repository containing exercises.
2. Clone the repository onto your computer using the command: `git clone repository_address`.
   You will find the address of the repository by pressing "Clone or download" button on its webpage.
3. Complete the exercises and commit changes to your repository using the commands below.
   `git add filename` will add a single file which you have changed.
   If you want to add all the changed files at once, use `git add .`.
   Remember that the fullstop (dot) at the end of this command is important!
   Next, commit changes using `git commit -m "description_of_changes"`.
4. Push changes to your repository on GitHub by typing: `git push origin main`.
5. Create a [*pull request*](https://help.github.com/articles/creating-a-pull-request) to the original repository when you have finished all the exercises.

### Do the exercises in appropriate files.

**The repository with the exercises will be removed 2 weeks after the end of the course. This will result in the removal of all forks made from this repository.**


## Task 1 (2 points)

Write a function named `check_character` that:
* takes a string and a single character,
* returns the number of occurrences of the character in the string.

Do not use the `count` method. Instead, use a **loop**, or **list comprehension**.

##### Example:
```python
print(check_character('Order of the Phoenix', 'o'))
```
##### Result
```plaintext
2
```

> Characters are case-sensitive `('A' != 'a', etc.)`.

Write the solution in `answer1.py`.


## Task 2 (4 points)

Write a function named `get_random`.
The function should:
* Take one optional parameter `number` &ndash; number of numbers to be drawn.
    **Default value is `3`.**
* Draw numbers from the range between 1 and 100 one by one; the drawn numbers cannot be repeated.
    Use the `while` loop for this and draw until you get `number` unique numbers.
    **Do not use methods `sample` and `shuffle`.**
* If an invalid parameter is passed to it, the function should **throw** an `Exception` with the message `"Invalid Data!"`.
* The function should return a sorted list of drawn numbers (from smallest to largest).

Sample function results:

##### Example:
```python
print(get_random(5))
```
##### Result (sample):
```plaintext
[2, 33, 46, 81, 100]
```

##### Example:
```python
print(get_random())
```
##### Result (sample):
```plaintext
[58, 66, 99]
```

Put the task solution in the file `answer2.py`.


## Task 3 (5 points)

We want to have the following tables in the database:
```SQL
* Readers:
    id : serial primary key,
    name : varchar(60),
    email : varchar(60),
    is_active : boolean, cannot be null, default value: true
* Books:
    id : serial primary key,
    title : varchar(60),
    price : decimal(5, 2), 
    author : varchar(60),
    publishing_houses_id: int
* PublishingHouses:
    id : serial primary key,
    name : varchar(60),
    city : varchar(20),
    address : varchar(120)
```

In the file `answers3.py` you will find a number of variables: `query_1 = ""` ... `query_10 = ""`.
Write the following SQL queries and place them in the indicated variables:

1. creating a `Readers` table (email must be unique).
2. creating a `PublishingHouses` table.
3. creating a `Books` table (add an appropriate relationship with the `PublishingHouses` table:
    * each book can have one publisher,
    * each publisher can have multiple books on offer.
4. creating a many-to-many relationship between tables `Readers` and `Books`.
5. retrieving from the database all books with a price greater than 10.
6. inserting into the `PublishingHouses` table a new publishing house named "Super Books", located in Wilderness, 120 Main Road.
7. removing the book with `id` 12.
8. selecting all readers who have ever borrowed a book (based on the many-to-many relationship between the book and the reader; see point 5).
9. deactivating the user with id 2 (set the value `is_active` to false for this user, assume the user already exists in the database).
10. adding an `date_of_birth` field to the `Readers` table to store the reader's date of birth. The field can take the `null` value.

Half a point is awarded for each query.


## Task 4 (4 points)

Using the **Flask** framework, write a website that meets the following objectives:

1. When accessed using the GET method, it displays an empty form that contains the following fields:
    * `name`: reader's first name,
    * `email`: reader's email.

2. When accessed using the POST method:
    * verifies the correctness of the data
        (it is enough to check if the name is not empty and if there is an "@" sign in the `email` field),
    * writes this data to the `Readers` table in the database (the same table as in task 3),
    * if any of the data is incorrect, instead of writing to the database, it displays an error message on the page.

Remember to connect to the database correctly and close the connection afterwards.

Write your solution in the file `answer4.py`.


## Task 5 (5 points)

Write an `EBook` class in Python. The class should have the following properties:
1. inherit from the `Book` class (look up `exam_lib` module).
2. have additional attributes: `size` (in MB) and `registration_code`.
    The registration code should not be accessible externally (remember the naming convention).
3. have an `__init__` method that takes the following data: title, author, page count, size, and registration code.
    The title, author, and page count have to be passed to the `__init__` method of the parent class.
    The `__init__` method must check if the given registration code is valid. If so &ndash; then set it;
    if not &ndash; then the code should be set to `None`.
    The code is valid if it is a string (`str`) of 16 digits.
4. have a `check_code` static method. It should take one parameter (registration code) and return a boolean value: `True` if the code is valid, `False` if not.
    The code is valid if it is a string (`str`) of 16 digits.
5. have a getter (`property`) and a setter for the `registration_code` attribute.
    * the getter should simply return the value of the registration code.
    * the setter should only set the registration code if the number is valid.

Write the solution in the file `answer5.py`.
