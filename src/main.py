from src.helper.Indexer import Indexer
from conf.config import settings
import argparse
import log4j

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Indexer")
    parser.add_argument("--hello_message", default="Hello Word", required=True)
    parser.add_argument("--end_message", default="Bye Bye, have a nice day", required=True)

    args = parser.parse_args()

    print(args.hello_message)

    url = settings.url
    indexer = Indexer(url)
    document = {"name": "Albert", "date_of_birth": "2000-09-01"}
    indexer.index(document)

    print(args.end_message)
