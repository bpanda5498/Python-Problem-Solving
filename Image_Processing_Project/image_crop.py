import cv2
import numpy as np
from skimage.segmentation import active_contour
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def preprocess_image(image):
    """
    Preprocesses an MRI image for segmentation.
    Args:
        image: A NumPy array representing the MRI image.
    Returns:
        A preprocessed NumPy array.
    """
    # Preprocessing for active contour (original format)
    image = cv2.resize(image, (256, 256))  # Example resize with OpenCV
    return image
def segment_with_active_contour(image, seed_point_variation=0):
    """
    Segments the substantia nigra region using K-means, thresholding, morphology, and active contours.
    Args:
        image: A preprocessed MRI image in original format.
        seed_point_variation: (Optional) Integer value to introduce random variation in seed points for active contours.
    Returns:
        A tuple containing NumPy arrays representing the segmented substantia nigra regions (left and right).
    """
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # K-means clustering for initial segmentation
    kmeans = KMeans(n_clusters=2, random_state=0)
    reshaped_image = gray_image.reshape((-1, 1))
    kmeans.fit(reshaped_image)
    clustered_image = kmeans.labels_.reshape(gray_image.shape)
    # Select the cluster corresponding to the substantia nigra
    substantia_nigra_cluster = 1 if np.sum(clustered_image == 1) > np.sum(clustered_image == 0) else 0
    substantia_nigra_mask = np.uint8(clustered_image == substantia_nigra_cluster) * 255
    # Thresholding segmentation
    _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Combine K-means and thresholding segmentation
    combined_segmentation = cv2.bitwise_or(substantia_nigra_mask, thresholded_image)
    # Morphological operations to enhance the segmentation
    kernel = np.ones((5, 5), np.uint8)
    morphed_image = cv2.morphologyEx(combined_segmentation, cv2.MORPH_CLOSE, kernel)
    # Active contour (Snakes) segmentation for left side
    left_x_center = 140 + seed_point_variation 
    left_y_center = 150
    left_r = 50
    left_snake_init = np.array([[left_x_center + left_r * np.cos(t), left_y_center + left_r * np.sin(t)] for t in np.linspace(0, 2 * np.pi, 100)])
    left_snake = active_contour(morphed_image, left_snake_init, alpha=0.015, beta=10, gamma=0.001)
    # Active contour (Snakes) segmentation for right side
    right_x_center = 140 + seed_point_variation
    right_y_center = 160
    right_r = 50
    right_snake_init = np.array([[right_x_center + right_r * np.cos(t), right_y_center + right_r * np.sin(t)] for t in np.linspace(0, 2 * np.pi, 100)])
    right_snake = active_contour(morphed_image, right_snake_init, alpha=0.015, beta=10, gamma=0.001)
    return left_snake, right_snake
# Load your MRI image using OpenCV
image = cv2.imread("MEDIAN FILTERED IMAGE.png")  # Replace format if needed
# Preprocess the image for active contour segmentation
preprocessed_image = preprocess_image(image)
# Perform segmentation using active contour with seed point variation (optional)
seed_point_variation = 10
left_snake, right_snake = segment_with_active_contour(preprocessed_image, seed_point_variation)
# Create separate images for left and right substantia nigra regions
left_segmented_image = np.zeros_like(preprocessed_image)
right_segmented_image = np.zeros_like(preprocessed_image)
cv2.drawContours(left_segmented_image, [left_snake.astype(int)], -1, 255, thickness=-1)
cv2.drawContours(right_segmented_image, [right_snake.astype(int)], -1, 255, thickness=-1)
# Visualize the original and segmented images
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(left_segmented_image, cmap='gray')
plt.title('Segmented Left Substantia Nigra')
plt.subplot(1, 3, 3)
plt.imshow(right_segmented_image, cmap='gray')
plt.title('Segmented Right Substantia Nigra')
plt.show()