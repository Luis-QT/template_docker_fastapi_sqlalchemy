""" File to init FastAPI """
import os
import time
import sentry_sdk
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.apis.routes import route as route_apis
from app.apis.master.router import router as master_router
from libraries.translator.translator import Traslator

sentry_sdk.init(
    dsn=os.getenv(
        'SENTRY_URL',
        ""
    ),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redocs",
    title="APIs",
    description="",
    version="1.0",
    openapi_url="/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https?://.*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=['Content-Type', 'Authorization', 'Requester'],
)

Traslator.load_translations()
route_apis(app)

if os.environ['APP_MODE'] != "production":
    app.include_router(master_router, tags=["Master"])

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    """ Calculates time on execute APIs """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response

@app.get("/")
async def get():
    """ Response / """
    return "Hola Mundo"

@app.get("/sentry-debug")
async def trigger_error():
    """ Generate error to test Sentry """
    division_by_zero = 1 / 0
    return division_by_zero
