__author__ = 'kristof.leroux@gmail.com'

from tweeql.exceptions import TweeQLException
from tweeql.query_runner import QueryRunner

runner = QueryRunner()
runner.run_query("SELECT text, sentiment(text) AS sentiment, location FROM Twitter WHERE text CONTAINS 'twitter';", False)
#runner.stop_query()
