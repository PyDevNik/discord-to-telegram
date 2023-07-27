# Discord to Telegram Message Forwarder

![Discord to Telegram Message Forwarder](/assets/discord_to_telegram.png)

The "Discord to Telegram Message Forwarder" is a Python-based utility that enables seamless message forwarding from a Discord server to a designated Telegram channel. This open-source project, developed by [PyDevNik](https://github.com/PyDevNik), aims to facilitate communication and provide a convenient way to keep both Discord and Telegram communities informed.

**Features:**

- **Real-time Message Forwarding:** The utility ensures that messages posted in a specific Discord server are instantly forwarded to a Telegram channel of your choice. This feature helps to maintain cross-platform communication and keep users up-to-date regardless of their preferred platform.

- **Customizable Setup:** The forwarder allows users to customize the setup according to their specific requirements. Administrators can configure the Discord server, select the desired channels, and set up the appropriate authentication tokens for secure message forwarding.

- **Selective Channel Forwarding:** Users can specify particular Discord channels whose messages should be forwarded to the Telegram channel. This flexibility ensures that only relevant information is shared between platforms, preventing unnecessary clutter.

- **Telegram Admin Panel:** The forwarder includes an an admin panel in Telegram bot.
  
**Getting Started:**

1. **Requirements:**
   - Python (version 3.X)
   - Discord API token
   - Telegram Bot token

2. **Installation:**
   - Clone the repository:
     ```bash
     git clone https://github.com/PyDevNik/discord-to-telegram.git
     cd discord-to-telegram
     ```
   - Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configuration:**
   - Obtain a Discord API token by creating a new Discord application and bot. Set the token in the configuration file.
   - Create a Telegram bot and get its token. Configure the Telegram bot token in the configuration file.
   - Customize the Discord server and channel settings for message forwarding.

4. **Usage:**
   - Run the forwarder script:
     ```bash
     cd src/bots
     python runner.py
     ```
   - The forwarder will start monitoring the specified Discord channels and forwarding messages to the designated Telegram channel.
