<div align="center">

# Port Status Checker

**Inspect TCP port reachability and discover exposed services from one straightforward command-line interface.**

<br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-CLI-30363D?style=for-the-badge&logo=windows-terminal&logoColor=white)
![Engine](https://img.shields.io/badge/Scan_Engine-Nmap-2E8B57?style=for-the-badge)
![Purpose](https://img.shields.io/badge/Use-Authorized_Testing-orange?style=for-the-badge)

</div>

---

## Overview

**Port Status Checker** is a menu-driven Python utility for checking whether a specific TCP port accepts connections and for running an Nmap scan against a host. It combines a quick socket-level connectivity check with service and version discovery, presenting returned host and port information in a readable terminal report.

## Key Features

- 🔌 **Single-port connectivity checks** — test a TCP port with a two-second connection timeout.
- 🛰️ **Nmap-powered scanning** — use Nmap to discover ports and gather service/version information.
- 🧭 **Host and service details** — display host state, resolved hostname, protocol, port state, service name, and available product/version details.
- 🧰 **Simple interactive menu** — switch between a socket check, an Nmap scan, and exit without restarting the script.
- 🛠️ **Useful error messages** — report common input, connection, DNS-resolution, timeout, and Nmap errors.
- ⚡ **Fast scan profile** — run Nmap with `-sV -sC -F` to request service/version detection, default scripts, and a fast scan of common ports.

## Tech Stack & Architecture

| Component | Role |
| --- | --- |
| **Python 3** | Application logic and command-line interface |
| **`socket`** | Built-in TCP connection test for a single port |
| **`python-nmap`** | Python wrapper used to invoke and read Nmap scan results |
| **Nmap** | External scanning engine for port discovery and service enumeration |

### How it works

1. **Menu selection** — the user chooses a single-port check, an Nmap scan, or exit.
2. **Socket check** — the tool accepts a host and port, validates the port range (`1–65535`), and attempts a TCP connection with a two-second timeout.
3. **Nmap scan** — the tool initializes Nmap, scans the supplied target with `-sV -sC -F`, and retrieves the hosts and protocols returned by the scan.
4. **Report** — results are printed in the terminal, including port state and available service details.
5. **Error handling** — expected connection and scanner errors are caught and displayed to the user.

## Quick Start

### 1. Prerequisites

- Python 3 installed and available from your terminal.
- Nmap installed separately. The Nmap executable is **not** installed by installing `python-nmap`.
- Network authorization to test the target host.

For Windows, install Nmap from the [official Nmap download page](https://nmap.org/download.html).

### 2. Get the project ready

Save the script as `port_scanner.py`, then open a terminal in the directory containing the file.

Create and activate a virtual environment (recommended):

**Windows — PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install python-nmap
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install python-nmap
```

### 3. Configure the Nmap executable

The script defines `NMAP_SEARCH_PATH` near the top of the file. It currently includes a machine-specific Windows path and common Windows installation paths, followed by `nmap`.

Update this list if Nmap is installed somewhere else. For example, if `nmap` is available on your system's `PATH`, you can simplify the list to:

```python
NMAP_SEARCH_PATH = ["nmap"]
```

Keep the paths that match your environment. The scanner must be able to launch the Nmap executable for option 2 to work.

### 4. Run the checker

```bash
python port_scanner.py
```

On Windows, this may also be:

```powershell
py port_scanner.py
```

Choose an option from the displayed menu:

- **1** — Check a single TCP port.
- **2** — Run an Nmap scan.
- **3** — Exit.

### Example usage

For a single-port check, enter a host you are authorized to test and a port number, such as `127.0.0.1` and `80`. The result depends on whether a service on that host accepts the connection.

For an Nmap scan, provide an authorized IP address or hostname. Nmap will scan the target using the script's configured arguments.

## Visual Proof

> **Screenshot / terminal recording placeholder**
>
> Add a screenshot of a completed scan here once you have captured output from your own environment. Remove this placeholder after adding the image.

```text
=============================================
          ADVANCED PORT SCANNER
=============================================
1. Check a Single Port (Socket)
2. Run Nmap Scan
3. Exit
=============================================
Select an option (1-3): _
```

<!-- Example image markup: ![Port Status Checker output](docs/images/port-scanner-demo.png) -->

## Scan Behavior & Limitations

- The socket option tests **one TCP port**; it is not a full port scan.
- A refused connection is reported as closed. A timeout is inconclusive: filtering, packet loss, host unavailability, or network conditions may prevent a response.
- The Nmap option uses `-F`, which limits the scan to Nmap's fast-scan set of common ports; it does not inspect every port.
- `-sV` requests service/version detection and `-sC` runs Nmap's default script set. Script results and scan completeness vary with the target, network, and permissions.
- The tool reports information Nmap returns; it does not guarantee that every service or vulnerability will be identified.
- The current implementation is designed for interactive terminal use and does not provide JSON/CSV export, asynchronous scanning, or a graphical interface.

## Ethical Use

> [!WARNING]
> Use this tool **only on systems you own or have explicit permission to assess**. Scanning networks or services without authorization may violate organizational policies or local law. You are responsible for obtaining permission, choosing an appropriate scan scope, and complying with applicable rules. Do not use scan results to access, disrupt, or damage systems.

## Contributing

Bug reports, focused improvements, and documentation fixes are welcome. When proposing changes, include the environment, steps to reproduce the issue, and relevant terminal output with sensitive information removed.

## License

No license is specified in this repository yet. Add a `LICENSE` file before presenting the project as open source, and update this section to name the chosen license.
