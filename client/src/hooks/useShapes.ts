import { useEffect, useState } from "preact/hooks";
import { Circle, Rectangle, Shape } from "../models/Shapes";


export interface IUseShapesHook {
    shapes: Shape[];
}

export default function useShapes(): IUseShapesHook {

    const [shapes, setShapes] = useState<Shape[]>([]);

    useEffect(() => {
        setTimeout(() => setShapes([
            new Rectangle({ x: 100, y: 100, width: 100, height: 100 }),
            new Circle({ x: 200, y: 200, radius: 50, color: "red" })
        ]), 100);
    }, [])

    return { shapes };
}