# Write your movie_review function here:
def movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif 5 <= rating < 9:
    return "This one was fun."
  elif rating >= 9:
    return "Outstanding!"
print(movie_review(9))
print(movie_review(4))
print(movie_review(6))