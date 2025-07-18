# En este archivo puedes definir los modelos de reseñas si lo necesitas. En este caso, es opcional.
class Review:
    def __init__(self, productId, user, review, rating, timestamp):
        self.productId = productId
        self.user = user
        self.review = review
        self.rating = rating
        self.timestamp = timestamp
