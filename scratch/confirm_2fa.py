import os
import sys
import django

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medicenters_project.settings.dev')
django.setup()

from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice

def confirm_totp(username, token):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print(f"Error: User '{username}' does not exist.")
        return

    device = TOTPDevice.objects.filter(user=user, name='Default').first()
    if not device:
        print(f"Error: No TOTP device found for user '{username}'. Run setup_2fa.py first.")
        return

    # Verify token
    try:
        token_val = int(token)
    except ValueError:
        print("Error: Token must be a 6-digit number.")
        return

    if device.verify_token(token_val):
        device.confirmed = True
        device.save()
        print(f"Success: 2FA TOTP Device for user '{username}' has been successfully confirmed and activated!")
    else:
        print("Error: Invalid code! Please make sure your authenticator app's time is synchronized with the server.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python confirm_2fa.py <username> <6-digit-token>")
    else:
        confirm_totp(sys.argv[1], sys.argv[2])
