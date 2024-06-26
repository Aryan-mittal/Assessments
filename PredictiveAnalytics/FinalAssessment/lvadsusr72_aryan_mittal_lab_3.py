# -*- coding: utf-8 -*-
"""LVADSUSR72_ARYAN_MITTAL_LAB-3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19L8G_HEPuxxvubEPZQ0DnVR_Xxs-wcVA
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/content/seeds.csv")

df.head()

df.info()

df.describe()

df.isnull().sum()       #detecting the null values

df.fillna(df.median(), inplace = True)

df.isnull().sum()

# Visualize distributions of numerical features
plt.figure(figsize=(16, 10))
for i, column in enumerate(df.columns, 1):
    plt.subplot(3, 3, i)
    sns.histplot(df[column], kde=True)
    plt.title(column)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))  #detecting the outlieirs
sns.boxplot(data=df)
plt.title("Boxplot of Numerical Features ")
plt.xticks(rotation=45)
plt.show()

#as we can see , there are no significant outliers

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# Standardizing the features
X = df.copy()
scaler = StandardScaler()
features_scaled = scaler.fit_transform(X)

# Applying the Elbow Method to find the optimal number of clusters
inertia = []
range_values = range(1, 11)

for i in range_values:
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)

# Plotting the Elbow Method graph
plt.figure(figsize=(10, 6))
plt.plot(range_values, inertia, marker='o', linestyle='--')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.show()

from sklearn.metrics import silhouette_score
silhouette_scores = []
range_values = range(2, 10)
for i in range_values:
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(features_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(features_scaled, kmeans.labels_))

plt.plot(range_values, silhouette_scores, marker='o')
plt.title('Silhouette Scores')
plt.xlabel('Number of clusters')
plt.ylabel('Silhouette Score')
plt.tight_layout()
plt.show()

optimal_clusters = 3
kmeans_final = KMeans(n_clusters=optimal_clusters, random_state=42)
kmeans_final.fit(features_scaled)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(features_scaled)
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=kmeans_final.labels_, palette='viridis', s=100, alpha=0.6)
plt.title('Cluster Visualization with PCA')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Cluster')
plt.show()

