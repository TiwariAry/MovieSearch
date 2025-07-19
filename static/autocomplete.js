document.addEventListener('DOMContentLoaded', function() {
    const movieInput = document.getElementById('movie_input');
    const movieList = document.getElementById('movie_list');

    let movies = [];

    const populateSuggestions = (movies, query) => {
        movieList.innerHTML = '';

        const filteredMovies = movies.filter((movie) =>
            movie.toLowerCase().startsWith(query.toLowerCase())
        );

        filteredMovies.forEach(movie => {
            const option = document.createElement('option');
            option.value = movie;
            movieList.appendChild(option);
        })
    }

    const getMovies = async () => {
        try {
            const url = '/api/movielist';
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(response.statusText);
            }

            movies = await response.json();
        }
        catch (error) {
            console.log(error);
        }
    }

    getMovies();

    movieInput.addEventListener('input', () => {
        populateSuggestions(movies, movieInput.value);
    });
});