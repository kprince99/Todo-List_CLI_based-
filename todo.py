import typer
import sys
import os

app = typer.Typer(add_completion=False)

done_list = "done.txt"
task_list = "task_list.txt"

@app.command()
def help():
    todohelp='\n'"""Usage :- 
        $ todo add "todo item"  # Add a new todo
        $ todo ls               # Show remaining todos
        $ todo del NUMBER       # Delete a todo
        $ todo done NUMBER      # Complete a todo
        $ todo help             # Show usage
        $ todo report           # Statistics"""'\n'
    sys.stdout.buffer.write(todohelp.encode('utf8'))

@app.command()
def ls():
  if os.path.isfile(task_list): 
        with open(task_list, 'r') as reader:
            content = reader.readlines()    
        d_len=len(content)
        if d_len != 0:
            st=""
            for line in content:
                st+='[{}] {}'.format(d_len,line)
                d_len-=1
            sys.stdout.buffer.write(st.encode('utf8'))			# Print the Tasks in Reverse Order in UTF-8 Encoding as the default print() generates unexpected results.
        else:
            print ("There are no pending todos!")


@app.command()
def add(task: str):   
   if os.path.isfile(task_list): 
        with open(task_list, 'r') as r:
            data = r.read()
        with open(task_list, 'w') as fileMod:
            fileMod.write(task+'\n'+data)
   else:
        with open(task_list, 'w') as writeFile:
            writeFile.write(task+'\n')
   print('Task Added SuccessFully: "{}"'.format(task))
   
@app.command()
def done(num: int):
    if os.path.isfile(task_list):
        with open(task_list) as fileMod:
            content = fileMod.readlines()
        no_of_list = len(content)
        if num <=0 or num > no_of_list:
            print ("Error: Entered task number #{} doesn't exist".format(num))   
        else:
            with open(task_list, 'w') as todoFileMod:
                if os.path.isfile(done_list):
                    with open(done_list, 'r') as doneFile:
                        data = doneFile.read()
                    with open(done_list, 'w') as doneWrite:
                        for line in content:
                            if no_of_list == num:
                                doneWrite.write(line)
                            else:
                                todoFileMod.write(line)
                            no_of_list-=1
                        doneWrite.write(data)
                else:
                    with open(done_list ,'w') as doneWrite:
                        for line in content:
                            if no_of_list == num:
                                doneWrite.write(line)
                            else:
                                todoFileMod.write(line)
                            no_of_list-=1        
            print("Marked todo #{} as done.".format(num))   
    else:
	    print("Error: todo #{} does not exist.".format(num))  


@app.command()
def report():
 if os.path.isfile(task_list): 
    if os.path.isfile(done_list):
        with open(task_list,'r') as todoFile:
            todoData=todoFile.readlines()
            print("###### Recent Pending Tasks ###### \n")
            for line in todoData:
                print(line.strip())
        with open(done_list,'r') as doneFile:
            doneData=doneFile.readlines()
            print("###### Completed Tasks ###### \n")
            for line in doneData:
                print(line.strip())

               
if __name__ == "__main__":
    app()