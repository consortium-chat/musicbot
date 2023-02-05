# Musicbot

Matrix bot that posts weekly music in a room.

## Setup

1. Install [Python 3.10] and pip.

2. Clone this repository and `cd` into it.

3. Create and activate a virtual environment in the project directory:

   ```
   python3.10 -m venv .venv
   source .venv/bin/activate
   ```

4. Install [Poetry]:

   ```
   pip install poetry
   ```

5. Run `poetry install` to install dependencies.

6. Create a `.env` file in the project directory and set the following values:

   ```
   USER_ID = <matrix_user_id>
   PASSWORD = <matrix_password>
   ```

7. Run `python musicbot` to start the bot.

[Python 3.10]: https://www.python.org/downloads
[Poetry]: https://python-poetry.org

## License

[MIT](license.txt)
