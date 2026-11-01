import streamlit as st

st.set_page_config(page_title="Өгөгдлийн шинжилгээний сургалт", page_icon="📊", layout="wide")

pages = {
    "Эхлэл": [st.Page("views/home.py", title="Нүүр", icon="🏠", default=True)],
    "Хичээлүүд": [
        st.Page("views/pandas_basics.py", title="1. Pandas үндэс", icon="🐼"),
        st.Page("views/cleaning.py", title="2. Өгөгдөл цэвэрлэх", icon="🧹"),
        st.Page("views/viz.py", title="3. Дүрслэл", icon="📈"),
        st.Page("views/stats.py", title="4. Статистик", icon="🎲"),
        st.Page("views/ml.py", title="5. Машин сургалт", icon="🤖"),
    ],
    "Шалгалт": [st.Page("views/quiz.py", title="Мэдлэг шалгах", icon="📝")],
}
st.navigation(pages).run()
