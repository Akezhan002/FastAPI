from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router  = APIRouter(
    prefix="/web",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/base")
def get_base_template(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@router.get("/products")
def get_products_template(request: Request):
    return templates.TemplateResponse("product.html", {"request": request})

@router.get("/clients")
def get_clients_template(request: Request):
    return templates.TemplateResponse("client.html", {"request": request})

@router.get("/orders")
def get_orders_template(request: Request):
    return templates.TemplateResponse("order.html", {"request": request})


