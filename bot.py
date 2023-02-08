import asyncio
import logging
import os
from time import sleep

import aiohttp
import nio
import schedule
from dotenv import load_dotenv

load_dotenv(override=True)

logger = logging.getLogger("musicbot")
logging.basicConfig(level=logging.INFO)

homeserver = os.environ["HOMESERVER"]
user = os.environ["USER_ID"]
password = os.environ["PASSWORD"]
music_room = os.environ["MUSIC_ROOM"]

client = nio.AsyncClient(homeserver, user)


async def get_song_of_the_week():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://www.reddit.com/r/listentothis/top.json?t=week&limit=1"
        ) as response:
            data = await response.json()
            url: str = data["data"]["children"][0]["data"]["url"]
            title: str = data["data"]["children"][0]["data"]["title"]
            return f"{title}: {url}"


async def post_song_of_the_week(message: str):
    # Login to the homeserver
    response = await client.login(password)
    logger.info(response)

    # Send a message to the music room
    response = await client.room_send(
        room_id=music_room,
        message_type="m.room.message",
        content={
            "msgtype": "m.text",
            "body": message,
        },
    )
    logger.info(response)

    # Logout from the homeserver
    response = await client.logout()
    logger.info(response)


def song_of_the_week():
    logger.info("Posting song of the week")
    try:
        message = asyncio.run(get_song_of_the_week())
        asyncio.run(post_song_of_the_week(message))
    except Exception as e:
        logger.error(e)


def main():
    schedule.every().saturday.at("07:00").do(song_of_the_week)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == "__main__":
    main()
