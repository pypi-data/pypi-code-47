from itertools import islice
from typing import Optional, Dict, Iterable
import argparse
from getpass import getpass

import psycopg2
from datetime import date

from typeguard import typechecked

from pubfisher.core import Publication
from pubfisher.fishers.googlescholar import PublicationGSFisher


class OriginKind:
    # Publications defining the most important models.
    PRIMARY = 'primary'

    # Publications citing one of the primary publications.
    CITES = 'cites'

    # Publications needed to understand the other publications.
    SUPPLEMENTARY = 'supplementary'


class PgInsertionSummary:
    """
    Represents a result of the *insert_into_pg_...* methods below.
    """
    @typechecked
    def __init__(self, origin_id: int, pub_ids: Dict[Publication, int]):
        self.origin_id = origin_id
        self.pub_ids = pub_ids

    def __str__(self):
        return 'Origin ID: {}\nPublication IDs:\n{}' \
            .format(self.origin_id, self.pub_ids)


class WEMTaxonomyFisher(PublicationGSFisher):
    @typechecked
    def __init__(self, host: str, db_name: str, user: str, password: str,
                 *args, **kwargs):
        super(WEMTaxonomyFisher, self).__init__(*args, **kwargs)
        self._pg_host = host
        self._pg_db_name = db_name
        self._pg_user = user
        self._pg_password = password

    def _pg_connect(self):
        return psycopg2.connect(dbname=self._pg_db_name,
                                host=self._pg_host,
                                user=self._pg_user,
                                password=self._pg_password)

    @typechecked
    def _insert_into_pg_with_existing_origin(self,
                                             pubs: Iterable[Publication],
                                             origin_id: int,
                                             offset: int=0) \
            -> PgInsertionSummary:
        """
        Inserts *pubs* into our Postgres database schema.

        :param pubs: the publications to insert
        :param origin_id: postgres id of the origin of these publications
        :param offset: optional offset within the origin specified by *origin_id*
        :return: a summary of the insertion
        """

        with self._pg_connect() as db:
            with db.cursor() as cursor:

                pub_ids = {}
                nr = 1

                for pub in pubs:
                    doc = pub.document

                    if not pub.url:
                        print('Ignored publication with no URL: {} by {}'
                              .format(doc.title, doc.authors))
                        continue

                    print('Storing publication no. {}: {}, in {} by {}, '
                          '{} citations'
                          .format(nr + offset, doc.title, pub.year, doc.authors,
                                  doc.citation_count))

                    cursor.execute('SELECT * '
                                   'FROM publications '
                                   'WHERE lower(pub_title) = lower(%(title)s)',
                                   {'title': doc.title})

                    pub_id = None
                    try:
                        pub_row = next(cursor)
                        print('    !! Publication exists already, '
                              'updating metadata only...')
                        col_names = [col.name for col in cursor.description]
                        existing_pub = dict(zip(col_names, pub_row))
                        pub_id = existing_pub['pub_id']

                        cursor.execute('UPDATE publications '
                                       'SET pub_authors = %(authors)s, '
                                       'pub_year = %(year)s, '
                                       'pub_url = %(url)s, '
                                       'pub_eprint = %(eprint)s, '
                                       'pub_citation_count = %(citation_count)s '
                                       'WHERE pub_id = %(pk)s;',
                                       {'authors': doc.authors,
                                        'year': pub.year,
                                        'url': pub.url,
                                        'eprint': pub.eprint,
                                        'citation_count': doc.citation_count,
                                        'pk': pub_id})
                    except StopIteration:
                        cursor.execute('INSERT INTO publications '
                                       '(pub_id, pub_title, pub_authors, '
                                       'pub_year, pub_abstract, pub_url, '
                                       'pub_eprint, pub_relevant,'
                                       ' pub_citation_count) '
                                       'VALUES (DEFAULT, %(title)s, %(authors)s, '
                                       '%(year)s, %(abstract)s, %(url)s, '
                                       '%(eprint)s, DEFAULT, %(citation_count)s) '
                                       'RETURNING pub_id;',
                                       {'title': doc.title,
                                        'authors': doc.authors,
                                        'year': pub.year,
                                        'abstract': doc.abstract,
                                        'url': pub.url,
                                        'eprint': pub.eprint,
                                        'citation_count': doc.citation_count})
                        pub_id = cursor.fetchone()[0]
                    finally:
                        assert pub_id is not None
                        cursor.execute('INSERT INTO publication_origins '
                                       '(pub_id, pub_origin, pub_origin_position) '
                                       'VALUES '
                                       '(%(pk)s, %(origin_id)s, %(position)s);',
                                       {'pk': pub_id,
                                        'origin_id': origin_id,
                                        'position': nr + offset})
                        pub_ids[pub] = pub_id

                        nr += 1

                return PgInsertionSummary(origin_id, pub_ids)

    @typechecked
    def _insert_into_pg(self,
                        pubs: Iterable[Publication], query_url: str,
                        origin_kind: str, cites: Optional[int]=None) \
            -> PgInsertionSummary:
        """
        Inserts *pubs* into our Postgres database schema.

        :param pubs: the publications to insert
        :param query_url: the GS query url these publications where retrieved from
        :param origin_kind: a string denoting the reason why these publications
            are of interest
        :param cites: an optional postgres id of a publication that all
            the inserted publications cite
            (should be provided if *origin_kind* is "cites")
        :return: a summary of the insertion
        """

        origin_id = None

        with self._pg_connect() as db:
            with db.cursor() as cursor:
                cursor.execute('INSERT INTO origins '
                               '(origin_id, origin_url, origin_retrieval_date, '
                               'origin_cites, origin_kind) '
                               'VALUES (DEFAULT, %(url)s, %(retrieval_date)s, '
                               '%(cites)s, %(kind)s) '
                               'RETURNING origin_id;',
                               {'url': query_url,
                                'retrieval_date': date.today(),
                                'cites': cites,
                                'kind': origin_kind})
                origin_id = cursor.fetchone()[0]

        if origin_id:
            return self._insert_into_pg_with_existing_origin(pubs, origin_id)
    
    # Model papers

    def look_for_collobert_paper(self):
        self.look_for_key_words('Natural language processing (almost) '
                                'from scratch')

    def look_for_w2v_paper(self):
        self.look_for_key_words('Efficient estimation of word '
                                'representations in vector space')

    def look_for_glove_paper(self):
        self.look_for_key_words('Glove: Global vectors for word '
                                'representation')

    def look_for_elmo_paper(self):
        self.look_for_key_words('Deep contextualized word '
                                'representations')

    def look_for_gen_pre_training_paper(self):
        self.look_for_key_words('Improving Language Understanding by '
                                'Generative Pre-Training')

    def look_for_bert_paper(self):
        self.look_for_key_words('Bert: Pre-training of deep '
                                'bidirectional transformers for '
                                'language understanding')

    def look_for_fast_text_paper(self):
        self.look_for_key_words('Advances in pre-training '
                                'distributed word representations')

    def look_for_c2w_paper(self):
        self.look_for_key_words('Finding Function in Form: '
                                'Compositional Character Models '
                                'for Open Vocabulary Word Representation')

    # Use case papers

    def look_for_multilingual_corr_paper(self):
        self.look_for_key_words('Improving Vector Space Word Representations '
                                'Using Multilingual Correlation')

    def look_for_multilingual_proj_paper(self):
        self.look_for_key_words('A representation learning framework '
                                'for multi-source transfer parsing')

    def fish_for_taxonomy(self):

        # Step 1: Store the papers of the 3 most important models.

        self.look_for_w2v_paper()
        w2v_pub = next(self.fish_all())
        w2v_summary = self._insert_into_pg((w2v_pub,), self.query_url,
                                           OriginKind.PRIMARY, cites=None)

        self.look_for_glove_paper()
        glove_pub = next(self.fish_all())
        glove_summary = self._insert_into_pg((glove_pub,), self.query_url,
                                             OriginKind.PRIMARY, cites=None)

        self.look_for_elmo_paper()
        elmo_pub = next(self.fish_all())
        elmo_summary = self._insert_into_pg((elmo_pub,), self.query_url,
                                            OriginKind.PRIMARY, cites=None)

        # Step 2: Collect the first 400/250 citations of each of the primary papers.

        def citation_count_or_zero(pub: Publication):
            doc = pub.document
            return doc.citation_count if doc.citation_count else 0

        def first_n_sorted_by_citation_count(pubs: Iterable[Publication], n):
            return sorted(islice(pubs, n), key=citation_count_or_zero, reverse=True)

        self.look_for_citations_of(w2v_pub.document)
        w2v_citations = first_n_sorted_by_citation_count(self.fish_all(), 400)

        w2v_pg_id = w2v_summary.pub_ids[w2v_pub]
        w2v_citations_summary = self._insert_into_pg(w2v_citations, self.query_url,
                                                     OriginKind.CITES,
                                                     cites=w2v_pg_id)

        self.look_for_citations_of(glove_pub.document)
        glove_citations = first_n_sorted_by_citation_count(self.fish_all(), 250)

        glove_pg_id = glove_summary.pub_ids[glove_pub]
        glove_citations_summary = self._insert_into_pg(glove_citations,
                                                       self.query_url,
                                                       OriginKind.CITES,
                                                       cites=glove_pg_id)

        self.look_for_citations_of(elmo_pub.document)
        elmo_citations = first_n_sorted_by_citation_count(self.fish_all(), 250)

        elmo_pg_id = elmo_summary.pub_ids[elmo_pub]
        elmo_citations_summary = self._insert_into_pg(elmo_citations,
                                                      self.query_url,
                                                      OriginKind.CITES,
                                                      cites=elmo_pg_id)

        print('Added the following publications:')
        print(w2v_citations_summary)
        print(glove_citations_summary)
        print(elmo_citations_summary)

        # Step 3: Add some important citations missed out by Google Scholar

        self.fish_missing_w2v_citations(w2v_pg_id)

    def fish_missing_w2v_citations(self, w2v_pg_id: int):

        self.look_for_fast_text_paper()
        ft_pub = next(self.fish_all())
        ft_summary = self._insert_into_pg((ft_pub,), self.query_url,
                                          OriginKind.CITES,
                                          cites=w2v_pg_id)

        self.look_for_multilingual_corr_paper()
        mc_pub = next(self.fish_all())
        mc_summary = self._insert_into_pg((mc_pub,), self.query_url,
                                          OriginKind.CITES,
                                          cites=w2v_pg_id)

        self.look_for_multilingual_proj_paper()
        mp_pub = next(self.fish_all())
        mp_summary = self._insert_into_pg((mp_pub,), self.query_url,
                                          OriginKind.CITES,
                                          cites=w2v_pg_id)

        self.look_for_c2w_paper()
        c2w_pub = next(self.fish_all())
        c2w_summary = self._insert_into_pg((c2w_pub,), self.query_url,
                                           OriginKind.SUPPLEMENTARY,
                                           cites=w2v_pg_id)

        print('Added the following missing citations of the w2v paper:')
        print(ft_summary)
        print(mc_summary)
        print(mp_summary)
        print(c2w_summary)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Collect publications for the '
                                                 'WEM taxonomy.')
    parser.add_argument('--host', type=str,
                        help='host of the Postgres database',
                        default='localhost')
    parser.add_argument('--db', type=str,
                        help='name of the Postgres database',
                        required=True)
    parser.add_argument('--user', type=str,
                        help='name of a user having write access to the '
                             'Postgres database (default: taxonomist)',
                        default='taxonomist')

    args = parser.parse_args()
    password = getpass('Enter password for user {}:'.format(args.user))

    fisher = WEMTaxonomyFisher(host=args.host,
                               db_name=args.db,
                               user=args.user,
                               password=password)
    fisher.fish_for_taxonomy()
