from connectivity import py_connectivity


def fn_items():
    items = []
    try:
        sql = (
            "select item_pk_id as id,item_name,category,description,unit,default_price,DATE_FORMAT(created_at, "
            "'%d %M %Y %r') as created_at,DATE_FORMAT(updated_at, '%d %M %Y %r') as updated_at from stc_items")
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                items.append(json_data)
        return {"items": items}
    except Exception as e:
        print("fn_items " + str(e))
        return {"items": items}


def fn_manage_items(request):
    item_id = request.get("item_id")
    item_name = request.get("item_name")
    category = request.get("category")
    description = request.get("description")
    unit = request.get("unit")
    default_price = request.get("default_price")
    try:
        result = py_connectivity.call_proc('sp_items_inup',
                                           (item_id, item_name, category, description, unit, default_price, None))
        return {"val": 1, "message": "Your response have been updated successfully"}
    except Exception as e:
        print("fn_manage_items " + str(e))
        return {"val": 0, "message": "Something went wrong"}
