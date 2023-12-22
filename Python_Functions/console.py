import cmd

#class MyCommand(cmd.Cmd):
    #prompt = ">>> "

class Phonebook(cmd.Cmd):
   def __init__(self):
       super().__init__()  
       self.phonebook = {}

   def do_add(self, arg):
      """Add a contact to the phonebook"""
      if ' ' in arg:
          name, number = arg.split()
          self.phonebook[name] = number
      else:
          print("Error: Please enter a name and a number separated by a space.")

   def do_update(self, arg):
       """Update a contact in the phonebook"""
       name, number = arg.split()
       if name in self.phonebook:
           self.phonebook[name] = number
       else:
           print("Contact does not exist.")

   def do_delete(self, arg):
       """Delete a contact from the phonebook"""
       if arg in self.phonebook:
           del self.phonebook[arg]
       else:
           print("Contact does not exist.")

   def do_show(self, arg):
       """Show a contact in the phonebook"""
       if arg in self.phonebook:
           print(f"Name: {arg}, Number: {self.phonebook[arg]}")
       else:
           print("Contact does not exist.")

   def do_count(self, arg):
       """Count the number of contacts in the phonebook"""
       print(f"Number of contacts: {len(self.phonebook)}")

   #def do_quit(self, arg):
    #    '''This quits the command interpreter'''
     #   return True

   #def do_EOF(self, arg):
    #    """EOF signal to exit the program."""
     #   return True

if __name__ == '__main__':
   Phonebook().cmdloop()