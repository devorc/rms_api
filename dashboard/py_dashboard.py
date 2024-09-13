from connectivity import py_connectivity
from datetime import datetime, timedelta
from collections import defaultdict


def fn_sales(request):
    date_range = request.get('date_range')
    print(request)
    total_investment = 0
    total_sales = 0
    total_tax = 0
    records_grouped = []
    try:
        if date_range == 'today' or date_range == 'yesterday':
            start_date, end_date = fn_convert_date_range(date_range)
            sql = (f"SELECT DATE_FORMAT(dt,'%H:%i') dt,investment, sale_price, tax FROM sales_investment_1hr where "
                   f"dt between '{start_date} 00:00:00' and '{end_date} 23:59:59'")
            result, key = py_connectivity.get_result(sql)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    total_investment += data['investment']
                    total_sales += data['sale_price']
                    total_tax += data['tax']
                    records_grouped.append(data)
        else:
            start_date, end_date = fn_convert_date_range(date_range)
            sql = f"SELECT dt,investment, sale_price, tax FROM sales_overall where dt between '{start_date}' and '{end_date}'"
            result, key = py_connectivity.get_result(sql)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    total_investment += data['investment']
                    total_sales += data['sale_price']
                    total_tax += data['tax']
                    records_grouped.append(data)
        profit_loss = total_sales - total_tax - total_investment
        return {"records": records_grouped, "total_investment": total_investment, "total_sales": total_sales,
                "total_tax": round(total_tax, 2), "profit_loss": round(profit_loss, 2)}
    except Exception as e:
        print("fn_sales " + str(e))
        return {"records": []}


def fn_sales_by_category(request):
    date_range = request.get('date_range')
    records_grouped = []
    try:
        if date_range == 'today':
            sql = ("with a as (select otype, sum(grand_total) tot from orders where created_at between concat("
                   "current_date(),' 00:00:00') and current_timestamp() group by otype), b as (select sum("
                   "grand_total) as all_tot from orders where created_at between concat(current_date(),' 00:00:00') "
                   "and current_timestamp()) select ot.type_name category, ifnull(a.tot,0) as tot_price, "
                   "case when ifnull(a.tot,0)=0 then 0 else round((ifnull(a.tot,0)/all_tot)*100,2) end as perc from "
                   "order_types ot left join a on a.otype=ot.type_id left join b on 1=1")
            result, key = py_connectivity.get_result(sql)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    records_grouped.append(data)
        else:
            start_date, end_date = fn_convert_date_range(date_range)
            sql = (f"WITH cte AS ("
                   f"  SELECT SUM(tot_price) AS tot "
                   f"  FROM sales_by_category "
                   f"  WHERE dt BETWEEN '{start_date}' AND '{end_date}'"
                   f") "
                   f"SELECT s.category, "
                   f"       SUM(s.tot_price) AS tot_price, "
                   f"       ROUND((SUM(s.tot_price) / cte.tot) * 100, 2) AS perc "
                   f"FROM sales_by_category s "
                   f"JOIN cte ON 1=1 "
                   f"WHERE s.dt BETWEEN '{start_date}' AND '{end_date}' "
                   f"GROUP BY s.category, cte.tot")
            result, key = py_connectivity.get_result(sql)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    records_grouped.append(data)
        return {"records": records_grouped}
    except Exception as e:
        print("fn_sales_by_category " + str(e))
        return {"records": []}


def fn_sales_by_items(request):
    date_range = request.get('date_range')
    print(request)
    records_grouped = []
    try:
        if date_range == 'today':
            sql = ("with a as (select sum(price) as tot from order_items where dt between concat(current_date(),"
                   "' 00:00:00') and current_timestamp()) SELECT o.dish_name as items, SUM(o.price) AS price, "
                   "SUM(o.qty) as qty, round((sum(o.price)/a.tot)*100,2) perc FROM order_items o left join a on "
                   "1=1 where o.dt between concat(current_date(),' 00:00:00') and current_timestamp() GROUP BY "
                   "o.dish_name ORDER BY price DESC LIMIT 5")
            result, key = py_connectivity.get_result(sql)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    records_grouped.append(data)
        else:
            start_date, end_date = fn_convert_date_range(date_range)
            sql = (f"WITH cte AS ("
                   f"  SELECT SUM(price) AS tot "
                   f"  FROM sales_by_items "
                   f"  WHERE dt BETWEEN '{start_date}' AND '{end_date}'"
                   f") "
                   f"SELECT c.items, "
                   f"       SUM(c.price) AS price, "
                   f"       SUM(c.qty) AS qty, "
                   f"       ROUND((SUM(c.price) / cte.tot) * 100, 2) AS perc "
                   f"FROM sales_by_items c "
                   f"JOIN cte ON 1=1 "
                   f"WHERE c.dt BETWEEN '{start_date}' AND '{end_date}' "
                   f"GROUP BY c.items, cte.tot "
                   f"ORDER BY price DESC "
                   f"LIMIT 5")
            print(sql)
            result, key = py_connectivity.get_result(sql)
            if result and len(result) > 0:
                for row in result:
                    data = dict(zip(key, row))
                    records_grouped.append(data)
        return {"records": records_grouped}
    except Exception as e:
        print("fn_sales_by_items " + str(e))
        return {"records": []}


def fn_convert_date_range(date_string):
    start_date = ''
    end_date = ''
    today = datetime.today()
    if date_string == 'today':
        # Today's date
        start_date = today
        end_date = today
    elif date_string == 'yesterday':
        # Yesterday's date
        start_date = today - timedelta(days=1)
        end_date = today - timedelta(days=1)
    elif date_string == 'last7days':
        # Last 7 days
        start_date = today - timedelta(days=7)
        end_date = today
    elif date_string == 'last30days':
        # Last 30 days
        start_date = today - timedelta(days=30)
        end_date = today
    elif date_string == 'thismonth':
        # Start and end date of this month
        start_date = today.replace(day=1)
        end_date = today
    elif date_string == 'lastmonth':
        # Start and end date of last month
        first_day_of_current_month = today.replace(day=1)
        last_day_of_last_month = first_day_of_current_month - timedelta(days=1)
        start_date = last_day_of_last_month.replace(day=1)
        end_date = last_day_of_last_month
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = end_date.strftime('%Y-%m-%d')
    return start_date, end_date
