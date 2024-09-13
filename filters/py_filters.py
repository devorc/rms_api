from connectivity import py_connectivity


def fn_meal_type():
    meal_type = []
    try:
        sql = "SELECT category_name as label,category_id as value from category"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                meal_type.append(json_data)
            print(meal_type, "-h")
        return {"meal_type": meal_type}
    except Exception as e:
        print("fn_meal_type " + str(e))
        return {"meal_type": meal_type}


def fn_add_meal_type(request):
    category = request.get('category')
    try:
        sql = f"insert into category (category_name) values('{category}')"
        py_connectivity.exec_qry(sql)
        return {"val": 1, "message": "Category have been added successfully"}
    except Exception as e:
        print("fn_add_meal_type " + str(e))
        return {"val": 1, "message": "Something went wrong"}


def fn_dish_type():
    dish_type = []
    try:
        sql = "SELECT type_id as value, type_name as label from dish_types"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                dish_type.append(json_data)
        return {"dish_type": dish_type}
    except Exception as e:
        print("fn_dish_type " + str(e))
        return {"dish_type": dish_type}


def fn_add_dish_type(request):
    type_name = request.get('type_name')
    try:
        sql = f"insert into dish_types (type_name) values('{type_name}')"
        py_connectivity.exec_qry(sql)
        return {"val": 1, "message": "Category have been added successfully"}
    except Exception as e:
        print("fn_add_dish_type " + str(e))
        return {"val": 1, "message": "Something went wrong"}


def fn_printer():
    printer = []
    try:
        sql = "SELECT printer_id as value, printer_name as label from printer"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                printer.append(json_data)
        return {"printer": printer}
    except Exception as e:
        print("fn_printer " + str(e))
        return {"printer": printer}


def fn_hall():
    hall = []
    try:
        sql = "SELECT hall_pk as value, hall_name as label from hall"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                hall.append(json_data)
        return {"hall": hall}
    except Exception as e:
        print("fn_hall " + str(e))
        return {"hall": hall}


def fn_reference():
    ref = []
    try:
        sql = "SELECT previlege_id as value,previlege_name as label FROM previlege"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                ref.append(json_data)
        return {"ref": ref}
    except Exception as e:
        print("fn_hall " + str(e))
        return {"ref": ref}


def fn_percentage():
    percentage = []
    try:
        sql = "SELECT label,value FROM percentage"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                percentage.append(json_data)
        return {"percentage": percentage}
    except Exception as e:
        print("fn_hall " + str(e))
        return {"percentage": percentage}
