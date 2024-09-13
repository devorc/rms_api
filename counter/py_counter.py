from connectivity import py_connectivity


def fn_counter_details(request):
    counter_details = []
    try:
        hall_fk = request.get("hall_fk")
        if hall_fk == 0:
            sql = "SELECT counter_id,name,persons,seats,available_seats,hall_fk,hall_name from v_counter"
        else:
            sql = "SELECT counter_id,name,persons,seats,available_seats, hall_fk,hall_name from v_counter where hall_fk=" + str(hall_fk)
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                counter_details.append(json_data)
        return {"counter_details": counter_details}
    except Exception as e:
        print("fn_counter_details " + str(e))
        return {"counter_details": counter_details}


def fn_hall_details():
    hall_details = []
    try:
        sql = "SELECT * FROM v_hall"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                hall_details.append(json_data)
        return {"hall_details": hall_details}
    except Exception as e:
        print("fn_counter_details " + str(e))
        return {"hall_details": hall_details}


def fn_counter_manage(request):
    counter_id = request.get("counter_id")
    counter_name = request.get("name")
    seats = request.get("seats")
    hall_id = request.get("hall_id")
    try:
        result = py_connectivity.call_proc('sp_counter_inup', (
            counter_id, counter_name, seats, hall_id, None))
        return {"val": 1, "message": "Your response have been updated successfully"}
    except Exception as e:
        print("fn_counter_manage " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_counter_delete(request):
    counter_id = request.get("counter_id")
    try:
        result = py_connectivity.call_proc('sp_counter_del', (counter_id, None))
        return {"val": 1, "message": "Table have been removed successfully"}
    except Exception as e:
        print("fn_counter_delete " + str(e))
        return {"val": 0, "message": "Something went wrong"}
