import json
import os

from fastapi import FastAPI
from pydantic import BaseModel


DATABASE_FILENAME = "shapes.json"


class Circle(BaseModel):
    x: float
    y: float
    r: float
    colour: str


app = FastAPI()

if not os.path.isfile(DATABASE_FILENAME):
    with open(DATABASE_FILENAME, "w") as f:
        f.write("[]")


@app.get("/", status_code=200)
async def root():
    return {}


@app.post("/shapes/circle", status_code=204)
async def circle(shape: Circle):
    item = {
        "type": "circle",
        "x": shape.x,
        "y": shape.y,
        "r": shape.r,
        "colour": shape.colour,
    }

    with open(DATABASE_FILENAME, "r") as f:
        shapes = json.load(f)

    shapes.append(item)

    with open(DATABASE_FILENAME, "w") as f:
        f.write(json.dumps(shapes))
