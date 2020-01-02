"""Module for the management command to backfill external_id from legacy_id."""

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from bomojo.movies.models import Movie

import pybomojo


class Command(BaseCommand):
    """Management command to backfill external_id from legacy_id."""

    help = 'Backfills external_id for movies that only have legacy_id'

    def handle(self, *args, **options):
        """Find all movies where external_id is null and backfill it.

        This method uses pybomojo to search for the movie by finding an exact
        title match.
        """
        movies = Movie.objects.filter(external_id__isnull=True)
        skipped = []

        for movie in movies:
            search_results = pybomojo.search_movies(movie.title)
            exact_result = next((result for result in search_results
                                 if result['exact']), None)

            if exact_result is None:
                skipped.append(movie)
                self.stdout.write('No match found for {}\n'.format(movie))
                continue

            external_id = exact_result['movie_id']
            try:
                movie.external_id = external_id
                movie.save(update_fields=['external_id'])
                self.stdout.write('{}: {}\n'.format(movie.legacy_id,
                                                    external_id))
            except IntegrityError:
                skipped.append(movie)
                self.stdout.write(
                    'Duplicate found for {}: {}\n'.format(movie, external_id))
                continue

        if skipped:
            self.stdout.write('Unable to backfill the following movies:\n')
            for movie in skipped:
                self.stdout.write('{}\n'.format(movie))
