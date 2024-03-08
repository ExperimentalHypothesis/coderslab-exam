from exam_lib import Book


class EBook(Book):
    def __init__(self, title: str, author: str, pages: int, size: int, registration_code: str):
        super().__init__(title, author, pages)
        self.size = size
        self.registration_code = registration_code

    @staticmethod
    def check_code(registration_code: str):
        return isinstance(registration_code, str) and len(registration_code) == 16 and registration_code.isdigit()

    @property
    def registration_code(self):
        return self._registration_code

    @registration_code.setter
    def registration_code(self, registration_code: str):
        if self.check_code(registration_code):
            self._registration_code = registration_code
        else:
            self._registration_code = None


if __name__ == "__main__":

    # initialize
    ebook = EBook("Bible", "Jesus Christ", 666, 1, "0123456789012345")

    # check all fields are set ok
    assert ebook.title == "Bible"
    assert ebook.author == "Jesus Christ"
    assert ebook.pages == 666
    assert ebook.size == 1
    assert ebook.registration_code == "0123456789012345"


    # re-set a new registration_code -- all invalid so all should fail and set to None
    ebook.registration_code = "10"
    assert ebook.registration_code is None
    ebook.registration_code = "abc"
    assert ebook.registration_code is None
    ebook.registration_code = "123abc"
    assert ebook.registration_code is None
    ebook.registration_code = "012345678901234x"
    assert ebook.registration_code is None

    # re-set a new registration_code -- valid, so set it
    ebook.registration_code = "1212121212121212"
    assert ebook.registration_code == "1212121212121212"
