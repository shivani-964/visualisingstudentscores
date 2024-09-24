## Student Score Analysis and Prediction Tool 🎓

This project is a Streamlit-based web application designed to help students analyze their current academic performance and predict the marks required to achieve a target SGPA (Semester Grade Point Average). The tool provides insights on component-wise marks for various subjects and generates a personalized PDF gradesheet.

## Features

**📊 Performance Analysis:**
        Input your current marks for different components of each subject (Midterms, EndSem, Others).
        Predict the marks required in upcoming exams to achieve a desired SGPA.
        
**✅ Feasibility Check:**
        The tool determines if achieving the target SGPA is feasible based on the inputted current marks.
        
**📈 Visualizations:**

        Choose from multiple types of visualizations:
        
            **~ Histograms**
            
            **~ Line Graphs**
            
            **~ Scatter Plots**
            
            **~ Heatmaps**
            
            **~ Pie Charts**
            
        These visualizations give you a clear breakdown of your current and required marks.

**📝 PDF Gradesheet:**
        Generate a customized PDF gradesheet containing your current marks, required marks, and a breakdown for each subject.
        
**🗣 Faculty Comments:**
        A chatbot that offers subject-specific advice from faculty to help you improve your performance.

**💪 Motivational Quotes:**
       Get random motivational quotes to keep you inspired throughout your academic journey.

**📅 Upcoming Exam Schedules:**
       A quick view of upcoming exams for your subjects, helping you stay prepared.

**Emotion Feedback:**
       Express how you feel about your component-wise marks, whether you’re happy, neutral, or unhappy.

## Tech Stack
      **Frontend:** Streamlit
      **Backend:** Python
      **Data Handling:** Pandas, NumPy
      **Visualization:** Matplotlib, Seaborn
      **PDF Generation:** FPDF

## Installation

To set up this project locally, follow these steps:

**1: Clone the repository:** 

      git clone https://github.com/your-username/studentscores.git
      cd studentscores
      
 **2: Create a virtual environment (Optional but recommended):**
 
      python -m venv env
      source env/bin/activate # On Windows, use 'env\Scripts\activate'
      
**3: Install required dependencies:**

      pip install -r requirements.txt
      # If there is no requirements.txt, manually install the required libraries: 
      pip install streamlit pandas numpy matplotlib seaborn fpdf
      
**4: Run the Streamlit application:**

      streamlit run studentscores.py
      
**5: Open the app in your browser:** 

      Streamlit will automatically open a browser window showing the app. If not, you can access it by navigating to:
      http://localhost:8501/
      
## Usage

**1: Enter Your Marks:** Input your marks in each subject for different components (Midterms, EndSem, Others).

**2: Set Target SGPA:** Adjust the slider to set your target SGPA.

**3: Analyze Results:** View the required marks, check the feasibility, and visualize your performance.

**4: Download Gradesheet:** Generate and download a PDF gradesheet with the current and required marks.

## Visualizations

Histograms and heatmaps provide an overview of your scores.

Line graphs and scatter plots show how your scores are distributed across various components.

Pie charts give a breakdown of marks distribution per subject.

## Example Screenshots

## Contributions

Feel free to contribute to this project by submitting issues, feature requests, or pull requests.

**Steps for Contribution:**

1: Fork the repository.

2: Create a new branch (git checkout -b feature-name).

3: Make your changes.

4: Commit your changes (git commit -m 'Add some feature').

5: Push to the branch (git push origin feature-name).

6: Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
If you have any questions or feedback, feel free to reach out!
