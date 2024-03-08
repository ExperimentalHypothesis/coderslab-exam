class Book:
    """Represent the book.

    :param str title: book title
    :param str author: author name
    :param int pages: number of pages
    """
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def print_book_info(self):
        """
        Returns info about book.

        :rtype: str
        :return: info about book.
        """
        return (f"Book title: {self.title}\n"
                f"Book author: {self.author}\n"
                f"Number of pages: {self.pages}")
