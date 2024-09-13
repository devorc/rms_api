from connectivity import py_connectivity


def fn_suppliers():
    suppliers = []
    try:
        sql = ("select supplier_pk_id as id,name,mobile_no,email,address,DATE_FORMAT(created_at, '%d %M %Y %r') as "
               "created_at,DATE_FORMAT(updated_at, '%d %M %Y %r') as updated_at from stc_supplier")
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                suppliers.append(json_data)
        return {"suppliers": suppliers}
    except Exception as e:
        print("fn_suppliers " + str(e))
        return {"suppliers": suppliers}


def fn_manage_suppliers(request):
    supplier_id = request.get("supplier_id")
    name = request.get("name")
    email = request.get("email")
    mobile_no = request.get("mobile_no")
    address = request.get("address")
    try:
        result = py_connectivity.call_proc('sp_supplier_inup', (supplier_id, name, mobile_no, email, address, None))
        return {"val": 1, "message": "Your response have been updated successfully"}
    except Exception as e:
        print("fn_manage_suppliers " + str(e))
        return {"val": 0, "message": "Something went wrong"}
