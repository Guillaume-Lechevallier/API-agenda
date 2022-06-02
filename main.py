import web

# Generating routes
urls = (
    '/c=(.*)', 'Celsus',
    'favicon.ico'
)
app = web.application(urls, globals())


class Celsus:
    def GET(self, value):
        print(value)





if __name__ == "__main__":
    app.run()
