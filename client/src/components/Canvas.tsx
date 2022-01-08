import { h } from "preact";
import { useEffect, useState } from "preact/hooks";
import useShapes from "../hooks/useShapes";
import WindowUtil from "../utils/WindowUtil";

import styles from "./App.css";

export interface ICanvasProps {}

export default function Canvas(props: ICanvasProps) {

    const [size, setSize] = useState(0);
    const { shapes } = useShapes();

    useEffect(() => {
        return WindowUtil.onResize(() => {
            const canvas = document.getElementById("canvas") as HTMLCanvasElement;
            if (canvas == null) return;

            const width = canvas.parentElement?.clientWidth ?? 0;
            const height = canvas.parentElement?.clientHeight ?? 0;
            const size = Math.min(width, height);
            setSize(size);    
        })
    }, [])

    useEffect(() => {
        const canvas = document.getElementById("canvas") as HTMLCanvasElement;
        if (canvas == null) return;
        
        const ctx = canvas.getContext("2d");
        if (ctx == null) return;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        shapes.forEach((shape) => shape.draw(ctx));
    }, [shapes]);

    return (
        <canvas 
            id="canvas" 
            class={styles.canvas} 
            style={{ width: size, height: size }} 
            width="2000" 
            height="2000" 
        />
    );
}