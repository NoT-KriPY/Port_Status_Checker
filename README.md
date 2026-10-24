# Port Status Checker

A Python-based network utility for checking TCP port connectivity and performing Nmap scans with service detection and version identification.

## Overview

**Port Status Checker** is a command-line tool built with Python that helps users check whether a TCP port is reachable and run network scans using Nmap. It combines Python's `socket` module for direct TCP connection checks with `python-nmap` for launching Nmap scans and displaying discovered services.

This project is intended for learning and practicing networking and cybersecurity fundamentals.

## Features

- **TCP port check:** Attempt to connect to a specified host and port.
- **Nmap scanning:** Run a fast scan with service/version detection and default scripts.
- **Service details:** Display discovered ports, service names, products, and version information when available.
- **Interactive menu:** Choose a scan option or exit from the command line.
- **Connection timeout:** Avoid waiting indefinitely for a TCP connection attempt.

## Requirements

- Python 3
- Nmap installed on your computer
- The `python-nmap` Python package

> **Important:** Installing `python-nmap` does not install the Nmap executable. Install Nmap separately and ensure that it is available on your system.

## Installation

### 1. Install Nmap

Download Nmap from the official website: https://nmap.org/download.html

After installation, open a terminal or Command Prompt and check that Nmap is available:

```bash
nmap --version
```

If this command is not recognized, add Nmap to your system's `PATH` or configure the executable path in the Python script.

### 2. Install the Python dependency

```bash
python -m pip install python-nmap
```

### 3. Get the project

Download or clone this repository, then open a terminal in the project directory.

```bash
git clone <your-repository-url>
cd port-status-checker
```

Replace `<your-repository-url>` with the URL of your GitHub repository.

## Run the program

```bash
python main.py
```

If your Python file has a different name, replace `main.py` with the actual filename.

Follow the on-screen menu to select a TCP port check, run an Nmap scan, or exit.

## How it works

### TCP port check

The program attempts to establish a TCP connection to the host and port you enter. A successful connection indicates that the port accepted the connection from your machine at that time. A failed connection does not necessarily mean the port is closed; a firewall, routing issue, or service configuration may also prevent access.

### Nmap scan

The program uses `python-nmap` to call Nmap with options including:

- `-sV` — probe open ports to identify service/version information.
- `-sC` — run Nmap's default script set.
- `-F` — scan a reduced set of commonly used ports.

Results depend on network reachability, target configuration, permissions, and Nmap's detection capabilities.

## Configuration note

If the script contains a hard-coded Nmap path for a specific computer, update it to match your own installation or use the `nmap` executable available through your system's `PATH`. Avoid committing personal computer paths to a public repository.

## Example workflow

1. Start the program.
2. Select the TCP port-checking option or Nmap scan option.
3. Enter the target host and any requested port information.
4. Review the connection result or scan output.

The exact prompts and output depend on the current version of the script.

## Responsible use

Use this tool only on systems you own or have explicit permission to test. Port scanning and default NSE scripts can generate traffic and may trigger monitoring or security alerts. Do not scan networks without authorization.

## Limitations

- A TCP connection check tests reachability at the time of the attempt; it is not a complete security assessment.
- Nmap results may be incomplete or inaccurate depending on network conditions and target defenses.
- The program depends on an external Nmap installation for scan functionality.
- This is an educational project, not a replacement for a professional vulnerability assessment.

## Technologies

- Python
- `socket`
- `python-nmap`
- Nmap

## License

No license has been specified yet. If you plan to make this repository public and allow others to reuse the code, consider adding a license file.

---

**Repository description:** A Python-based network security utility for checking TCP port connectivity and performing Nmap scans with service detection, version identification, and detailed terminal output.

**Suggested GitHub topics:** `python` `cybersecurity` `port-scanner` `nmap` `network-security` `socket-programming`
