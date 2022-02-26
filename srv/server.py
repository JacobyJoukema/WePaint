import json
import os
from typing import Optional
from uuid import uuid4

from database import (connect_database, create_circle_table, create_rect_table,
                      del_circle, del_rect, get_circles, get_rectangles,
                      insert_circle, insert_rect)
from fastapi import FastAPI
from pydantic import BaseModel


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


class Shapes(BaseModel):
    circles: list[Circle]
    rectangles: list[Rectangle]


class ResponseID(BaseModel):
    id: str


app = FastAPI()


@app.get("/", status_code=200)
async def root() -> dict:
    return {}


@app.get("/shapes", response_model=Shapes, status_code=200)
async def get_shapes(beg_time: int = None, end_time: int = None) -> Shapes:
    with connect_database() as conn:
        circles = get_circles(conn, beg_time, end_time)
        rects = get_rectangles(conn, beg_time, end_time)

        circle_resp = []
        rect_resp = []
        for circle in circles:
            circle_resp.append(
                {
                    "id": circle[0],
                    "colour": circle[1],
                    "x": circle[2],
                    "y": circle[3],
                    "r": circle[4],
                    "type": "circle",
                }
            )
        for rect in rects:
            rect_resp.append(
                {
                    "id": rect[0],
                    "colour": rect[1],
                    "x": rect[2],
                    "y": rect[3],
                    "w": rect[4],
                    "h": rect[5],
                    "type": "rect",
                }
            )

        resp = circle_resp + rect_resp
        resp.sort(lambda x: x.id)
        return resp


@app.post("/shapes/circle", response_model=ResponseID, status_code=200)
async def add_circle(shape: Circle) -> ResponseID:
    with connect_database() as conn:
        item = {
            "id": str(uuid4()),
            "x": shape.x,
            "y": shape.y,
            "r": shape.r,
            "colour": shape.colour,
        }

        insert_circle(conn, item)

        return ResponseID(id=item["id"])


@app.post("/shapes/rect", response_model=ResponseID, status_code=200)
async def add_rect(shape: Rectangle) -> ResponseID:
    with connect_database() as conn:

        item = {
            "id": str(uuid4()),
            "x": shape.x,
            "y": shape.y,
            "w": shape.w,
            "h": shape.h,
            "colour": shape.colour,
        }

        insert_rect(conn, item)

        return ResponseID(id=item["id"])


@app.delete("/shapes/circle/{id}", status_code=204)
async def circle_del(id: str) -> dict:
    with connect_database() as conn:

        del_circle(conn, id)
        return {}


@app.delete("/shapes/rect/{id}", status_code=204)
async def rect_del(id: str) -> dict:
    with connect_database() as conn:
        del_rect(conn, id)

        return {}


def main() -> FastAPI:
    with connect_database() as conn:
        print("Init DB")

        create_circle_table(conn)
        create_rect_table(conn)

        get_circles(conn, None, None)
        get_rectangles(conn, None, None)

        return app
