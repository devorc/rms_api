from connectivity import py_connectivity


def fn_order_report(request):
    orders = []
    from_dt = request.get('from_dt')
    to_dt = request.get('to_dt')
    try:
        sql = (f"SELECT order_no,type_name as order_type,DATE_FORMAT(created_at, '%d %M %Y %r') as created_at,"
               f"DATE_FORMAT(updated_at, '%d %M %Y %r') as updated_at,user_name,order_value,parcel_charge,"
               f"c_gst,s_gst,order_total,discount,grand_total,dis_perc,dis_ref,dis_person,reference,table_no,"
               f"persons,user_name,order_id as id from v_orders where updated_at between '{from_dt}' and '{to_dt}' "
               f"and ostatus=2")
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                if str(json_data['table_no']) == "0":
                    json_data['table_no'] = '-'
                if str(json_data['persons']) == "0":
                    json_data['persons'] = '-'
                if str(int(json_data['parcel_charge'])) == "0":
                    json_data['parcel_charge'] = '-'
                if not json_data['dis_ref']:
                    json_data['dis_ref'] = '-'
                if not json_data['dis_person']:
                    json_data['dis_person'] = '-'
                json_data['discount_text'] = str(json_data['discount']) + "(" + str(json_data['dis_perc']) + "%)"
                orders.append(json_data)
        return {"orders": orders}
    except Exception as e:
        print("fn_order_report " + str(e))
        return {"orders": orders}


def fn_order_report_items(request):
    dish_items = []
    order_id = request.get('order_id')
    try:
        sql = (f"select dish_name, include_tax, sum(qty) qty, sum(price) price from v_order_items where "
               f"order_fk={order_id} and status=1 group by dish_name, include_tax")
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            for row in result:
                json_data = dict(list(zip(key, row)))
                json_data['price'] = round(json_data['price'], 2)
                if json_data["include_tax"] == 1:
                    price = json_data['price'] * 100 / 105
                    price = round(price, 2)
                    json_data['price'] = price
                dish_items.append(json_data)
        return {"dish_items": dish_items}
    except Exception as e:
        print("fn_order_report_items " + str(e))
        return {"dish_items": dish_items}


def fn_dish_report(request):
    dish = []
    from_dt = request.get('from_dt')
    to_dt = request.get('to_dt')
    try:
        sql = (f"SELECT o.dish_name, dt.type_name as dish_type,d.including_tax, c.category_name as dish_category, "
               f"sum(o.qty) as tot_qty,round(sum(o.price),2) as tot_price FROM rms.order_items o join rms.dish_items "
               f"d on o.dish_fk=d.dish_id join rms.dish_types dt on d.dish_type_fk=dt.type_id join rms.category c on "
               f"c.category_id=d.category_fk where o.dt between '{from_dt}' and '{to_dt}'  and o.status=1 group by "
               f"o.dish_name,dt.type_name, c.category_name")
        result, key = py_connectivity.get_result(sql)
        if result and len(result) > 0:
            cnt = 1
            for row in result:
                json_data = dict(list(zip(key, row)))
                json_data["id"] = cnt
                if json_data["including_tax"] == 1:
                    price_in = round(json_data['tot_price'], 2)
                    price_ex = json_data['tot_price'] * 100 / 105
                    price_ex = round(price_ex, 2)
                    json_data['price_exc'] = price_ex
                    json_data['price_inc'] = price_in

                else:
                    tax = 5 / 100
                    price_ex = round(json_data['tot_price'], 2)
                    price_in = json_data['tot_price'] + (json_data['tot_price'] * tax)
                    price_in = round(price_in, 2)
                    json_data['price_exc'] = price_ex
                    json_data['price_inc'] = price_in
                cnt = cnt + 1
                dish.append(json_data)
        return {"dish": dish}
    except Exception as e:
        print("fn_dish_report " + str(e))
        return {"dish": dish}
