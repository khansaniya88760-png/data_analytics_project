import pandas as pd, numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, seaborn as sns
sns.set_theme(style='whitegrid', context='notebook')
OUT='charts/'
import os; os.makedirs('charts',exist_ok=True)
df=pd.read_csv('shopping_data.csv')
df=df.drop_duplicates()
df['City']=df.City.str.strip().str.title()
df.loc[(df.Discount_Percent<0)|(df.Discount_Percent>100),'Discount_Percent']=np.nan
df['Order_Date']=pd.to_datetime(df.Order_Date)
df['Product_Category']=df.Product_Category.str.replace('_',' & ')
df['Payment_Mode']=df.Payment_Mode.str.replace('_',' ')
pal='viridis'
def save(n):
    plt.tight_layout(); plt.savefig(OUT+n,dpi=150); plt.close()

# 1 revenue by category
d=df.groupby('Product_Category').Order_Value_INR.sum().sort_values(ascending=False)
plt.figure(figsize=(8,5)); ax=sns.barplot(x=d.index,y=d.values,hue=d.index,palette=pal,legend=False)
for c in ax.containers: ax.bar_label(c,fmt='₹%.0f',padding=3,fontsize=9)
plt.title('Total Revenue by Product Category'); plt.ylabel('Revenue (INR)'); plt.xlabel(''); plt.xticks(rotation=15); save('1_revenue_by_category.png')

# 2 orders by city
d=df.City.value_counts()
plt.figure(figsize=(8,5)); ax=sns.barplot(x=d.values,y=d.index,hue=d.index,palette='crest',legend=False,orient='h')
for c in ax.containers: ax.bar_label(c,padding=3)
plt.title('Number of Orders by City'); plt.xlabel('Orders'); plt.ylabel(''); save('2_orders_by_city.png')

# 3 payment mode pie
d=df.Payment_Mode.value_counts()
plt.figure(figsize=(7,7)); plt.pie(d.values,labels=d.index,autopct='%1.1f%%',startangle=90,colors=sns.color_palette('Set2'),wedgeprops=dict(edgecolor='white'))
plt.title('Payment Mode Share'); save('3_payment_mode_share.png')

# 4 customer type
d=df.Customer_Type.value_counts()
plt.figure(figsize=(7,5)); ax=sns.barplot(x=d.index,y=d.values,hue=d.index,palette='Set2',legend=False)
for c in ax.containers: ax.bar_label(c,padding=3)
plt.title('Orders by Customer Type (missing values excluded)'); plt.ylabel('Orders'); plt.xlabel(''); save('4_customer_type.png')

# 5 monthly trend
m=df.set_index('Order_Date').Order_Value_INR.resample('MS').sum()
plt.figure(figsize=(11,5)); plt.plot(m.index,m.values,marker='o',color='#2a9d8f')
plt.title('Monthly Revenue Trend'); plt.ylabel('Revenue (INR)'); plt.xlabel('Month'); plt.xticks(rotation=30); save('5_monthly_revenue_trend.png')

# 6 order value distribution
plt.figure(figsize=(8,5)); sns.histplot(df.Order_Value_INR.dropna(),bins=30,kde=True,color='#e76f51')
plt.title('Distribution of Order Value'); plt.xlabel('Order Value (INR)'); save('6_order_value_distribution.png')

# 7 rating by category boxplot
plt.figure(figsize=(9,5)); sns.boxplot(data=df,x='Product_Category',y='Customer_Rating',hue='Product_Category',palette='pastel',legend=False)
plt.title('Customer Rating by Product Category'); plt.xlabel(''); plt.xticks(rotation=15); save('7_rating_by_category.png')

# 8 discount vs order value
plt.figure(figsize=(8,5)); sns.scatterplot(data=df,x='Discount_Percent',y='Order_Value_INR',hue='Product_Category',alpha=.75)
plt.title('Discount % vs Order Value'); plt.xlabel('Discount (%)'); plt.ylabel('Order Value (INR)'); save('8_discount_vs_order_value.png')

# 9 delivery days vs rating
d=df.groupby('Delivery_Days').Customer_Rating.mean()
plt.figure(figsize=(8,5)); ax=sns.barplot(x=d.index.astype(int),y=d.values,hue=d.index,palette='rocket_r',legend=False)
plt.title('Average Rating by Delivery Days'); plt.xlabel('Delivery Days'); plt.ylabel('Avg Rating'); plt.ylim(0,5); save('9_delivery_days_vs_rating.png')

# 10 heatmap
plt.figure(figsize=(8,6)); sns.heatmap(df.select_dtypes('number').corr(),annot=True,fmt='.2f',cmap='coolwarm',center=0)
plt.title('Correlation Heatmap'); save('10_correlation_heatmap.png')
