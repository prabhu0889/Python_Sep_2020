class Book:

    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author
        self.reviews = []

    def __str__(self):
        return f"{self.id}, {self.name}, {self.author}, {self.reviews}"

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews


class Reviews:

    def __init__(self, id, description, rating):
        self.id = id
        self.description = description
        self.rating = rating

    def __str__(self):
        return f"{self.id}, {self.description}, {self.rating}"
