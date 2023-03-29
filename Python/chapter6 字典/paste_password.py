import pyperclip
import sys
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
    print('Usage: py pw.')
    sys.exit()

if sys.argv[1] in PASSWORDS:
    pyperclip.copy(PASSWORDS[sys.argv[1]])
    print('Password for '+sys.argv[1]+' copied to clipboard.')
else:
    print('There is no account named'+sys.argv[1])
