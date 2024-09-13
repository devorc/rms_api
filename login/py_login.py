from connectivity import py_connectivity
from auth.py_jwt import signJWT


def fn_admin_login(request):
    try:
        username = request.get("username")
        password = request.get("password")
        sql = (
            f"select user_id,user_name,priv_id from v_users where user_name='{username}' and password='{password}' and  "
            f"status=1")
        result, _ = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            token = signJWT(result[0][0], result[0][1], result[0][2])
            return {"message": "Login Success", "token": token, "val": 1}
        else:
            return {"message": "Invalid User", "token": '', "val": 0}
    except Exception as e:
        print("fn_admin_login " + str(e))
        return {"message": "Something went wrong", "token": '', "val": 0}
