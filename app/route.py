from counter import py_counter
from dashboard import py_dashboard
from dish import py_dish
from login import py_login
from filters import py_filters
from orders import py_order
from purchase import py_purchase
from report import py_report
from users import py_user


def admin_login(request):
    response = py_login.fn_admin_login(request)
    return response


def meal_type():
    response = py_filters.fn_meal_type()
    return response


def add_meal_type(request):
    response = py_filters.fn_add_meal_type(request)
    return response


def dish_type():
    response = py_filters.fn_dish_type()
    return response


def add_dish_type(request):
    response = py_filters.fn_add_dish_type(request)
    return response


def printer():
    response = py_filters.fn_printer()
    return response


def reference():
    response = py_filters.fn_reference()
    return response


def percentage():
    response = py_filters.fn_percentage()
    return response


def hall():
    response = py_filters.fn_hall()
    return response


def dish_items(request):
    response = py_dish.fn_dish_items(request)
    return response


def dish_items_user(request):
    response = py_dish.fn_dish_items_user(request)
    return response


def dish_manage(request):
    response = py_dish.fn_dish_manage(request)
    return response


def dish_delete(request):
    response = py_dish.fn_dish_delete(request)
    return response


def dish_status(request):
    response = py_dish.fn_dish_status(request)
    return response


def qty_update(request):
    response = py_dish.fn_qty_update(request)
    return response


def user_list():
    response = py_user.fn_user_list()
    return response


def user_manage(request):
    response = py_user.fn_user_manage(request)
    return response


def user_delete(request):
    response = py_user.fn_user_delete(request)
    return response


def user_status(request):
    response = py_user.fn_user_status(request)
    return response


def prv_lst():
    response = py_user.fn_prv_lst()
    return response


def order_types():
    response = py_order.fn_order_types()
    return response


def order_stat():
    response = py_order.fn_order_stat()
    return response


def take_order(request, decoded):
    response = py_order.fn_take_order(request, decoded)
    return response


def add_order_items(request):
    response = py_order.fn_add_order_items(request)
    return response


def running_orders():
    response = py_order.fn_running_orders()
    return response


def dash_nav():
    response = py_order.fn_dash_nav()
    return response


def running_orderitems(request):
    response = py_order.fn_running_orderitems(request)
    return response


def order_complete(request):
    response = py_order.fn_order_complete(request)
    return response


def remove_items(request):
    response = py_order.fn_remove_items(request)
    return response


def cancel_order(request):
    response = py_order.fn_cancel_order(request)
    return response


def order_report(request):
    response = py_report.fn_order_report(request)
    return response


def reprint_bill(request):
    response = py_order.fn_reprint_bill(request)
    return response


def order_report_items(request):
    response = py_report.fn_order_report_items(request)
    return response


def dish_report(request):
    response = py_report.fn_dish_report(request)
    return response


def counter_details(request):
    response = py_counter.fn_counter_details(request)
    return response


def hall_details():
    response = py_counter.fn_hall_details()
    return response


def counter_manage(request):
    response = py_counter.fn_counter_manage(request)
    return response


def counter_delete(request):
    response = py_counter.fn_counter_delete(request)
    return response


def purchase_list():
    response = py_purchase.fn_purchase_list()
    return response


def add_purchase(request):
    response = py_purchase.fn_add_purchase(request)
    return response


def sales(request):
    response = py_dashboard.fn_sales(request)
    return response


def sales_by_category(request):
    response = py_dashboard.fn_sales_by_category(request)
    return response


def sales_by_items(request):
    response = py_dashboard.fn_sales_by_items(request)
    return response