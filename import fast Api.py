from fastapi import FastAPI
from pydantic import BaseModel

# 1. Определение модели данных (схемы) с помощью Pydantic
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

app = FastAPI()

# --- Маршруты (Endpoints) ---

# 2. Базовый маршрут (root)
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 3. Маршрут с параметром пути (item_id) и параметром запроса (q)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# 4. Маршрут для сохранения/обновления (PUT)
# Принимает item_id (параметр пути) и объект Item (тело запроса)
@app.put("/items/{item_id}")
def save_item(item_id: int, item: Item):
    # FastAPI автоматически преобразует JSON-тело запроса в объект Item
    return {"item_id": item_id, "item_name": item.name, "item_price": item.price}