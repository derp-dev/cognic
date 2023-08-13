import os, sys, docker, json

# Check if the number of arguments passed is valid  (1 or 2 only)
if len(sys.argv) > 1:
  for arg in sys.argv[1:]:
    # Handle extra arguments
    if arg == '-h':
      # Print help message
    elif arg == '-v':
        # Print version
        sys.argv.remove(arg)
    else:
        sys.argv.remove(arg)
    
elif len(sys.argv) < 2:
  print('No arguments passed')
  exit()
elif (sys.argv[1] != None):
  print(f'Init script name: {sys.argv[0]}')
  print('additional parameters passed: ' + (sys.argv[1]))
else:
  print(f'main parameter object passed: {sys.argv[1]}')

prompt = []

for line in args.split('\n'):
  prompt.append(line)