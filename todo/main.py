import logging
import time
import json
import os
from datetime import datetime
from Todo import TodoApp

logger = logging.getLogger(__name__)
logger_path =os.path.join(os.path.dirname(__file__), "app.log")
logging.basicConfig(filename=logger_path,encoding="utf-8",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



Todo = TodoApp("tasks.json")
Todo.load()
text = ("""
Welcome To advanced CLI Todo Application!
**********************************
Enter these commands to navigate through application!
        1. Add Task
        2. View Tasks
        3. Update Task
        4. Delete Task
        5. Clear All Tasks
        6. Mark Task as Completed
        7. Mark Task as Pending
        0. Exit Application
""")

def confirm():
    confirmation = input("Do you really want to continue your Action?" \
    "\t 1 - Continue" \
    "\t 2 - Cancel\n").strip()
    if confirmation.isdigit():
        if confirmation == '1':
            return True
        elif confirmation == '2':
            return False
        else:
            print("Warning! Please Enter Valid Input.")
            logger.warning("Invalid input received for confirmation prompt.")
            time.sleep(1.5)
            return confirm()
while True:
    print(text)
    command = input("Enter Command: ").strip()
    if not command:
        continue
    if command.isdigit():
        command = int(command)
        if command==1:
            new_task = input("Enter Task: ").strip()
            print(f"Task Recieved: {new_task}")
            logger.info(f"New Task Received: {new_task}")
            if not new_task:
                print("Warning! Task cannot be empty.")
                logger.warning("Attempted to add an empty task.")
                time.sleep(1.5)
                continue
            if confirm():
                try:
                    Todo.save(new_task.strip())
                    print("Task Saved")
                    logger.info(f"Task Saved: {new_task}")
                    time.sleep(1)
                    continue
                except Exception as e:
                    print(f"Error happened: {e}")
                    logger.error(f"Error happened while saving task: {e}")
            else:
                print("Cancelling Operation...")
                logger.info("User cancelled the add task operation.")
                time.sleep(1)
                continue
        elif command==2:
            try:
                option = input("1 - View All Tasks\n2 - View pending Tasks only\n").strip()
                if option.isdigit():
                    if option=='1':
                        Todo.list_todos()
                    elif option=='2':
                        Todo.list_todos("pending")
                    else:
                        print("Warning! Please Enter Valid Input.")
                        logger.warning("Invalid input received for viewing tasks option.")
                        time.sleep(1.5)
                        continue
                else:
                    print("Warning! Please Enter Only Numbers.")
                    logger.warning("Non-numeric input received for viewing tasks option.")
                    time.sleep(1.5)
                    continue
            except Exception as e:
                print(f"Error happened: {e}")
                logger.error(f"Error happened while listing tasks: {e}")
        elif command==3:
            try:
                Todo.list_todos()
                task_id = input("Enter Task ID to Update: ").strip()
                new_task = input("Enter New Task Description: ").strip()
                if task_id.isdigit():
                    tasks = Todo.load()
                    if int(task_id) not in [task["id"] for task in tasks] or int(task_id) <= 0:
                        print("Warning! Task ID does not exist.")
                        logger.warning(f"Attempted to update non-existent task ID: {task_id}")
                        time.sleep(1.5)
                        continue
                    else:
                        if confirm():
                            Todo.update_task(int(task_id), new_task)
                            print("Task Updated Successfully.")
                            logger.info(f"Task ID {task_id} updated to: {new_task}")
                            time.sleep(1)
                            continue
                        else:
                            print("Cancelling Operation...")
                            logger.info("User cancelled the update task operation.")
                            time.sleep(1)
                            continue
                else:
                    print("Warning! Please Enter Only Numbers.")
                    logger.warning("Non-numeric input received for task ID during update.")
                    time.sleep(1.5)
                    continue
            except Exception as e:
                print(f"Error happened: {e}")
                logger.error(f"Error happened while updating task: {e}")
        elif command==4:
            try:
                Todo.list_todos()
                task_id = input("Enter Task ID to Delete: ").strip()
                if task_id.isdigit():
                    tasks = Todo.load()
                    if int(task_id) not in [task["id"] for task in tasks] or int(task_id) <= 0:
                        print("Warning! Task ID does not exist.")
                        logger.warning(f"Attempted to delete non-existent task ID: {task_id}")
                        time.sleep(1.5)
                        continue
                    else:
                        if confirm():
                            Todo.delete(int(task_id))
                            print("Task Deleted Successfully.")
                            logger.info(f"Task ID {task_id} deleted.")
                            time.sleep(1)
                            continue
                        else:
                            print("Cancelling Operation...")
                            logger.info("User cancelled the delete task operation.")
                            time.sleep(1)
                            continue
            except Exception as e:
                print(f"Error happened: {e}")
                logger.error(f"Error happened while deleting task: {e}")
        elif command==5:
            try:
                if confirm():
                    Todo.clear()
                else:
                    print("Aborting Operation Getting back to home")
                    logger.info("User cancelled the clear all tasks operation.")
                    time.sleep(1)
                    continue
            except Exception as e:
                print(f"Error Happened: {e}")
                logger.error(f"Error happened while clearing tasks: {e}")
        elif command==0:
            if confirm():
                print("Exiting Application...")
                logger.info("Application exited by user.")
                time.sleep(1)
                break
            else:
                print("Cancelling Operation...")
                logger.info("User cancelled the exit operation.")
                time.sleep(1)
        elif command==6:
            try:
                Todo.list_todos("pending")
                task_id = input("Enter Task ID to Mark as Completed: ").strip()
                if task_id.isdigit():
                    tasks = Todo.load()
                    if int(task_id) not in [task["id"] for task in tasks if task["status"]=="Pending"] or int(task_id) <= 0:
                        print("Warning! Task ID does not exist.")
                        logger.warning(f"Attempted to complete non-existent task ID: {task_id}")
                        time.sleep(1.5)
                        continue
                    else:
                        if confirm():
                            Todo.complete_task(int(task_id))
                            print("Task Marked as Completed Successfully.")
                            logger.info(f"Task ID {task_id} marked as completed.")
                            time.sleep(1)
                            continue
                        else:
                            print("Cancelling Operation...")
                            logger.info("User cancelled the complete task operation.")
                            time.sleep(1)
                            continue
                
                else:
                    print("Warning! Please Enter Only Numbers.")
                    logger.warning("Non-numeric input received for task ID during complete operation.")
                    time.sleep(1.5)
                    continue
            except Exception as e:
                print(f"Error happened: {e}")
                logger.error(f"Error happened while completing task: {e}")



        elif command==7:
            try:
                Todo.list_todos("completed")
                task_id = input("Enter Task ID to Mark as Pending: ").strip()
                if task_id.isdigit():
                    tasks = Todo.load()
                    if int(task_id) not in [task["id"] for task in tasks if task["status"]=="Completed"] or int(task_id) <= 0:
                        print("Warning! Task ID does not exist.")
                        logger.warning(f"Attempted to complete non-existent task ID: {task_id}")
                        time.sleep(1.5)
                        continue
                    else:
                        if confirm():
                            Todo.set_pending(int(task_id))
                            print("Task Marked as Pending Successfully.")
                            logger.info(f"Task ID {task_id} marked as pending.")
                            time.sleep(1)
                            continue
                        else:
                            print("Cancelling Operation...")
                            logger.info("User cancelled the complete task operation.")
                            time.sleep(1)
                            continue
                
                else:
                    print("Warning! Please Enter Only Numbers.")
                    logger.warning("Non-numeric input received for task ID during complete operation.")
                    time.sleep(1.5)
                    continue
            except Exception as e:
                print(f"Error happened: {e}")
                logger.error(f"Error happened while completing task: {e}")
        else:
            print("Please Enter valid command!")
            logger.warning(f"Invalid command received: {command}")
            time.sleep(1.5)
    else:
        print("Warning! Please Enter Only Numbers.")
        logger.warning("Non-numeric input received for main command.")
        time.sleep(1.5)
        continue