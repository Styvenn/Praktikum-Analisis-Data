import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('nilai_siswa.csv')

data.head()
data.info()
data.describe()

print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])

matematika = data[data['Matpel'] == 'Matematika']
print(matematika)

Inggris = data[data['Matpel'] == 'Bahasa Inggris']
print(Inggris)

Fisika = data[data['Matpel'] == 'Fisika']
print(Fisika)

Produktif = data[data['Matpel'] == 'Produktif']
print(Produktif)

data.groupby('Matpel')['Nilai'].agg(['max','min'])

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Nilai Rata-Rata')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show()