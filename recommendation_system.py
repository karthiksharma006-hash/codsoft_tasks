
# Movie Recommendation System
# Content-Based Filtering

movies = {
    "Inception": ["Sci-Fi", "Thriller", "Action"],
    "Interstellar": ["Sci-Fi", "Drama", "Adventure"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Avengers: Endgame": ["Action", "Sci-Fi", "Adventure"],
    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Joker": ["Crime", "Drama", "Thriller"],
    "Jurassic Park": ["Adventure", "Sci-Fi"],
    "Mission Impossible": ["Action", "Thriller"],
}

def recommend_movies(movie_name):
    movie_name = movie_name.strip().lower()

    selected_movie = None
    for title in movies:
        if title.lower() == movie_name:
            selected_movie = title
            break

    if selected_movie is None:
        print("Movie not found. Please try another movie.")
        return

    selected_genres = set(movies[selected_movie])
    recommendations = []

    for title, genres in movies.items():
        if title == selected_movie:
            continue

        common_genres = selected_genres.intersection(genres)
        if common_genres:
            score = len(common_genres) / len(
                selected_genres.union(genres)
            )
            recommendations.append((title, score, common_genres))

    recommendations.sort(key=lambda item: item[1], reverse=True)

    print(f"\nMovies similar to '{selected_movie}':")
    for title, score, genres in recommendations[:5]:
        print(f"- {title} (Matching genres: {', '.join(sorted(genres))})")

    if not recommendations:
        print("No similar movies found.")

print("====================================")
print("     MOVIE RECOMMENDATION SYSTEM")
print("====================================")
print("Available movies:")
for movie in movies:
    print("-", movie)

while True:
    choice = input(
        "\nEnter a movie name (or 'exit' to quit): "
    )

    if choice.strip().lower() == "exit":
        print("Thank you for using the Movie Recommendation System!")
        break

    recommend_movies(choice)
