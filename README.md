# Face and eye detection using Python and OpenCV

Real time face and eye detection using your computer's webcam.

# **Pre-requisites :**
1. Python 3.7
2. OpenCV v3.4.1
3. numpy

# **Some details**
**Why do we use Cascade Classifiers?**

Cascade classifiers help us to reduce the computation time as well as to save computation power.
Cascade refers to a series of waterfalls. Similarly, in Computer Science, they are used to solve image recognition problems.
For example, a very strong classifier that can detect faces is broken down into several hundred or thousand weak classifiers.
Each classifier can recognize a sub-region of an image and verify whether they are the target object or not, which in this case, is the face.
If at any point, any classifier in the chain feels that it is not the target object, then it immeditaely rejects the region.
In this way, regions which does not contain any target object can be effecctively rejected and resources and time can be saved.

**Why do we use Multi-scaling?**

Multi-scaling means that the algorithm looks at different sub-regions of the image from various scales.
Multi-scaling is necessary so that the algorithm can successfully detect faces of all sizes.

**Why do we set the value to 0 in video capture??**

The value '0' refers to the primary camera in your laptop/computer. Since in most computers there is only one camera, we set the value to 0. You can change the value if there are multiple cameras in your set up.

# To understand the project better, kindly go through the details of Haar features, Adaptive Boosting (AdaBoost) and Viola-Jones Algorithm.
