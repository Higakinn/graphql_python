# from books.app import app
from books.database.init_db import init_db


def main():
    init_db()
    # app.run()


if __name__ == '__main__':
    main()