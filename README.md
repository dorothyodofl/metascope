# MetaScope

MetaScope is a comprehensive security tool designed to enhance the defenses of Windows systems. It provides advanced security configurations and monitors system activities to protect against threats and vulnerabilities.

## Features

- **Enable Windows Firewall:** Automatically enables the Windows Firewall to protect your system from unauthorized access.
- **Advanced Security Policies:** Configures advanced security policies, such as disabling SMBv1, to safeguard against known vulnerabilities.
- **System Log Monitoring:** Monitors system logs for suspicious activities, providing insights into potential security threats.
- **Security Updates:** Automatically installs security updates to ensure that your system is protected against the latest threats.

## Requirements

- Windows operating system.
- Python 3.x installed.
- Administrative privileges to apply security settings and updates.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/metascope.git
   ```

2. Navigate to the project directory:

   ```bash
   cd metascope
   ```

3. Run MetaScope:

   ```bash
   python metascope.py
   ```

## Usage

- Run the script with administrative privileges to ensure all security configurations can be applied.
- Check `metascope.log` file for detailed logs of actions taken and any potential errors encountered during execution.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Note:** This script uses PowerShell commands for certain operations. Ensure that PowerShell is available and properly configured on your system.