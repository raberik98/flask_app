# flask_app
This is an example flask app.

I will follow this video for an easy introduction and then I will bring more complexity to it like MVC, Docker a SPA frontend that is rendered in the client side and then I will deploy it to the cload.

Souce video for the introduction: https://www.youtube.com/watch?v=oQ5UfJqW5Jo&t=68s

When you run the app from a container then you need to set the following environmental vairables:

- **BACKEND_HOST** (default: '0.0.0.0')
- **BACKEND_PORT** (default: 8080)


*eg.:*

```sh
    docker build -t flask-app .

    docker run -e BACKEND_PORT=8080 -p 80:8080 flask-app
```