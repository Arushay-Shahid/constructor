class Employee:
    #initializing (constructor)
  def __init__(self):
    print('Employee Created')

    #Deleting (Destructor)  
  def __del__(self):
    print('Destructor called, Employee Deleted ')
obj = Employee()
del obj      