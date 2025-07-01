Absolutely, Harshini! Here's your **final `README.md`**, fully customized with all your app features, Excel output, Streamlit screenshots, and interview-ready language tailored for **ServiceTitan-type roles**.

---

## ✅ Final `README.md` (Copy-Paste Ready)

```markdown
# 🔧 Home Services Pricebook Optimizer

An AI-powered pricing assistant for HVAC, Plumbing, and Electrical service providers — designed to match real-world workflows like those used in ServiceTitan.

> 📈 Optimize profit margins, 🤖 use AI for pricing/classification, 📊 visualize trends, and 📥 export Excel pricebooks with formulas — all from a friendly Streamlit app.

---

## 📸 Demo Screenshots

| Margin Analysis | Regression Trend | Suggested Pricing | Excel Output |
|-----------------|------------------|-------------------|--------------|
| ![margin](screenshots/margin_boxplot.png) | ![trend](screenshots/trend_line.png) | ![optimized](screenshots/suggested_prices.png) | ![excel](screenshots/excel_output.png) |

---

## 🚀 Features

✅ Upload your own pricebook CSV  
✅ Auto-calculate total cost and profit margins  
✅ AI-powered price prediction and service categorization  
✅ Margin optimization via interactive slider  
✅ Profit margin boxplot by category  
✅ Linear regression to visualize cost-price trends  
✅ Export to:
- 📄 CSV (optimized pricebook)
- 📊 Excel (formulas for Total Cost & Margin %)

✅ Built-in session logger to track predictions  
✅ Streamlit-based interactive UI

---

## 🧠 Tech Stack

| Tool            | Use Case                               |
|-----------------|----------------------------------------|
| Python          | Core logic and modeling                |
| Pandas          | Data handling and transformation       |
| Scikit-learn    | Regression + Classification models     |
| Streamlit       | Web UI                                 |
| Matplotlib      | Visualizations                         |
| openpyxl        | Excel file generation with formulas    |

---

## 📁 Folder Structure

```

Home\_Services\_Pricebook\_Optimizer/
├── app.py
├── ai\_models.py
├── train\_models.py
├── price\_optimizer.py
├── excel\_exporter.py
├── create\_sample\_data.py
├── requirements.txt
├── data/
│   └── home\_services\_realistic.csv
├── models/
│   ├── price\_predictor.pkl
│   ├── category\_classifier.pkl
│   └── category\_label\_encoder.pkl
├── session\_log.txt
└── screenshots/
├── margin\_boxplot.png
├── trend\_line.png
├── suggested\_prices.png
└── excel\_output.png

````

---

## 📥 Try It Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Home_Services_Pricebook_Optimizer.git
cd Home_Services_Pricebook_Optimizer
````

### 2. Create a virtual environment and activate

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train AI models (one-time)

```bash
python train_models.py
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 📊 Dataset Format

Your CSV should include the following columns:

```csv
Service,Category,Labor Cost,Material Cost,Price
```

Example:

```csv
Furnace Repair,HVAC,120,60,250
Leak Detection,Plumbing,90,30,180
Light Fixture Installation,Electrical,65,35,130
```

🧠 The app will compute:

* `Total Cost = Labor + Material`
* `Profit Margin (%) = (Price - Total Cost)/Price`

---

## 📤 Output Formats

* ✅ `optimized_pricebook.csv`: clean CSV with updated prices
* ✅ `optimized_pricebook_with_formulas.xlsx`: Excel with formulas like:

  * `Total Cost = C2 + D2`
  * `Profit Margin (%) = (E2 - F2)/E2`

---

## 💼 Use Cases

* ServiceTitan consultants optimizing pricebooks
* SMBs creating dynamic pricing strategies
* Field service owners testing AI-assisted markup tools
* Business analysts aligning real cost-to-price logic

---

## 👩‍💻 Author

**Harshini Akunuri**
*Data Scientist | AI Developer | ServiceOps Optimizer*
📫 [LinkedIn →](https://www.linkedin.com/in/harshini-akunuri/)
🌐 [GitHub →](https://github.com/ha723-web)

---

## 📄 License

Licensed under the [MIT License](LICENSE).

```

---

