from connectivity import py_connectivity


def fn_category():
    category = []
    try:
        sql = (
            "select  category_name from stc_item_category")
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                category.append(json_data)
        return {"category": category}
    except Exception as e:
        print("fn_category " + str(e))
        return {"category": category}


def fn_manage_category(request):
    category_name = request.get("category")
    try:
        result = py_connectivity.call_proc('sp_category_inup',
                                           (category_name, None))
        return {"val": 1, "message": "Your response have been updated successfully"}
    except Exception as e:
        print("fn_manage_category " + str(e))
        return {"val": 0, "message": "Something went wrong"}
