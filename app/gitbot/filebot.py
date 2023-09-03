import os
import sys
import datetime
import logging
from collections import defaultdict

# Configure logger
logging.basicConfig(filename='app.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

# Set memory limit
MEMORY_LIMIT = 50 # MB
memory_usage = 0

# Check memory usage
def check_memory():
  global memory_usage
  process = psutil.Process(os.getpid())
  memory_usage = process.memory_info().rss / float(2**20)
  if memory_usage > MEMORY_LIMIT:
    logging.error("Memory limit exceeded. Freeing memory...")
    clear_memory()

# Clear memory  
def clear_memory():
  global memory_usage
  del process
  gc.collect()
  memory_usage = 0

# Check for duplicates  
def check_duplicates(filename):
  seen = defaultdict(int)
  with open(filename) as f:
    for line in f:
      seen[line] += 1
      if seen[line] > 1:
        logging.warning("Duplicate detected: %s", line)
        
# Read file
def read_file(filename):
  check_memory()
  with open(filename) as f:
    content = f.read()
    logging.info("File %s read successfully", filename)
    return content
  
# Write to file  
def write_file(filename, content):
  check_memory() 
  with open(filename, 'w') as f:
    f.write(content)
    logging.info("File %s written successfully", filename)
    
# Append to file
def append_file(filename, content):
  check_memory()
  with open(filename, 'a') as f: 
    f.write(content)
    logging.info("Appended to file %s successfully", filename)
    
# Delete file
def delete_file(filename):
  check_memory()
  if os.path.exists(filename):
    os.remove(filename)
    logging.info("File %s deleted successfully", filename)
  else:   
    logging.warning("File %s does not exist", filename)
    
# Search file    
def search_file(filename, pattern):
  check_memory()
  with open(filename) as f:
    for line in f:
      if pattern in line:
        logging.info("Pattern %s found in %s", pattern, filename)
        return True
    logging.info("Pattern %s not found in %s", pattern, filename)
    return False