# Kütüphaneleri yüklüyoruz
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from yellowbrick.cluster import KElbowVisualizer

# Veriyi içe aktarıyoruz
df = pd.read_excel("online_retail_II.xlsx")

# Eksik verilere sahip gözlem birimlerinin df üzerinden kaldırılması
df.dropna(inplace=True)

# Quantity ve Price değerleri için, 0'dan büyük değerlerin alınması
df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

# Data setine "Total Price" değişkeninin eklenmesi
df['Total_Price'] = df['Price'] * df['Quantity']

# RFM metriklerinin hesaplanması
df['InvoiceDate'].max()  # En eski alışveriş tarihi

today_date = dt.datetime(2011, 12, 11)

rfm = df.groupby('Customer ID').agg(
    {'InvoiceDate': lambda InvoiceDate: (today_date - InvoiceDate.max()).days,  # Recency değeri
     'Invoice': lambda Invoice: Invoice.nunique(),  # Frequency değeri
     'Total_Price': lambda Total_Price: Total_Price.sum()})  # Monetary değeri

# RFM metrikleri kolonlarının yeniden adlandırılması
rfm.columns = ['recency', 'frequency', 'monetary']

rfm = rfm[rfm["monetary"] > 0]

# Veri üzerinde standardizasyon işlemi gerçekleştirilmesi
scaler = StandardScaler()
rfm_scaled_data = scaler.fit_transform(rfm)
rfm_scaled_df = pd.DataFrame(rfm_scaled_data, columns=[
    'recency', 'frequency', 'monetary'])

# Elbow yöntemiyle optimum küme sayısının belirlenmesi
kmeans = KMeans()
elbow = KElbowVisualizer(kmeans, k=(2, 20))
elbow.fit(rfm_scaled_data)

# elbow.show()
print(elbow.elbow_value_)

# rfm veri kümesi için final clusterların oluşturulması
kmeans_model = KMeans(elbow.elbow_value_).fit(rfm_scaled_data)
clusters = kmeans_model.labels_

rfm["cluster_no"] = clusters + 1
rfm_scaled_df["cluster_no"] = clusters + 1

fig = plt.figure(figsize=(8, 8))
sns.boxplot(x="cluster_no", y="monetary", data=rfm_scaled_df)

sns.scatterplot("frequency", "monetary", hue="cluster_no", data=rfm_scaled_df)

sns.pairplot(rfm_scaled_df, hue='cluster_no')

# Segmentlere ayrılmış müşterilerin 3B temsili
ax = fig.add_subplot(111, projection='3d')
x = rfm_scaled_df['frequency']
y = rfm_scaled_df['monetary']
z = rfm_scaled_df['recency']
ax.set_xlabel("frequency")
ax.set_ylabel("monetary")
ax.set_zlabel("recency")
ax.scatter(x, y, z)

plt.show()
