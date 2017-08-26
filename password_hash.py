import argparse
import getpass
import hashlib

parser = argparse.ArgumentParser(description='SfMNet TensorFlow implementation.')

parser.add_argument('--username', type=str, help='User nickname', default='neosh')
parser.add_argument('--length',   type=int, help='Length of the password', default=50)
parser.add_argument('--web',      type=str, help='Name of the web where you will put your hash', required=True)

args = parser.parse_args()


print('Enter password 1/2:')
pw1 = getpass.getpass()
print('Enter password 2/2:')
pw2 = getpass.getpass()

if pw1 != pw2:
    print('Passwords are not same')
    exit(1)

concated_string = pw1 + args.username + args.web + pw1
sha_string = hashlib.sha512(concated_string).hexdigest().upper()
hashed_string = sha_string[:args.length]

print('Webname: {:s}'.format(args.web))
print('Username: {:s}'.format(args.username))
print('Password: {:s}'.format(hashed_string))

