
import socket
import nmap


# Your Nmap executable path
NMAP_SEARCH_PATH = [
    r"C:\Users\ACER\Desktop\Projects_for_Intern\nmap\nmap.exe",
    r"C:\Program Files (x86)\Nmap\nmap.exe",
    r"C:\Program Files\Nmap\nmap.exe",
    "nmap",
]


def socketchecker():
    """Check whether a single TCP port accepts connections."""

    target_ip = input("Please input the IP address or domain: ").strip()

    try:
        target_port = int(input("Please input the port number: ").strip())

        if not 1 <= target_port <= 65535:
            print("Invalid port. Enter a number between 1 and 65535.")
            return

        print(f"\nChecking {target_ip}:{target_port}...")

        with socket.create_connection(
            (target_ip, target_port), timeout=2
        ):
            print(f"[+] Port {target_port} is OPEN.")

    except ValueError:
        print("Invalid port number. Please enter an integer.")

    except ConnectionRefusedError:
        print(f"[-] Port {target_port} is CLOSED (connection refused).")

    except socket.timeout:
        print("[-] Connection timed out. The port may be filtered or unreachable.")

    except socket.gaierror:
        print("[-] Could not resolve the IP address or domain name.")

    except OSError as e:
        print(f"[-] Connection failed: {e}")


def nscanner():
    """Run an Nmap scan and display discovered port information."""

    target = input(
        "Enter the IP or domain to scan: "
    ).strip()

    if not target:
        print("Target cannot be empty.")
        return

    print(f"\n[+] Starting Nmap scan on {target}...")
    print("[+] Initializing Nmap...")

    try:
        # Explicitly tell python-nmap where nmap.exe is located.
        nm = nmap.PortScanner(
            nmap_search_path=NMAP_SEARCH_PATH
        )

        print(f"[+] Nmap version: {nm.nmap_version()}")
        print("[+] Scanning ports. Please wait...")

        # -sV: Detect service/version information
        # -sC: Run Nmap's default scripts
        # -F:  Scan a reduced list of common ports
        nm.scan(
            hosts=target,
            arguments="-sV -sC -F"
        )

        hosts = nm.all_hosts()

        if not hosts:
            print("[-] No hosts returned. Check the target and network.")
            return

        for host in hosts:
            host_info = nm[host]

            print("\n" + "=" * 60)
            print(f"Host IP:   {host}")
            print(f"Hostname:  {host_info.hostname() or 'Not resolved'}")
            print(f"State:     {host_info.state()}")
            print("=" * 60)

            protocols = host_info.all_protocols()

            if not protocols:
                print("No port information was returned.")
                continue

            for protocol in protocols:
                print(f"\nProtocol: {protocol.upper()}")
                print("-" * 60)

                port_info = host_info[protocol]

                for port in sorted(port_info.keys()):
                    info = port_info[port]

                    state = info.get("state", "unknown")
                    service = info.get("name", "unknown")
                    product = info.get("product", "")
                    version = info.get("version", "")
                    extra = info.get("extrainfo", "")

                    details = " ".join(
                        value for value in (product, version, extra)
                        if value
                    )

                    print(
                        f"Port: {port:<6} "
                        f"State: {state:<10} "
                        f"Service: {service:<15} "
                        f"{details}"
                    )

        print("\n[+] Scan completed.")

    except nmap.PortScannerError as e:
        print(f"\n[-] Nmap error: {e}")
        print(
            "Check that nmap.exe exists at the configured path "
            "and that the executable can run."
        )

    except Exception as e:
        print(f"\n[-] Scan failed: {e}")


def main():
    """Display the main menu."""

    while True:
        print("\n" + "=" * 45)
        print("          ADVANCED PORT SCANNER")
        print("=" * 45)
        print("1. Check a Single Port (Socket)")
        print("2. Run Nmap Scan")
        print("3. Exit")
        print("=" * 45)

        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            socketchecker()

        elif choice == "2":
            nscanner()

        elif choice == "3":
            print("See you soon!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
