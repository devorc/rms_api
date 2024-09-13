import json
import sys
from pathlib import Path
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware

from auth import py_jwt

env_path = str(Path(__file__).absolute().parents[1] / "config.env")
load_dotenv(env_path)

sys.path.append(str(Path(__file__).absolute().parents[1]))

auth_scheme = py_jwt.JWTBearer()

origins = ["*"]
app = FastAPI()

import route

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"Info": "In live"}


@app.get("/rms/")
async def index():
    return {"Info": "In live"}


# Admin Apis
@app.post("/rms/admin/login")
async def admin_login(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.admin_login(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in admin_login: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/meal_type")
async def meal_type():
    try:
        response = route.meal_type()
        return response
    except Exception as e:
        print("Exception in meal_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/filters/add_meal_type")
async def add_meal_type(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.add_meal_type(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in add_meal_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/dish_type")
async def dish_type():
    try:
        response = route.dish_type()
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/filters/add_dish_type")
async def add_dish_type(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.add_dish_type(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in add_dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/printer")
async def printer():
    try:
        response = route.printer()
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/reference")
async def reference():
    try:
        response = route.reference()
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/percentage")
async def percentage():
    try:
        response = route.percentage()
        return response
    except Exception as e:
        print("Exception in dish_type: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/filters/hall")
async def hall():
    try:
        response = route.hall()
        return response
    except Exception as e:
        print("Exception in hall: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dish/dish_items")
async def dish_items(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.dish_items(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dish/dish_items_user")
async def dish_items_user(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.dish_items_user(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_items_user: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/manage")
async def dish_manage(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.dish_manage(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_manage: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/delete")
async def dish_delete(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.dish_delete(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_delete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/status")
async def dish_status(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.dish_status(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_status: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/dish/qty_update")
async def qty_update(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.qty_update(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in qty_update: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/users/user_list")
async def user_list():
    try:
        response = route.user_list()
        return response
    except Exception as e:
        print("Exception in dish_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/users/prv_lst")
async def prv_lst():
    try:
        response = route.prv_lst()
        return response
    except Exception as e:
        print("Exception in dish_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/users/manage")
async def user_manage(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.user_manage(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in user_manage: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/users/delete")
async def user_delete(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.user_delete(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in user_delete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/users/status")
async def user_status(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.user_status(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in user_status: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/order_types")
async def order_types():
    try:
        response = route.order_types()
        return response
    except Exception as e:
        print("Exception in order_types: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/order_stat")
async def order_stat():
    try:
        response = route.order_stat()
        return response
    except Exception as e:
        print("Exception in order_status: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/take_order")
async def take_order(request: Request, decoded=Depends(auth_scheme)):
    try:
        data = await request.json()
        if data is not None:
            response = route.take_order(data, decoded)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in take_order: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/add_order_items")
async def add_order_items(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.add_order_items(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in add_order_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/running_orders")
async def running_orders():
    try:
        response = route.running_orders()
        return response
    except Exception as e:
        print("Exception in running_orders: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dash/dash_nav")
async def dash_nav():
    try:
        response = route.dash_nav()
        return response
    except Exception as e:
        print("Exception in running_orders: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/running_orderitems")
async def running_orderitems(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.running_orderitems(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in running_orderitems: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/order_complete")
async def order_status(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.order_complete(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in order_complete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/remove_items")
async def remove_items(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.remove_items(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in remove_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/orders/cancel_order")
async def cancel_order(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.cancel_order(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in cancel_order: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/orders/reprint_bill")
async def reprint_bill(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.reprint_bill(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in reprint_bill: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/report/order_report")
async def order_report(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.order_report(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in order_report: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/report/order_report_items")
async def order_report_items(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.order_report_items(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in order_report_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/report/dish_report")
async def dish_report(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.dish_report(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in dish_report: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/counters/counter_details")
async def counter_details(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.counter_details(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in counter_details: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/counters/hall_details")
async def hall_details():
    try:
        response = route.hall_details()
        return response
    except Exception as e:
        print("Exception in counter_details: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/counter/counter_manage")
async def counter_manage(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.counter_manage(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in counter_manage: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/counter/counter_delete")
async def counter_delete(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.counter_delete(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in counter_delete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/counter/counter_delete")
async def counter_delete(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.counter_delete(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in counter_delete: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/purchase/suppliers")
async def suppliers():
    try:
        response = route.suppliers()
        return response
    except Exception as e:
        print("Exception in suppliers: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/purchase/manage_suppliers")
async def manage_suppliers(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.manage_suppliers(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in manage_suppliers: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/purchase/items")
async def items():
    try:
        response = route.items()
        return response
    except Exception as e:
        print("Exception in items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/purchase/manage_items")
async def manage_items(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.manage_items(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in manage_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/purchase/category")
async def category():
    try:
        response = route.category()
        return response
    except Exception as e:
        print("Exception in items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/purchase/manage_category")
async def manage_category(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.manage_category(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in manage_category: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/purchase/list")
async def purchase_list():
    try:
        response = route.purchase_list()
        return response
    except Exception as e:
        print("Exception in purchase_list: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.post("/rms/purchase/add")
async def add_purchase(request: Request):
    try:
        data = await request.json()
        if data is not None:
            response = route.add_purchase(data)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in manage_category: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dashboard/get_sales_stats")
async def get_sales_stats(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.sales(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in get_sales_stats: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dashboard/sales_by_category")
async def sales_by_category(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.sales_by_category(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in sales_by_category: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")


@app.get("/rms/dashboard/sales_by_items")
async def sales_by_items(data=None):
    try:
        if data is not None:
            request = json.loads(data)
            response = route.sales_by_items(request)
            return response
        else:
            raise HTTPException(status_code=400, detail="Invalid Request!")
    except Exception as e:
        print("Exception in sales_by_items: " + str(e))
        raise HTTPException(status_code=400, detail="Invalid Request!")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
