import math

from connectivity import py_connectivity


def fn_order_types():
    order_types = []
    try:
        sql = "SELECT type_id as value, type_name as label from order_types"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                order_types.append(json_data)
        return {"order_types": order_types}
    except Exception as e:
        print("fn_order_types " + str(e))
        return {"order_types": order_types}


def fn_order_stat():
    order_status = []
    try:
        sql = "SELECT status_id as value, c_status as label from order_status"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                order_status.append(json_data)
        return {"order_status": order_status}
    except Exception as e:
        print("fn_order_stat " + str(e))
        return {"order_status": order_status}


def fn_take_order(request, decoded):
    print(request)
    table_fk = request.get("table_fk")
    persons = request.get("persons")
    order_type = request.get("order_type")
    user_fk = decoded.get("user_id")
    dishes = request.get("dish")
    refr = request.get("refr")
    try:
        result = py_connectivity.call_proc('sp_order', (
            table_fk, persons, order_type, user_fk, refr, None))
        val = result[5]
        for dish in dishes:
            result = py_connectivity.call_proc('sp_order_items', (
                dish['id'], dish['quantity'], dish['price'], val, None))
        result = py_connectivity.call_proc('sp_kot', (
            val, 0, 'New', None))
        return {"val": 1, "message": "Your order have been placed successfully"}
    except Exception as e:
        print("fn_take_order " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_add_order_items(request):
    order_id = request.get("order_id")
    dishes = request.get("dish")
    try:
        for dish in dishes:
            result = py_connectivity.call_proc('sp_order_items', (
                dish['id'], dish['quantity'], dish['price'], order_id, None))
        result = py_connectivity.call_proc('sp_kot', (
            order_id, 0, 'Running', None))
        return {"val": 1, "message": "Items have been added successfully"}
    except Exception as e:
        print("fn_take_order " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_running_orders():
    running_orders = []
    try:
        sql = ("SELECT order_id,order_no,table_no,persons,otype,type_name,user_name,reference from v_orders where "
               "ostatus=1 order by order_id")
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                running_orders.append(json_data)
        return {"running_orders": running_orders}
    except Exception as e:
        print("fn_running_orders " + str(e))
        return {"running_orders": running_orders}


def fn_running_orderitems(request):
    order_id = request.get("order_id")
    order_items = []
    try:
        sql = f"SELECT order_items_id,dish_name,qty,price,include_tax,parcel_type from v_order_items where order_fk={order_id} and status=1"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                order_items.append(json_data)
        return {"order_items": order_items}
    except Exception as e:
        print("fn_running_orderitems " + str(e))
        return {"order_items": order_items}


def fn_order_complete(request):
    try:
        print(request)
        (order_id, order_value, parcel_charge,
         c_gst, s_gst, total, discount, grand_total, d_percent, d_ref, d_person) = gen_bill_data(request)
        py_connectivity.call_proc('sp_order_complete', (
            order_id, order_value, parcel_charge, c_gst, s_gst, total, discount, grand_total, d_percent, d_ref,
            d_person, None))
        return {"val": 1, "message": "Order have been completed successfully"}
    except Exception as e:
        print("fn_order_status " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_remove_items(request):
    order_id = request.get("order_id")
    item_ids = request.get("item_ids")
    try:
        py_connectivity.call_proc('sp_orderitem_remove', (order_id, item_ids, None))
        return {"val": 1, "message": "Order items have been removed successfully"}
    except Exception as e:
        print("fn_remove_items " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_cancel_order(request):
    order_id = request.get("order_id")
    try:
        py_connectivity.call_proc('sp_order_cancel', (order_id, None))
        return {"val": 1, "message": "Order have been cancelled successfully"}
    except Exception as e:
        print("fn_remove_items " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def fn_reprint_bill(request):
    order_id = request.get("order_id")
    order_id = order_id.replace(" ", "")
    try:
        py_connectivity.call_proc('sp_reprint', (order_id, None))
        return {"val": 1, "message": "Bill has been printed successfully"}
    except Exception as e:
        print("fn_remove_items " + str(e))
        return {"val": 0, "message": "Something went wrong"}


def gen_bill_data(request):
    print(request, "----bg")
    order_id = request.get("order_id")
    order_items = request.get('order_items')
    order_type = request.get('order_type')
    discount = request.get('discount')
    d_percent = request.get('d_percent') if request.get('d_percent') not in [''] else 0
    d_ref = request.get("d_ref")
    d_person = request.get("d_person")
    parcel_charge = 0.00
    order_value = 0.00
    total = 0.00
    base_parcel_charge = 5
    try:
        for order_item in order_items:
            if int(order_item['include_tax']) == 1:
                order_value = (order_value + (order_item['price'] * 100 / 105))
            else:
                order_value = order_value + order_item['price']
            i = int(order_item['qty'])
            cnt = 0
            while i > 0:
                i = i - int(order_item['parcel_type'])
                cnt += 1
            parcel_charge_per_item = cnt * base_parcel_charge
            parcel_charge = parcel_charge + parcel_charge_per_item
        order_value = round(order_value, 2)
        if int(order_type) < 2:
            parcel_charge = 0.00
        tax = 2.5 / 100
        c_gst = round(order_value * tax, 2)
        s_gst = c_gst
        total = total + order_value + parcel_charge + c_gst + s_gst
        if int(discount) == 1:
            discount = round(total * d_percent / 100, 2)
        else:
            discount = 0
        grand_total = round_half_up(total - discount)
        return order_id, order_value, parcel_charge, c_gst, s_gst, total, discount, grand_total, d_percent, d_ref, d_person
    except Exception as e:
        print("gen_bill_data " + str(e))


def round_half_up(n):
    return math.floor(n + 0.5)


def fn_dash_nav():
    lst = []
    try:
        sql = "SELECT * FROM dash_show WHERE isactive =1"
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                lst.append(json_data)
        return {"dash_nav": lst}
    except Exception as e:
        print("fn_dash_nav " + str(e))
        return {"dash_nav": lst}
