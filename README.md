# Weather Bot

This is a simple Telegram bot that can show the weather for a given city.

The bot uses the Telegram API and OpenWeatherMap API.

## Installation

1. Download Python 3 and Git CLI.
2. Open the console and input the following commands:

    ```sh
    git clone https://github.com/holy-alexis/weather_bot
    cd weather_bot
    ```

3. Install the required dependencies:

    ```sh
    # For Windows
    pip install -r requirements.txt

    # For Linux
    pip3 install -r requirements.txt
    ```

## Configuration

1. Open `config.py` using any IDE.
2. Insert your tokens:
    - In the variable `api_key`, insert the token from the Telegram Bot API (see [BotFather](https://t.me/BotFather) for details).
    - In the variable `OWN_key`, insert the token from the OpenWeatherMap API (see [OpenWeatherMap](https://openweathermap.org/api) for details).

## Usage

1. Back in the console, input the following commands to run the bot:

    ```sh
    # For Windows
    python weather_bot.py

    # For Linux
    python3 weather_bot.py
    ```
