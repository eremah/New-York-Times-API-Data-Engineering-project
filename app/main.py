from fastapi import FastAPI
from . import schemas, crud, router, model
from .config import engine
from . import router

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="New York Times API",
    description="NYT API powered by FastAPI. \
    \nDevelopers: Tassiratou, Yeimi and Raphael",
    version="1.0.1"
)


@app.get('/')
def Home():
    return "Welcome to our Api"


app.include_router(router.router, tags=["NYT Books and Articles"])
# , prefix="/book"),
