export interface Shape {
    draw: (ctx: CanvasRenderingContext2D) => void;
}

export class Rectangle implements Shape {

    public color: string;
    public x: number;
    public y: number;
    public width: number;
    public height: number;

    constructor(data: any) {
        this.color = data.color ?? "black";
        this.x = data.x;
        this.y = data.y;
        this.width = data.width;
        this.height = data.height;
    }

    public draw(ctx: CanvasRenderingContext2D) {
        ctx.fillStyle = this.color;
        ctx.fillRect(
            this.x,
            this.y,
            this.x + this.width,
            this.y + this.height
        );
    }

}

export class Circle implements Shape {

    public color: string;
    public x: number;
    public y: number;
    public radius: number;

    constructor(data: any) {
        this.color = data.color ?? "black";
        this.x = data.x;
        this.y = data.y;
        this.radius = data.radius;
    }

    public draw(ctx: CanvasRenderingContext2D) {
        ctx.fillStyle = this.color;
        ctx.beginPath();
        ctx.arc(
            this.x,
            this.y,
            this.radius,
            0,
            2 * Math.PI
        );

        ctx.fill();
    }

}