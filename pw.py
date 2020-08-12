#! python3

import sys
import pyperclip

passwords = {
    'email': 'email_password',
    'fb': 'fb_password',
    'vk': 'vk_password'
}

if len(sys.argv) < 2:
    print('Usage: python3 pw.py [account name]')
    sys.exit

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('password for ' + account + ' copied in buffer')
else:
    print('Account ' + account + ' not found in the list')