import json
import os
from typing import Optional
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel


DATABASE_FILENAME = "shapes.js"


class Circle(BaseModel):
    x: float
    y: float
    r: float
    colour: str


class Rectangle(BaseModel):
    x: float
    y: float
    w: float
    h: float
    colour: str


class ResponseID(BaseModel):
    id: str


app = FastAPI()

if not os.path.isfile(DATABASE_FILENAME):
    with open(DATABASE_FILENAME, "w") as f:
        f.write("shapes = []")


@app.get("/", status_code=200)
async def root() -> dict:
    return {}


@app.post("/shapes/circle", response_model=ResponseID, status_code=200)
async def add_circle(shape: Circle) -> ResponseID:
    item = {
        "type": "circle",
        "id": str(uuid4()),
        "x": shape.x,
        "y": shape.y,
        "r": shape.r,
        "colour": shape.colour,
    }

    with open(DATABASE_FILENAME, "r") as f:
        shapes = json.loads(f.read()[8:])

    shapes.append(item)

    with open(DATABASE_FILENAME, "w") as f:
        f.write("shapes = %s" % json.dumps(shapes))

    return ResponseID(id=item["id"])


@app.post("/shapes/rect", status_code=204)
async def add_rect(shape: Rectangle) -> ResponseID:
    item = {
        "type": "rect",
        "id": str(uuid4()),
        "x": shape.x,
        "y": shape.y,
        "w": shape.w,
        "h": shape.h,
        "colour": shape.colour,
    }

    with open(DATABASE_FILENAME, "r") as f:
        shapes = json.loads(f.read()[8:])

    shapes.append(item)

    with open(DATABASE_FILENAME, "w") as f:
        f.write("shapes = %s" % json.dumps(shapes))

    return ResponseID(id=item["id"])


@app.delete("/shapes/circle/{id}", status_code=204)
async def del_circle(id: str) -> dict:
    with open(DATABASE_FILENAME, "r") as f:
        shapes = json.loads(f.read()[8:])

    shapes = [
        shape
        for shape in shapes
        if not (shape["id"] == id and shape["type"] == "circle")
    ]

    with open(DATABASE_FILENAME, "w") as f:
        f.write("shapes = %s" % json.dumps(shapes))

    return {}


@app.delete("/shapes/rect/{id}", status_code=204)
async def del_rect(id: str) -> dict:
    with open(DATABASE_FILENAME, "r") as f:
        shapes = json.loads(f.read()[8:])

    shapes = [
        shape for shape in shapes if not (shape["id"] == id and shape["type"] == "rect")
    ]

    with open(DATABASE_FILENAME, "w") as f:
        f.write("shapes = %s" % json.dumps(shapes))

    return {}
