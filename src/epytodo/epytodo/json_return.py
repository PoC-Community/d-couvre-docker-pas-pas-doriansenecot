##
## EPITECH PROJECT, 2019
## Untitled (Workspace)
## File description:
## json_return
##

REGISTER_POST = {"key1" : "value1","key2" : "value2","keyN" : "valueN"}
REGISTER_RES = {"result" : "account created"}
REGISTER_ERR = {"error" : "account already exists"}

INTERNAL_ERROR = {"error" : "internal error"}

SIGNIN_POST = {"username" : "_username","password" : "_password"}
SIGNIN_RES = {"result" : "signin successful"}
SIGNIN_ERR = {"error" : "login or password does not match"}
SIGNOUT_RES = {"result" : "signout successful"}

# USER_RES = {"result" :{"Username" : "username","ID" : "id"}}
USER_ERR = {"error" : "you must be logged in"}

TASK_ID_RES = {"result" :{"title" : "_title","begin" : "_begin","end" : "_end","status" : "_status"}}
TASK_ID_ERR = {"error" : "internal error"}

USER_TASK_RES = {"result" :{"tasks" :[{"_id1" :{"title" : "_title","begin" : "_begin","end" : "_end","status" : "_status"}},{"_idN" :{"title" : "_title","begin" : "_begin","end" : "_end","status" : "_status"}}]}}
USER_TASK_ERR = {"error" : "you must be logged in"}

TASK_ID_MOD_POST = {"title" : "_title","begin" : "_begin","end" : "_end","status" : "_status"}
TASK_ID_MOD_RES = {"result" : "update done"}
TASK_ID_MOD_ERR = {"error" : "task id does not exist"}

TASK_ID_ADD_POST = {"title" : "_title","begin" : "_begin","end" : "_end","status" : "_status"}
TASK_ID_ADD_RES = {"result" : "new task added"}
TASK_ID_ADD_ERR = {"error" : "you must be logged in"}

TASK_ID_DEL_POST = {}
TASK_ID_DEL_RES = {"result" : "task deleted"}
TASK_ID_DEL_ERR = {"error" : "task id does not exist"}
