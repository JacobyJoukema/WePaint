import { h } from "preact";
import Canvas from "./Canvas";
import TwitchChat from "./TwitchChat";

import styles from "./App.css";

export interface IMainProps {
    channel: string;
}

export default function Main(props: IMainProps) {
    const { channel } = props;

    return (
        <div class={styles.container}>
            <div class={styles.content}>
                <Canvas />
            </div>
            <div class={styles.sidebar}>
                <TwitchChat channel={channel} />
            </div>
        </div>
    );
}