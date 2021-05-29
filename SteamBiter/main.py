from item import Item
from new_items import NewParserItems
import asyncio
import time

start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)


def iterret(_it):
    print(f"{_it} started work: {tic()}")
    Item(NewParserItems().get_links()[_it]).show_data()
    print(f"{_it} ended work: {tic()}")


if __name__ == "__main__":
    [iterret(i) for i in range(10)]
