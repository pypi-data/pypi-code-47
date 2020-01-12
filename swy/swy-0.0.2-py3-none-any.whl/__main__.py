from swy import Manager


if __name__ == '__main__':
    app = Manager()
    try:
        app.run()
    finally:
        app.quit()
