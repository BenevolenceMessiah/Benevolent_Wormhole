#!/bin/bash

echo "Installing Benevolent Wormhole..."

# Navigate to script directory
cd "$(dirname "$0")"

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Set up the program to run at boot (example using cron)
(crontab -l ; echo "@reboot $(pwd)/start.sh") | crontab -

# Attempt to rename BW to include the Swirl emoji
ORIGINAL_BW="BW"
EMOJI_BW="BW🌀"

if mv "$ORIGINAL_BW" "$EMOJI_BW" 2>/dev/null; then
    echo "Renamed $ORIGINAL_BW to $EMOJI_BW"
    chmod +x "$EMOJI_BW"
    # Create an alias for easy use
    if [ -n "$BASH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    elif [ -n "$ZSH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    else
        SHELL_CONFIG="$HOME/.profile"
    fi
    echo "alias BW='$(pwd)/$EMOJI_BW'" >> "$SHELL_CONFIG"
    echo "Alias added to $SHELL_CONFIG"
    source "$SHELL_CONFIG"
else
    echo "Failed to rename $ORIGINAL_BW to include emoji. Using standard filename."
    chmod +x "$ORIGINAL_BW"
    # Create an alias for easy use
    if [ -n "$BASH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.bashrc"
    elif [ -n "$ZSH_VERSION" ]; then
        SHELL_CONFIG="$HOME/.zshrc"
    else
        SHELL_CONFIG="$HOME/.profile"
    fi
    echo "alias BW='$(pwd)/$ORIGINAL_BW'" >> "$SHELL_CONFIG"
    echo "Alias added to $SHELL_CONFIG"
    source "$SHELL_CONFIG"
fi

echo "Installation complete! You can now use the 'BW' command."
