# 📊 Өгөгдлийн шинжилгээний сургалт (Streamlit)

Python, Pandas, Plotly, SciPy, scikit-learn ашигласан интерактив сургалтын вэб апп.

## Агуулга
Pandas үндэс · Өгөгдөл цэвэрлэх · Дүрслэл · Статистик · Машин сургалт · Шалгалт

## Локалд ажиллуулах
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## GitHub → Streamlit Community Cloud
1. GitHub дээр шинэ repository үүсгээд энэ хавтасны бүх файлыг push хийнэ:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<нэр>/<repo>.git
   git push -u origin main
   ```
2. https://share.streamlit.io руу GitHub-аараа нэвтэрнэ.
3. **Create app** → repository, branch `main`, Main file path: `app.py` → **Deploy**.

## Бүтэц
```
app.py            # Навигаци
utils.py          # Жишиг өгөгдөл
views/            # Хичээл бүрийн хуудас
.streamlit/config.toml
requirements.txt
```
