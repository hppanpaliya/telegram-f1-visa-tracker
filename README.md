# Telegram F1 Visa Tracker

Telegram F1 Visa Tracker is a Python script that monitors a Telegram group specifically created for Indians seeking F1 visas. It filters messages and forwards relevant ones to designated users, providing timely notifications about available visa slots.

## Features

- Monitors a Telegram group for F1 visa-related messages.
- Filters out irrelevant messages containing forbidden keywords.
- Forwards eligible messages to designated users for notification.
- Easy setup and configuration using environment variables.
- Utilizes the Telegram API and the Telethon library.

## Prerequisites

- Python 3.7 or higher
- Pip package manager
- Telegram API credentials (API ID and hash)
- Telegram group name for F1 visa slots monitoring


## Telegram API Credentials

To use the Telegram API and access your group, you need to obtain the API ID and hash. Follow the steps below to get your credentials:

1. Visit the Telegram website: https://my.telegram.org/auth.
2. Log in with your Telegram account.
3. Under "API Development Tools," create a new application.
4. Provide the required information such as the app name, short name, and platform.
5. Once the application is created, you will see the API ID and hash. Keep them secure as they are sensitive credentials.


## Installation
1. Clone this repository:
```shell 
git clone https://github.com/hppanpaliya/telegram-f1-visa-tracker.git
```
2. Navigate to the project directory:
    ```shell
    cd telegram-f1-visa-tracker
    ```
3. Install the required dependencies:
    ```shell
    pip install -r requirements.txt
    ```

## Configuration
1. Create a .env file in the root directory.
2. Add the following lines to the .env file, replacing the placeholders with your actual values:
    ```shell
    API_ID=123456
    API_HASH=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
    GROUP_NAME=F1_Visa_Slots_Only
    USER_NAME=your_telegram_username
    ```

## First Run Setup

On the first run, the script will prompt you to enter your mobile number with the country code. Follow the steps below to complete the setup:

1. Run the script using the following command:

    ```shell
    python3 main.py
    ```
2. Enter your mobile number in the format +11232312131 or +919999911111 (including the country code).
3. You will receive an OTP on your Telegram account.
4. Enter the OTP when prompted by the script to authenticate and proceed.
   
The script will connect to the Telegram API, monitor the specified group, and forward eligible messages to the designated users.

   
## Usage
Run the script using the following command:
```shell
python3 main.py
```

## Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

## License
This project is licensed under the terms of the [MIT License](https://choosealicense.com/licenses/mit/).


