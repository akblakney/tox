#!/usr/bin/python3

from help import show_help
import sys
import json
import os

# by default, put file in ~/.tox
# can change if you want
FILE = '{}/.tox'.format(os.path.expanduser('~'))

# j is the json object
# category is category to add to 
# content to be added to category
def add(j, category, content):
  if category in j:
    j[category].append(content)
  else:
    cont = input('this category is not in the database, add it? [y/n] ')
    if cont == 'y' or cont == 'Y':
      j[category] = [content]

def show_category(j, category):

  if not category in j:
    raise BaseException('non-existent category')

  for i in range(len(j[category])):
    print('{}. {}'.format(i, j[category][i]))

# show them in alphabetical order
def show_categories(j):
  categories = []
  for category in j:
    categories.append(category)
  categories.sort()
  for c in categories:
    print(c)

def remove(j, category, index=None):

  if not category in j:
    raise BaseException('non-existent category')

  # remove the entire category
  if index is None:
    del j[category]
    return

  if index >= len(j[category]):
    raise BaseException('invalid index for deletion')

  j[category].pop(index)

# load all history from file
def load_json(filename):
  with open(filename, 'r') as f:
    return json.load(f)

# write to file
def write_json(filename, j):
  with open(filename, 'w') as f:
    f.write(json.dumps(j))


if __name__ == '__main__':

  j = load_json(FILE)

  n = len(sys.argv)
  if n < 2:
    raise BaseException('no action given')

  action = sys.argv[1]

  if action in ['h', '-h', '--help']:
    show_help()
    exit()

  if action == 'a':
    if n < 4:
      raise BaseException('not enough arguments for add action')
    content = ' '.join(sys.argv[3:n])
    add(j, sys.argv[2], content)

  elif action == 'r':
    if n < 3:
      raise BaseException('not enough arguments for remove action')
    if n > 3:
      remove(j, sys.argv[2], int(sys.argv[3]))
    else:
      remove(j, sys.argv[2])
    

  elif action == 's':
    if n == 2:
      show_categories(j)
    else:
      show_category(j, sys.argv[2])

  else:
    raise BaseException('invalid action')
    
  write_json(FILE, j)
