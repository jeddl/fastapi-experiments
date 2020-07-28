from fastapi import FastAPI, Request


def app_init():
    app = FastAPI()

    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        print(f"Request path: {request.url.path}")  # e.g. Request path: /foo
        response = await call_next(request)
        print(
            f"Response: {response}"
        )  # <starlette.responses.StreamingResponse object at 0x7f6fd0dd37c0>
        return response

    @app.get("/foo")
    def foo():
        return {"Hello": "World"}

    @app.get("/bar")
    def bar(bar: str):
        return {"bar": bar}

    return app


application = app_init()
