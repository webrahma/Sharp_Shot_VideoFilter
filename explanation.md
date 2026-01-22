# Sharp-Shot Video Filter: Technical Explanation

## 1. Sharpness Calculation: The Variance of the Laplacian Method

The core of the "Sharp-Shot" filter is the quantitative assessment of image sharpness, which is achieved using the **Variance of the Laplacian** method. This technique is widely recognized in computer vision for its effectiveness in blur detection [1].

### Mathematical Principle

The Laplacian is a second-order differential operator that measures the rate of change of the first-order derivatives. In image processing, it is used to highlight regions of rapid intensity change, which correspond to **edges** and **fine details**.

The continuous 2D Laplacian operator $L(x, y)$ for an image $I$ is defined as:
$$L(x, y) = \frac{\partial^2 I}{\partial x^2} + \frac{\partial^2 I}{\partial y^2}$$

In a digital image, this operation is approximated by convolvi

### The Role of Variance

After applying the Laplacian filter, a sharp image will produce a resulting image with high-magnitude pixel values (both positive and negative) at the edges. Conversely, a blurred image, which lacks sharp edges, will produce a resulting image with pixel values close to zero.

The **variance** of the Laplacian-filtered image is then calculated. This statistical measure quantifies the spread of the pixel values.

| Image State | Laplacian Output | Variance Value | Interpretation |
| :--- | :--- | :--- | :--- |
| **Sharp** | High-magnitude values (strong edges) | **High** | High-frequency details are present. |
| **Blurred** | Low-magnitude values (weak or no edges) | **Low** | High-frequency details have been attenuated. |

Therefore, a higher Laplacian Variance score directly correlates with a sharper image.

## 2. Ensuring Temporal Diversity: The Temporal Constraint Algorithm

The challenge requires selecting the top 5 sharpest frames while ensuring they are not clustered together in time. Simply selecting the top 5 frames by sharpness score often results in a "burst" of frames from a single, momentarily sharp segment of the video.

To solve this, a **Temporal Constraint Algorithm** is implemented:

1.  **Full Video Analysis:** The script first analyzes every frame in the video, calculating and storing its sharpness score and timestamp.
2.  **Sharpness Ranking:** All frames are sorted in descending order based on their sharpness score.
3.  **Greedy Selection with Minimum Interval:**
    *   The sharpest frame overall is selected first.
    *   Subsequent frames are considered in order of their sharpness rank.
    *   A candidate frame is only added to the final selection if its timestamp is separated from **all** previously selected frames by a minimum time interval (default: 1.0 second). This minimum interval acts as a temporal buffer, forcing the selection to span different moments in the video.

This approach guarantees that the final five frames are the sharpest available while maintaining a minimum temporal separation, thus providing a diverse and representative set of "sharp shots" from the entire video stream.

***

### References

[1] Pertuz, S., Puig, D., & Garcia, M. A. (2013). Analysis of focus measure operators for shape-from-focus. *Pattern Recognition*, 46(5), 1415-1432. [https://doi.org/10.1016/j.patcog.2012.11.011](https://doi.org/10.1016/j.patcog.2012.11.011)
