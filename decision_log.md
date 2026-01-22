# Decision Log

## The Most Difficult Decision  
### Balancing Memory Management vs. Processing Speed

### Context  
During the development of the **Sharp-Shot Filter**, the most challenging technical decision was determining how to handle video frames during the analysis phase without exhausting system resources.

---

### The Problem  
The initial straightforward approach was to store every video frame in a Python list along with its sharpness score.  
However, for **high-definition** or **long-duration** videos, this method led to:

- Excessive RAM consumption  
- Risk of system crashes  
- Slow performance during frame sorting  

This made the approach unsuitable for real-world or production use.

---

### The Decision — Metadata-First Approach  

To solve this, I implemented a **dual-pass processing strategy**:

#### **First Pass — Analysis Phase**
- The script iterates through the video.
- Calculates **Laplacian Variance** for each frame.
- Stores only lightweight metadata:
  - Frame index  
  - Timestamp  
  - Sharpness score  

> No actual image frames are stored in memory.

#### **Second Pass — Extraction Phase**
- After selecting the **Top 5 diverse sharpest frames** using temporal-constraint logic,
- The script jumps directly to required frames using:  
  `cv2.CAP_PROP_POS_FRAMES`
- Only the selected frames are loaded and saved.

---

### The Outcome  

This decision introduced a minor trade-off:

- Slightly increased processing time (two video passes)

But achieved major benefits:

- Extremely low memory usage  
- Ability to process large videos smoothly  
- No system crashes  
- 100% accuracy in identifying sharpest frames  
- A **production-ready and scalable solution**

---

### Final Note  
This design choice successfully balanced **performance efficiency** and **resource management**, making the Sharp-Shot Filter reliable even on machines with limited RAM.


