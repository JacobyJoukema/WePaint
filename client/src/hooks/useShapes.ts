import { useEffect, useState } from "preact/hooks";
import Config from "../constants/Config";
import { Circle, Rectangle, Shape } from "../models/Shapes";


export interface IUseShapesHook {
    shapes: Shape[];
}

export default function useShapes(): IUseShapesHook {

    const [shapes, setShapes] = useState<Shape[]>([]);

    useEffect(() => {
        const interval = setInterval(() => {
            fetch(Config.HTTP_API_ENDPOINT, {})
                .then(res => res.json())
                .then(body => setShapes(body.map((shape: any) => {
                    switch(shape.type) {
                        case "rect" : return new Rectangle(shape);
                        case "circle" : return new Circle(shape);
                    }
                })))
        }, 1000);

        return () => clearInterval(interval);
    }, [])

    /*
    useEffect(() => {
        setTimeout(() => setShapes([
            new Rectangle({ x: 100, y: 100, width: 100, height: 100 }),
            new Circle({ x: 200, y: 200, radius: 50, color: "red" })
        ]), 100);
    }, [])
    */

    return { shapes };
}