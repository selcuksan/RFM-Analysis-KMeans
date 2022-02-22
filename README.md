# K-Means Kümeleme Algoritması nedir

* Yakından ilişkili veri noktası gruplarını keşfeden denetimsiz bir makine öğrenimi algoritmasıdır. Algoritma istatistiksel olarak benzer nitelikteki kayıtları aynı gruba sokar. Bir elemanın yalnızca bir kümeye ait olmasına izin verir. 

* K adet özgün küme oluşturduğu ve her kümenin merkezi, kümedeki değerlerin ortalaması olduğu için K-Ortalamalar(K-Means) denmektedir.

## Algoritma tarafından sırasıyla şu adımlar gerçekleştirilir:
  → Küme merkezlerinin belirlenmesi
  
  → Merkez dışındaki örneklerin mesafelerine göre sınıflandırılması
  
  → Yapılan sınıflandırmaya göre yeni merkezlerin belirlenmesi
  
  → Kararlı hale gelinene kadar 2. ve 3. aşamanın tekrarlanması
  
    
    * K-Meansdaki ‘K’ parametresi verinin kaç tane kümeye ayrılacağını belirtir. 
      Uygun K sayısını seçmek için çeşitli metotlar bulunmaktadır.

       - Elbow metodu (Dirsek Yöntemi); noktaların her K değerine göre küme merkezine uzaklıklarının karesi toplamı hesaplanmaktadır. 
          Bu değerlere göre her K değeri için grafik çizilmektedir. 
          Grafik üzerinde toplamlar arasındaki farkın azalmaya başladığı dirsek noktası en uygun K değeri olarak belirlenmektedir.
     
     
# Gereksinimler

* Yerel makinenizde python ve Git kurulmuş olmalıdır.

# Kurulum & Çalıştırma

- <pre class="terminal"><code class="terminal-line" prefix="$">git clone https://github.com/selcuksan/RFM-Analizi-KMeans.git</code></pre>
- <pre class="terminal"><code class="terminal-line" prefix="$">cd RFM-Analizi-KMeans</code></pre>
- <pre class="terminal"><code class="terminal-line" prefix="$">pip install -r requirements.txt</code></pre>
- <pre class="terminal"><code class="terminal-line" prefix="$">py rfm-analysis-Kmeans.py</code></pre>
