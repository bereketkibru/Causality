# Causality
## Data overview
Consequently, detecting cancer at an early stage gives a 30% chance of it being treated
effectively, while late detection makes its treatment complex. In detecting breast cancer at
an early stage, some techniques are employed by medical practitioners such as: surgical
biopsy which has approximately 100% correctness, Fine Needle Aspiration (FNA) with visual
interpretation with 65% to 98% correctness, and mammography with 63% to 97%
correctness. However, the first technique is the most reliable but comes with a costly price
tag.

The Breast Cancer Wisconsin Diagnostic dataset (WDBC) was obtained from the UCI
Machine Learning Repository. Features are computed from a digitized image of a Fine
Needle Aspiration (FNA) They describe characteristics of the cell nuclei present in the
image. The WDBC consists of 569 instances and 30 real valued input features
Attribute Information:
1) ID number
2) Diagnosis (M = malignant, B = benign)
3) -32)

Ten real-valued features are computed for each cell nucleus:
* radius (mean of distances from center to points on the perimeter)
* texture (standard deviation of gray-scale values)
* perimeter
* area
* smoothness (local variation in radius lengths)
* compactness (perimeter^2 / area - 1.0)
* concavity (severity of concave portions of the contour)
* concave points (number of concave portions of the contour)
* symmetry
* fractal dimension ("coastline approximation" - 1)


The mean, standard error and "worst" or largest (mean of the three largest values) of these
features were computed for each image, resulting in 30 features. For instance, field 3 is Mean
Radius, field 13 is Radius SE, field 23 is Worst Radius.




## TECHNIQUES USED TO PERFORM CAUSAL INFERENCE
We use two different libraries to perform casual inference 
### Dowhy	
DoWhy is a Python Library that sparks causal thinking and analysis via 4-steps:
1.	Model a causal inference problem using assumptions that we create.
2.	 Identify an expression for the causal effect under these assumptions (“causal estimand”).
3.	Estimate the expression using statistical methods such as matching or instrumental variables.
4.	Verify the validity of the estimate using a variety of robustness checks.

If we make it simpler, the way DoWhy package done Causal Analysis is by Creating Causal Model -> Identify Effect -> Estimate the Effect -> Validate.
### CausalNex 
CausualNex is a Python library that uses Bayesian Networks to combine machine learning and domain expertise for causal reasoning. You can use CausalNex to uncover structural relationships in your data, learn complex distributions, and observe the effect of potential interventions.







