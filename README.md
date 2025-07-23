
# 🛒 AI Agent for E-commerce Data Q&A

This project is an AI-powered assistant that answers natural language questions using structured e-commerce data.

Built using **FastAPI**, **Google Gemini API**, and **MySQL**, the system allows you to ask questions like:
- 📊 _"What is my total sales?"_
- 💸 _"Calculate the RoAS (Return on Ad Spend)"_
- 📈 _"Which product had the highest CPC?"_

---

## 🚀 Features

✅ Converts plain English to SQL using Gemini API  
✅ Queries your real-time sales data from MySQL  
✅ Returns clean, human-readable answers  
✅ Bonus: Add visualizations with Matplotlib or Plotly  
✅ Deployed as an interactive API with FastAPI

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ecommerce-ai-agent.git
cd ecommerce-ai-agent
pip install -r requirements.txt
```

### 🛠️ Database Setup

1. Create a MySQL database named `ecommerce`
2. Load CSVs into tables (`eligibility`, `ad_sales`, `total_sales`) using the provided script:
```bash
python app/load_mysql_data.py
```

---

## ⚙️ Running the API

```bash
uvicorn main:app --reload
```

Visit the docs here: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📸 Demo Output

![API Output Demo](api_output_demo.png)

---

## 🧪 Example Questions

| Question                    | SQL Translation                                | Sample Output    |
|----------------------------|------------------------------------------------|------------------|
| What is my total sales?    | `SELECT SUM(total_sales) FROM total_sales;`    | 92500            |
| RoAS?                      | `SELECT SUM(revenue)/SUM(ad_spend)...`         | 2.73             |
| Highest CPC product?       | `SELECT product_id, MAX(cpc)...`               | `P678 - $3.50`   |

---

## 🔐 License

Licensed under the **MIT License**.

---

## 👨‍💻 Author

Built by [Tanishq Kolhatkar](https://www.linkedin.com/in/tanishq93/)  
Email: tanishq.kolhatkar@example.com
