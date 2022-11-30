from livereload import Server


def main():
    server = Server()
    server.watch('index.html')
    server.serve(root='.', default_filename='./index.html')


if __name__ == '__main__':
    main()
