from fastapi import FastAPI


def app_init():
    app = FastAPI()

    @app.get("/foo")
    def foo():
        return {"Hello": "World"}

    @app.get("/bar")
    def bar(bar: str):
        return {"bar": bar}

    return app

application = app_init()
