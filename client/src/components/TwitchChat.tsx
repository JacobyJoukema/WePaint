import { h } from "preact";
import Config from "../constants/Config";

export interface ITwitchChatProps {
    channel: string;
}

export default function TwitchChat(props: ITwitchChatProps) {
    const { channel } = props;
    return (
        <iframe 
            src={`https://www.twitch.tv/embed/${channel}/chat?parent=${Config.PARENT_DOMAIN}`}
            height="100%"
            width="100%"
        />
    );
} 
