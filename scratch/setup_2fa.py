import os
import sys
import django
import qrcode
from pathlib import Path

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicenters_project.settings.dev')
django.setup()

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

def setup_totp(username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Error: User '{username}' does not exist.")
        return

    # Check if a TOTP device already exists
    device = TOTPDevice.objects.filter(user=user, name='Default').first()
    if device:
        print(f"TOTP Device for user '{username}' already exists.")
    else:
        # Create a new TOTP Device
        device = TOTPDevice.objects.create(user=user, name='Default', confirmed=False)
        print(f"Created new TOTP device for user '{username}'.")

    # Generate provisioning URI for Google Authenticator/Authy
    print("\n" + "="*50)
    print(f"2FA Setup for user: {username}")
    print("="*50)
    print(f"Provisioning URI (for manual entry or scanning):")
    print(device.config_url)
    print("\nSecret Key (Base32):", device.bin_key)
    print("="*50)
    print("\nINSTRUCTIONS:")
    print("1. Scan the Provisioning URI above with your Authenticator App (Google Authenticator, Authy, Microsoft Authenticator, etc.) or manually enter the Secret Key.")
    print("2. Once scanned, confirm the device by running the confirmation script:")
    print(f"   python confirm_2fa.py {username} <6-digit-code-from-app>")
    print("="*50 + "\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python setup_2fa.py <username>")
    else:
        setup_totp(sys.argv[1])
