# Machine Learning Curriculum Roadmap

This roadmap outlines a phased journey from classic machine learning foundations to modern deep learning systems and production operations. Each phase highlights anchor lessons from the Coding for MBA series and recommends follow-on topics so you can keep advancing after Day 57.

## Phase 1 – Classic Machine Learning Foundations

> **Start here if you are following the Day 40–53 sequence.**
>
> The goal of Phase 1 is to master supervised learning workflows, evaluation techniques, and model selection before layering on deep learning.

| Day | Lesson | Key takeaway |
| --- | ------ | ------------ |
| Day 40 | [Introduction to Machine Learning](../Day_40_Intro_to_ML/README.md) | Frame ML problems, manage the train/validate/test split, and measure performance with cross-validation. |
| Day 41 | [Supervised Learning – Regression](../Day_41_Supervised_Learning_Regression/README.md) | Fit linear models, tune regularisation, and interpret coefficients for business insights. |
| Day 42 | [Supervised Learning – Classification Part 1](../Day_42_Supervised_Learning_Classification_Part_1/README.md) | Compare logistic regression and decision trees while diagnosing accuracy, precision, and recall. |
| Day 43 | [Supervised Learning – Classification Part 2](../Day_43_Supervised_Learning_Classification_Part_2/README.md) | Ensemble methods, ROC curves, and thresholding strategy selection. |
| Day 44 | [Unsupervised Learning](../Day_44_Unsupervised_Learning/README.md) | Cluster customer segments and reduce dimensionality with PCA. |
| Day 45 | [Feature Engineering & Evaluation](../Day_45_Feature_Engineering_and_Evaluation/README.md) | Build repeatable feature pipelines and validate models with more nuanced metrics. |
| Day 46 | [Intro to Neural Networks](../Day_46_Intro_to_Neural_Networks/README.md) | Understand perceptrons, activation functions, and gradient descent. |
| Day 47 | [Convolutional Neural Networks](../Day_47_Convolutional_Neural_Networks/README.md) | Apply convolutional filters for image classification. |
| Day 48 | [Recurrent Neural Networks](../Day_48_Recurrent_Neural_Networks/README.md) | Model sequential data with RNNs, LSTMs, and GRUs. |
| Day 49 | [Natural Language Processing](../Day_49_NLP/README.md) | Build text classification pipelines with tokenisation and embeddings. |
| Day 50 | [MLOps](../Day_50_MLOps/README.md) | Package, persist, and monitor models for reliable deployment. |
| Day 51 | [Regularised Models](../Day_51_Regularized_Models/README.md) | Contrast ridge, lasso, elastic net, and Poisson GLMs while measuring coefficient shrinkage. |
| Day 52 | [Ensemble Methods](../Day_52_Ensemble_Methods/README.md) | Blend bagging, boosting, and stacking ensembles with calibrated probability estimates. |
| Day 53 | [Model Tuning & Feature Selection](../Day_53_Model_Tuning_and_Feature_Selection/README.md) | Optimise hyperparameters with grid/Bayesian search and validate feature subsets via permutation importance and RFE. |
| Day 54 | [Probabilistic Modeling](../Day_54_Probabilistic_Modeling/README.md) | Master Gaussian mixtures, Bayesian classifiers, EM, and HMM log-likelihoods to reason about uncertainty. |
| Day 55 | [Advanced Unsupervised Learning](../Day_55_Advanced_Unsupervised_Learning/README.md) | Deploy DBSCAN, hierarchical clustering, t-SNE/UMAP-style embeddings, and autoencoder-driven anomaly detection. |
| Day 56 | [Time Series & Forecasting](../Day_56_Time_Series_and_Forecasting/README.md) | Forecast seasonal demand with ARIMA/SARIMAX, Holt-Winters, and Prophet-style decompositions plus robust evaluation. |
| Day 57 | [Recommender Systems](../Day_57_Recommender_Systems/README.md) | Build collaborative filtering and matrix factorisation recommenders with implicit-feedback aware ranking metrics. |

### Recommended next steps after Phase 1

- Apply cross-validation and feature engineering to your own datasets, documenting experiment results in a reproducible format.
- Practice hyperparameter optimisation with grid search, random search, and Bayesian optimisation frameworks.
- Explore AutoML tooling (e.g., Auto-sklearn, H2O AutoML) to accelerate baseline model comparisons.

## Phase 2 – Modern Deep Learning & Representation Learning

Deep learning expands the model families available in Phase 1. Focus on building intuition for architectures, transfer learning, and optimisation.

- Refresh Python packages for GPU acceleration (PyTorch or TensorFlow) and practice training models on cloud notebooks.
- Study convolutional network variants (ResNet, EfficientNet) and fine-tune pretrained models for domain-specific images.
- Learn about transformer architectures for text, vision, and multimodal data, starting with embeddings and attention mechanisms.
- Experiment with self-supervised learning and contrastive objectives to pre-train representations on unlabelled data.

## Phase 3 – Responsible AI & Model Governance

Ensure that your models meet ethical, legal, and organisational standards before moving them into production.

- Perform bias and fairness audits using disparate impact, equal opportunity, and calibration diagnostics.
- Implement explainability techniques (feature importance, SHAP, LIME) to communicate model decisions to stakeholders.
- Establish data governance practices: data lineage, versioning, and documentation (model cards, data sheets).
- Learn the regulatory landscape (GDPR, CCPA, sector-specific rules) and how they influence data collection and model deployment.

## Phase 4 – MLOps, Monitoring, and Lifecycle Management

Turn prototypes into production systems by investing in reliable infrastructure and collaboration workflows.

- Industrialise feature pipelines with tools like Feature Store platforms or workflow orchestrators (Airflow, Prefect).
- Automate training and evaluation with CI/CD pipelines, integrating unit tests, data quality checks, and model validation gates.
- Deploy models to scalable serving infrastructure (REST endpoints, batch scoring, or streaming) with containerisation and serverless platforms.
- Instrument monitoring for data drift, model drift, and performance regressions; integrate alerting and human-in-the-loop retraining.
- Track experiments, artefacts, and lineage with MLflow, Weights & Biases, or similar platforms, ensuring reproducibility across teams.

## Putting it all together

Progressing through these phases transforms the Day 40–53 lessons into a comprehensive ML competency path. Loop back to earlier phases whenever you encounter new domains or stakeholders—revisiting the fundamentals will keep each new system grounded in sound methodology.
