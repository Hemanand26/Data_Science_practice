# import numpy as np
#
# # Sample data
# data = np.array([
#     [30, 50000],  # Customer 1
#     [40, 70000],  # Customer 2
#     # Add more customers...
# ])
#
# # New customer
# new_customer = np.array([35, 60000])
#
# # Calculate distances to centroids
# distances_to_centroids = np.linalg.norm(data - new_customer, axis=1)
#
# # Find index of closest centroid
# closest_cluster_index = np.argmin(distances_to_centroids)
#
# # Assign new customer to closest cluster
# print("New customer assigned to Cluster:", closest_cluster_index + 1)

#----------------------------------------------------------------------------

# import numpy as np
# from sklearn.cluster import KMeans
#
# # Sample data: [age, income]
# data = np.array([
#
#     [30, 60000],
#     [35, 70000],
#     [40, 80000],
#     [45, 90000],
#     [50, 100000],
#     [55, 110000],
#     [25, 50000],
#     [60, 120000],[90,190000]
# ])
#
# # New customer data: [age, income]
# new_customer = np.array([92, 198000])
#
# # Create a KMeans instance with 3 clusters
# kmeans = KMeans(n_clusters=3, random_state=0)
#
# # Fit the KMeans model to the data
# kmeans.fit(data)
#
# # Print the centroids of the clusters
# print("Cluster Centers:")
# print(kmeans.cluster_centers_)
#
# # Predict the clusters for the existing data points
# labels = kmeans.predict(data)
# print("Cluster Labels for Existing Data Points:")
# print(labels)

# Predict the cluster for the new customer
# new_customer_cluster = kmeans.predict([new_customer])
#
# print("New Customer assigned to Cluster:")
# print(new_customer_cluster[0])

#-------------------------------------------

import numpy as np
from sklearn.cluster import KMeans

# Sample data: [age, income]
data = np.array([
    [25, 50000],
    [30, 60000],
    [35, 70000],
    [40, 80000],
    [45, 90000],
    [50, 100000],
    [55, 110000],
    [60, 120000]
])

# New customer data: [age, income]
new_customer = np.array([33, 65000])

# Create a KMeans instance with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)

# Fit the KMeans model to the data
kmeans.fit(data)

# Print the centroids of the clusters
print("Cluster Centers:")
print(kmeans.cluster_centers_)

# Predict the clusters for the existing data points
labels = kmeans.predict(data)
print("Cluster Labels for Existing Data Points:")
print(labels)

# Predict the cluster for the new customer
new_customer_cluster = kmeans.predict([new_customer])[0]

# Mapping of cluster labels to names
cluster_names = {
    0: "Young Low-Income Group",
    1: "Middle-Aged Medium-Income Group",
    2: "Senior High-Income Group"
}

# Get the name of the cluster for the new customer
new_customer_cluster_name = cluster_names[new_customer_cluster]

print("New Customer assigned to Cluster:")
print(new_customer_cluster_name)
