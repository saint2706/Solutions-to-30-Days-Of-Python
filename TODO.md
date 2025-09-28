# Repository Upgrade Roadmap

This document outlines the future work planned for the `Coding-For-MBA` repository, continuing the modernization and refactoring efforts.

## Phase 1: Core Data Science Curriculum (Days 26-37)

Apply the established refactoring pattern to the core data science lessons. For each day, the process will be:
1.  Refactor the main Python script into modular, testable functions.
2.  Create a corresponding test file in the `tests/` directory with `pytest`.
3.  Update the lesson's `README.md` to the new, more detailed format.
4.  Convert key lessons to Jupyter Notebooks (`.ipynb`) to enhance the interactive learning experience, especially for visualization and data manipulation lessons.

**Lessons to be addressed:**
- `Day_26_Statistics`
- `Day_27_Visualization` (Convert to Notebook)
- `Day_28_Advanced_Visualization` (Convert to Notebook)
- `Day_29_Interactive_Visualization` (Enhance existing notebook)
- `Day_30_Web_Scraping`
- `Day_31_Databases`
- `Day_32_Other_Databases`
- `Day_33_API`
- `Day_34_Building_an_API`
- `Day_35_Flask_Web_Framework`
- `Day_36_Case_Study`
- `Day_37_Conclusion`

## Phase 2: Machine Learning Curriculum (Days 38-50)

Apply the same refactoring and documentation pattern to the Machine Learning section. The focus will be on ensuring the code is clear, well-documented, and that the concepts are explained in the updated `README.md` format.

**Lessons to be addressed:**
- `Day_38_Linear_Algebra`
- `Day_39_Calculus`
- `Day_40_Intro_to_ML`
- `Day_41_Supervised_Learning_Regression`
- `Day_42_Supervised_Learning_Classification_Part_1`
- `Day_43_Supervised_Learning_Classification_Part_2`
- `Day_44_Unsupervised_Learning`
- `Day_45_Feature_Engineering_and_Evaluation`
- `Day_46_Intro_to_Neural_Networks`
- `Day_47_Convolutional_Neural_Networks`
- `Day_48_Recurrent_Neural_Networks`
- `Day_49_NLP`
- `Day_50_MLOps`

## High-Level Repository Goals

- **Increase Test Coverage:** While unit tests have been added for the refactored lessons, there is an opportunity to increase coverage and add more integration-style tests.
- **Performance Profiling:** The performance of other data-heavy scripts can be profiled and optimized, similar to the work done on `Day_25_Data_Cleaning`.
- **Interactive Visualizations:** Add more interactive visualizations using `Plotly` to other data-focused lessons to improve user engagement.
- **Dependency Review:** Periodically review and update the `requirements.txt` file to ensure all dependencies are on their latest stable versions.