import coloredlogs
import logging
import requests

if __name__ == "__main__":
    coloredlogs.install()

    logging.info("Starting...")

    # TODO: Derive time boundaries of the mint.
    beg_time = None
    end_time = None

    # Get the shapes from the server.
    params = {"beg_time": beg_time, "end_time": end_time}
    response = requests.get("https://srv:8000/shapes", params=params)
    response.raise_for_status()

    shapes = response.json()
    logging.info(f"Received {len(shapes)} shapes from the server:")

    # TODO: Render the shapes to an image.

    # TODO: Save file

    logging.info("Finished.")