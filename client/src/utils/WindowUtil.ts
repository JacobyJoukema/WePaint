import Config from "../constants/Config";

export default class WindowUtil {

    public static onResize(callback: () => void) {
        callback();
        const handler = this._debounce(
            Config.RESIZE_DEBOUNCE_DELAY, 
            callback
        )
        
        window.addEventListener("resize", handler);
        return () => window.removeEventListener("resize", handler);
    }

    private static _debounce(delay: number, ...funcs: Function[]) {
        let timeout: NodeJS.Timeout;
        const handler = () => funcs.forEach((func: Function) => func());
        return () => {
          clearTimeout(timeout);
          timeout = setTimeout(handler, delay);
        };
      }
}