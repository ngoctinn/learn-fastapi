Simple Postgres FastAPI sample

Hướng dẫn nhanh:

1. Cài phụ thuộc (từ thư mục `simple_postgres_app`):

```
python -m pip install -r requirements.txt
```

2. Sửa chuỗi kết nối PostgreSQL trong `database.py` (biến `DATABASE_URL`).
   Ví dụ: `postgresql://postgres:password@localhost:5432/fastapi_db`

3. Chạy server:

```
uvicorn simple_postgres_app.main:app --reload
```

4. API endpoints:

- POST /books/ (tạo sách) body JSON: {"title":"...","author":"...","pages":123}
- GET /books/ (danh sách sách)
- GET /books/{id} (lấy sách theo id)

Ghi chú: Tập này dùng SQLAlchemy synchronous + psycopg2. Để dùng async (asyncpg) cần thay engine/driver.
