from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.product import Product, sample_products

product_router = APIRouter(tags=["Product"], prefix='/product',
                           default_response_class=JSONResponse)


@product_router.get('/product/{product_id}', response_class=JSONResponse)
async def root(product_id: int):
    output = {"message": "Not found", "data": None}

    for item in sample_products:
        if item["product_id"] == product_id:
            output = {"message": "Found", "data": item}

    return output


@product_router.get('/products/search', response_class=JSONResponse)
async def root(keyword: str, category: str | None = None, limit: int | None = 10):
    output = {"message": "Not found", "data": None}
    data = []

    for item in sample_products:
        if limit < 0:
            break

        if keyword.lower() in item["name"].lower():
            if category is not None:
                if category == item["category"]:
                    data.append(item)
            else:
                data.append(item)

            limit -= 1

    if len(data) > 0:
        output = {"message": "Found", "data": data}

    return output
