<div align="center">

# 🔎 Port Status Checker

### A Python-Powered Network Security Utility

Check TCP connectivity, scan common ports, and discover network services with Nmap.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Nmap](https://img.shields.io/badge/Engine-Nmap-2E6E9E)
![Focus](https://img.shields.io/badge/Focus-Network%20Security-6C5CE7)
![Project](https://img.shields.io/badge/Type-Cybersecurity%20Project-16A085)

*Explore network reachability. Inspect services. Learn networking fundamentals.*

</div>

---

## 📌 Overview

**Port Status Checker** is an interactive command-line application built with Python that provides two ways to examine network connectivity:

- **TCP Port Check:** Attempts to connect to a user-specified host and port using Python's `socket` module.
- **Nmap Scan:** Uses Nmap to scan common ports and display detected services and available version information.

This project provides practical experience with TCP connections, port scanning, service discovery, and fundamental cybersecurity concepts.

> This is an educational networking tool, not a complete vulnerability assessment platform.

## ✨ Features

| Feature | Description |
|---|---|
| 🔌 TCP Connectivity Check | Tests whether a TCP connection can be established with a target host and port. |
| 🔍 Nmap Integration | Performs network scans using Nmap. |
| 🧩 Service Detection | Displays discovered service names and available product/version details. |
| ⚡ Fast Scanning | Uses Nmap's fast-scan option to check a reduced set of common ports. |
| 🖥️ Interactive Menu | Lets users choose a scanning option from the terminal. |
| ⏱️ Connection Timeout | Prevents a TCP connection attempt from waiting indefinitely. |

## 🧰 Tech Stack

- **Python 3** — application logic
- **Socket** — TCP connectivity testing
- **python-nmap** — Python interface for Nmap
- **Nmap** — network scanning and service discovery

## ⚙️ Requirements

Before running this project, ensure you have:

- Python 3 installed
- Nmap installed separately
- The `python-nmap` package installed
- Authorization to test the target system or network

**Important:** Installing `python-nmap` does not install the Nmap executable. Both are required for the Nmap scanning feature.

## 🚀 Installation and Setup

### 1. Verify Python

Open your terminal or Windows Command Prompt and run:

```bash
python --version
```

If your system uses `python3`, use that command instead.

### 2. Install Nmap

Download Nmap from its official website:

**https://nmap.org/download.html**

After installation, check whether it is available in your terminal:

```bash
nmap --version
```

If the command is not recognized, add the Nmap installation directory to your system's `PATH` or configure the executable path inside the Python script.

### 3. Install the Python dependency

Run:

```bash
python -m pip install python-nmap
```

### 4. Clone the repository

After uploading the project to GitHub, clone it using:

```bash
git clone <your-repository-url>
cd port-status-checker
```

Replace `<your-repository-url>` with the actual URL of your repository.

## ▶️ Running the Project

Run the Python file containing the program.

For example, if your file is named `main.py`:

```bash
python main.py
```

Follow the interactive menu to select the TCP port-checking option, run an Nmap scan, or exit the application.

*Replace `main.py` with your actual Python filename if it is different.*

## 🔍 How It Works

### Option 1: TCP Port Check

The application attempts to establish a TCP connection to the specified host and port using Python's `socket` module.

A successful connection indicates that the target accepted the TCP connection at that time.

A failed connection does **not** necessarily mean that the port is closed. Firewalls, routing problems, unavailable hosts, and service configurations can also prevent a connection.

### Option 2: Nmap Scan

The Nmap feature runs a scan using the following options:

| Argument | Purpose |
|---|---|
| `-F` | Scans a reduced set of commonly used ports. |
| `-sV` | Attempts to identify services and their versions. |
| `-sC` | Runs Nmap's default script set. |

The application then displays discovered ports and available service information, such as service names, product names, and version details.

Results depend on network conditions, target configuration, firewall rules, and Nmap's detection capabilities.

## 🖥️ Configuration Note

The original script may contain a Windows-specific path to `nmap.exe`.

That path may not work on another computer.

Before using the project on a different machine:

1. Update the hard-coded path to match your Nmap installation, or use `nmap` if it is available through your system's `PATH`.
2. Avoid publishing personal usernames or machine-specific directory paths.
3. Confirm that Nmap runs successfully from your terminal.

## 🧪 Example Workflow

1. Launch the application.
2. Select a TCP port check or Nmap scan.
3. Enter the requested host and port information.
4. Review the output displayed in the terminal.

The exact prompts and output depend on the version of the program you run.

## 🛡️ Responsible Use

**Only scan systems you own or have explicit permission to test.**

Port scanning and Nmap scripts generate network traffic and may trigger security monitoring or alerts. Never scan third-party systems or networks without authorization.

Use this tool responsibly and follow applicable laws, organizational policies, and testing permissions.

## ⚠️ Limitations

- A TCP connection check is a connectivity test, not a full security assessment.
- A failed connection does not conclusively prove that a port is closed.
- Service and version detection may be incomplete or inaccurate.
- Firewalls and network conditions can affect scan results.
- Nmap must be installed separately for the scanning functionality.
- The tool does not independently confirm whether a detected service contains a vulnerability.

## 🗺️ Future Improvements

Possible enhancements for future versions include:

- Input validation for hostnames, IP addresses, and port numbers
- Improved error handling for missing Nmap installations
- Exporting scan results to TXT, JSON, or CSV files
- Configurable scan options and connection timeouts
- Automated tests for the TCP connectivity function
- A more structured and readable scan report

## 📚 Learning Outcomes

This project offers hands-on practice with:

- Python socket programming
- TCP connectivity and port states
- Nmap integration
- Service discovery and version detection
- Network reconnaissance fundamentals
- Responsible cybersecurity testing

## 📄 License

No license has been specified yet. Add a `LICENSE` file if you want to define how other people may use, modify, or distribute this project.

---

<div align="center">

**Built as a hands-on Python and cybersecurity learning project.**

*Learn networking. Scan responsibly. Keep building.*

</div>
