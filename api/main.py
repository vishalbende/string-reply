import sys

sys.path.append("..")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from uvicorn import Config, Server



# from api.routers.bulk_update import router as bulk_update
# from api.validator import UnicornException
from settings import CORS_ORIGINS
from string_reply.v1  import router as string_reply_router
from string_reply.v2  import router as rule_based_router

def _get_app():
    app = FastAPI(
        title="String reply",
        openapi_tags=[
            {
                "name": "Backend",
                "description": "String reply",
            },
        ],
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(string_reply_router)
    app.include_router(rule_based_router)
    return app


def _start_uvicorn(app: "FastAPI"):
    config = Config(
        app=app,
        host="0.0.0.0",
        port="8000",
        loop="uvloop",
        log_level="error",
    )
    server = Server(config=config)
    server.run()




def main():
    _start_uvicorn(app=_get_app())


