import { RefObject } from "preact";
import { useState, useEffect, useCallback, useRef } from "preact/hooks";

type Layout = "landscape" | "portrait";

function getLayout(container: HTMLElement): Layout {
  console.log("getting layout", container.clientWidth, container.clientHeight);
  return container.clientWidth / container.clientHeight > 14 / 9
    ? "landscape"
    : "portrait";
}

export default function useLayout(container: RefObject<HTMLElement>): Layout {
  const [layout, setLayout] = useState<Layout>("landscape");
  const timeout = useRef<NodeJS.Timeout>();

  // Resize handler that debounces resize events.
  const onResize = useCallback(() => {
    clearTimeout(timeout.current as NodeJS.Timeout);
    timeout.current = setTimeout(() => {
      if (container.current) setLayout(getLayout(container.current));
    }, 200);
  }, []);

  // Set up resize event handler.
  useEffect(() => {
    window.addEventListener("resize", onResize);
    return () => window.removeEventListener("resize", onResize);
  }, [onResize]);

  return layout;
}
