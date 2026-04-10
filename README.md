# 🕵️‍♂️ Digital Footprint Analyzer

A real-time local network surveillance dashboard that monitors your machine's internet activity. Ever wonder what servers your applications are talking to in the background? The Digital Footprint Analyzer hooks into your system's active connections, maps them to the respective applications, and geolocates the destination IPs to show you exactly where your data is going.

## ✨ Features

- **Real-Time Network Scanning:** Live monitoring of all established outbound internet connections.
- **Process Identification:** Matches active connections back to their parent executable (e.g., `chrome.exe`, `discord.exe`).
- **IP Geolocation:** Resolves remote IP addresses to their Country, City, and ISP.
- **Beautiful Glassmorphism UI:** A sleek, fully responsive dark-mode dashboard with dynamic animations. 
- **Privacy First:** All network data is analyzed directly on your machine.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ installed on your system.

### Installation

1. Download or locate the project folder `DigitalFootprintAnalyzer`.
2. Ensure you have the required dependencies by installing them via `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the included batch script from the root directory:
   ```cmd
   .\run.bat
   ```
2. Wait for the Flask server to initialize.
3. Open your web browser and navigate to:
   **http://127.0.0.1:5000**

*Note: For the best results and to see ALL system-level connections without access biases, you may occasionally need to run the script or terminal as an Administrator.*

## 🧠 Architecture

- **Backend (`sensor.py` & `app.py`):** Uses Python, `Flask` for the API/server, `psutil` for reading system network data, and `requests` for hitting the external IP-API for geolocation.
- **Frontend (`index.html` & `style.css`):** Built with HTML, Vanilla Javascript, and pure CSS. Designed with modern web aesthetics specifically utilizing glassmorphism UI patterns.

## ⚠️ Limitations & Notes

This tool queries free, rate-limited public APIs for IP Geolocation (`ip-api.com`). To prevent temporary API blacklisting from the provider, the script purposefully limits the number of new IP resolves per scan by default.
