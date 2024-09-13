from connectivity import py_connectivity


def fn_user_list():
    user_list = []
    try:
        sql = ("select user_id as id,user_id,priv_id,previlege_name,user_name,password,DATE_FORMAT(login_created_at, "
               "'%d %M %Y %r') as login_created_at,DATE_FORMAT(login_updated_at, '%d %M %Y %r') as login_updated_at,"
               "status from v_users where priv_id!=1")
        print(sql)
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                user_list.append(json_data)
        return {"user_list": user_list}
    except Exception as e:
        print("fn_user_list " + str(e))
        return {"user_list": user_list}


def fn_user_manage(request):
    print(request, "-b")
    user_id = request.get("user_id")
    user_name = request.get("user_name")
    password = request.get("password")
    priv_id = request.get("priv_id")
    try:
        result = py_connectivity.call_proc('sp_user_inup', (
            user_id, user_name, password, priv_id, None))
        return {"val": 1, "message": "Your response have been updated successfully"}
    except Exception as e:
        print("fn_dish_manage " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_user_delete(request):
    user_id = request.get("user_id")
    try:
        result = py_connectivity.call_proc('sp_user_del', (user_id, None))
        return {"val": 1, "message": "User have been removed successfully"}
    except Exception as e:
        print("fn_dish_delete " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_user_status(request):
    user_id = request.get("user_id")
    status = request.get("status")
    try:
        sql = f"update users set status={status}  where user_id={user_id}"
        result = py_connectivity.exec_qry(sql)
        return {"val": 1, "message": "User status have been updated successfully"}
    except Exception as e:
        print("fn_user_status " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_prv_lst():
    prv_lst = []
    try:
        sql = "SELECT previlege_id,previlege_name FROM previlege"
        result, key = py_connectivity.get_result(sql)
        k = ['value', 'label']
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(k, row)))
                prv_lst.append(json_data)
        return {"prv_lst": prv_lst}
    except Exception as e:
        print("prv_lst " + str(e))
        return {"prv_lst": prv_lst}
