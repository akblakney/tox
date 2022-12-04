def show_help():
  print('''
Synopsis: general purpose, category based, todo/logging system.

Usage: tox [action] [arguments]

Actions:

  There are three actions: a (add), s (show), and r (remove). 

  --- ADD ---

  The add action takes a category name and then an entry to add to that
  category:

  tox a <category name> <entry>
    adds an entry to a category

  The category name must not include spaces, while the entry may contain spaces.
  For example, the following command adds "the godfather part 1" to the category
  "watch-list": 

    tox a watch-list the godfather part 1

  --- SHOW ---

  The show action can take either no arguments, or a category name as an argument.
  With no arguments, the command shows all categories:

  tox s
    shows all categories

  With a category name as an argument, it shows all entries in the category,
  numbered in the order they were inserted:

  tox s <category name>
    shows all items in a given category

  For example, the following command would print out all of the entries in the
  "to-read" category:
    tox s to-read

  --- REMOVE ---

  The remove action takes either a category name as an argument, or a category
  name and an index. If only a category name is given, then that entire
  category's list will be deleted. If a category name and an index is given,
  then only that index will be deleted from that category's list.

  tox r <category name>
    deletes the entire category with the given name

  tox r <category name> <index>
    removes a given index from a given category.

  For example, the following command deletes the second entry (note that
  indexing starts at zero, although this will be clear when the user uses the
  show command to view the items in a category before deleting one) in the
  todo-general category:
  
  tox r todo-general 2
''')
