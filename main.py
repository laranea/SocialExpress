__author__ = 'kristof.leroux@gmail.com'

from tweeql import status_handlers
from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner

import functions

def main():
    runner = QueryRunner()
    runner.run_query("SELECT text, sentiment(text) AS sentiment, location, language(text) AS language, influence(screen_name) AS influence FROM Twitter WHERE text CONTAINS 'twitter';", False)
    #runner.stop_query()
    
main()
