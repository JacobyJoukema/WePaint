const tmi = require('tmi.js');
const fetch = require("node-fetch")

// Sends a shape to the Python server.
function sendShapeToServer(type, body) {
    const endpoint = `http://srv:8000/shapes/${type}`;

    const headers = {'Content-Type': 'application/json'}
    const metadata = {method: "POST", body: body, headers: headers};

    fetch(endpoint, metadata)
        .then(async response => {
            const json = await response.json();
            if (response.status === 200) {
                console.info(`onMessageHandler(): drew shape with ${JSON.stringify(json)}.`);
            } else {
                console.error(`onMessageHandler(): failed to draw shape: ${JSON.stringify(json)}.`)
            }
        })
        .catch(error => {
            console.error(`onMessageHandler(): ${error}.`);
        });
}

// Called when a message is sent to Twitch chat.
function onMessageHandler(channel, context, msg, self) {
    const tokens = msg.trim().split(" ");
    if (tokens.length == 0) {
        console.debug(`onMessageHandler(): message "${msg}" is empty.`);
        return;
    }

    const name = tokens[0];

    if (name === "!circle") {
        const body = tokens.slice(1).join(" ");
        sendShapeToServer("circle", body);
    } else if (name === "!rect") {
        const body = tokens.slice(1).join(" ");
        sendShapeToServer("rect", body);
    } else {
        console.debug(`onMessageHandler(): message "${msg}" is not a command.`);
    }
}

// Called when the bot connects to Twitch chat.
function onConnectedHandler(addr, port) {
  console.info(`onConnectedHandler(): connected to "${addr}:${port}".`);
}

const config = {channels: ["BinaryandBeers"]};
const client = new tmi.client(config);

client.on("message", onMessageHandler);
client.on("connected", onConnectedHandler);

client.connect();

