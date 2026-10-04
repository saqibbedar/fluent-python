| Aspect                 | **Classification**                       | **Regression**                      |
| :--------------------- | :--------------------------------------- | :---------------------------------- |
| Output                 | discrete label (+1 or −1)                | continuous real number (any value)  |
| Function               | ( f_w(x) = sign(w·phi(x)) )      | ( f_w(x) = w·phi(x) )              |
| Meaning of (w·phi(x)) | margin or score (used to *decide class*) | actual predicted numeric value      |
| Decision boundary      | where ( w·phi(x)=0 )                    | not applicable (no boundary)        |
| Loss function          | 0–1, hinge, or logistic loss             | squared error ( (y - w·phi(x))^2 ) |
| Update type            | Perceptron / SVM / Logistic              | Gradient descent / Normal equation  |
| Example task          | Spam detection (is email spam or not?)   | House price prediction (predict $)  |