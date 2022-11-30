from livereload import Server


def main():
    server = Server()
    server.watch('yandex.html')
    server.serve(root='.', default_filename='./yandex.html')


if __name__ == '__main__':
    main()
