import os
import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='metascope.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def enable_firewall():
    """Enable Windows Firewall."""
    try:
        subprocess.run(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'on'], check=True)
        logging.info('Windows Firewall enabled successfully.')
    except subprocess.CalledProcessError as e:
        logging.error(f'Failed to enable Windows Firewall: {e}')


def set_advanced_security_policies():
    """Set advanced security policies."""
    try:
        # Example: Disable SMBv1
        subprocess.run(['Set-SmbServerConfiguration', '-EnableSMB1Protocol', 'False', '-Force'], shell=True, check=True)
        logging.info('Advanced security policies configured successfully.')
    except subprocess.CalledProcessError as e:
        logging.error(f'Failed to set advanced security policies: {e}')


def monitor_system_logs():
    """Monitor system logs for suspicious activities."""
    try:
        event_log_cmd = 'Get-EventLog -LogName Security -Newest 5'
        result = subprocess.run(['powershell', '-Command', event_log_cmd], capture_output=True, text=True, check=True)
        logging.info(f'Recent security log entries:\n{result.stdout}')
    except subprocess.CalledProcessError as e:
        logging.error(f'Failed to retrieve system logs: {e}')


def apply_security_updates():
    """Apply security updates."""
    try:
        subprocess.run(['powershell', '-Command', 'Install-WindowsUpdate -AcceptAll -AutoReboot'], check=True)
        logging.info('Security updates applied successfully.')
    except subprocess.CalledProcessError as e:
        logging.error(f'Failed to apply security updates: {e}')


def main():
    logging.info('MetaScope Security Enhancement Started.')
    
    enable_firewall()
    set_advanced_security_policies()
    monitor_system_logs()
    apply_security_updates()
    
    logging.info('MetaScope Security Enhancement Completed.')


if __name__ == '__main__':
    main()