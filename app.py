import numpy as np
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from restapi_exception_handler import RESTAPIException
from api import router as api_router
import pickle

def App():
    app = FastAPI()

    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(RESTAPIException)
    async def uvicorn_exception_handler(request: Request, exception: RESTAPIException):
        return JSONResponse(
            status_code=exception.status_code,
            content={ "error": exception.error },
        )
    app.include_router(api_router, prefix='/api')

    return app
