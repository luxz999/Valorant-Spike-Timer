# ⚡ Valorant Spike Timer ⚡

A spike timer for Valorant that helps improve your timing skills by automatically detecting spike plants.

## 🔥 Features
- **Automatic Spike Detection**: Detects spike plant using screen capture.
- **⏱️ Customizable Timer**: Starts a 45-second countdown.
- **🎨 Color-Coded Timer**: 
  - **🟢 Green**: 10+ seconds remaining
  - **🟡 Yellow**: 8-10 seconds remaining
  - **🔴 Red**: <7 seconds remaining
- **💻 Transparent Overlay**: Non-intrusive to gameplay.
- **⏯️ Hotkey Support**: Press `F8` to cancel timer anytime.

## 🛠️ Installation
### Prerequisites
Make sure **Python 3.10+** is installed.

### Install Dependencies
```bash
pip install pillow keyboard
```
## 🚀 Usage
1. Run the script:
```bash
python main.py
```
2. The script will monitor the screen for the spike plant

3. Timer appears when a spike is planted.

4. Press F8 to cancel.

## ⚠️ Notes
- Supports only **1920x1080** resolution with a **16:9** aspect ratio.
- Ensure **Windowed/Borderless mode** in **Valorant** for better detection.
- Check screen coordinates if timer isn't appearing.
- 
## 📹 Showcase
<iframe src="https://streamable.com/e/j1go86" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## 🔗 Acknowledgments
Based on [itsOwen/valorant-ai-bomb-timer](https://github.com/itsOwen/valorant-ai-bomb-timer) with improvements.

##### Created by: CHAT GPT 🧠
