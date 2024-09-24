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

            **Histograms**
            
            **Line Graphs**
            
            **Scatter Plots**
            
            **Heatmaps**
            
            **Pie Charts**
            
        These visualizations give you a clear breakdown of your current and required marks.

**📝 PDF Gradesheet:**
        Generate a customized PDF gradesheet containing your current marks, required marks, and a breakdown for each subject.
        
**🗣 Faculty Comments:**
        A chatbot that offers subject-specific advice from faculty to help you improve your performance.

**💪 Motivational Quotes:**
       Get random motivational quotes to keep you inspired throughout your academic journey.

**📅 Upcoming Exam Schedules:**
       A quick view of upcoming exams for your subjects, helping you stay prepared.

**😊 Emotion Feedback:**
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
      
## How to Use?

**1: Welcome Screen:** The home screen welcomes you to the Student Score Analysis and Prediction Tool. Provides a brief overview of the tool.

**2: Enter Your Marks:** Use the sidebar to input your current marks for each subject and component (e.g., M1, M2, EndSem, Others). Select completed exams for each subject from the dropdown menus.

**3: Set Target SGPA:** Use the slider in the sidebar to set your target SGPA.

**4: View Required Marks:** The main screen displays the required marks for each subject and component to achieve your target SGPA. Shows whether achieving your target SGPA is feasible based on your current marks.

**5: Visualizations:** Select the desired visualization type (Histogram, Heatmap, Line Graph, Scatter Plot, Pie Chart) from the dropdown menu. The corresponding chart is displayed for a detailed analysis.

**6: Overall Analysis:** Provides an overall analysis of your current and required marks. Displays subject-wise score breakdown.

**7: Upcoming Schedules:** Lists the upcoming exams and assessments for each subject.

**8: Faculty Comments:** Get helpful comments from faculty members for each subject. Select a subject from the dropdown menu and click the button to display comments.

**9: Motivational Quotes:** Displays random motivational quotes to keep you inspired.

**10: Download Gradesheet:** Click the "Download PDF" button to download your gradesheet as a PDF.

## Visualizations

Histograms and heatmaps provide an overview of your scores.

Line graphs and scatter plots show how your scores are distributed across various components.

Pie charts give a breakdown of marks distribution per subject.

## Example Screenshots
![Screenshot 2024-09-24 121626](https://github.com/user-attachments/assets/60d175df-efda-4939-982f-a527ed8922cf)
![Screenshot 2024-09-24 121651](https://github.com/user-attachments/assets/4e20d34b-e7a7-46c8-a4eb-56fa057a8594)
![Screenshot 2024-09-24 121906](https://github.com/user-attachments/assets/e5f94258-68ec-43ee-b235-ea1733ec98c0)
![Screenshot 2024-09-24 121707](https://github.com/user-attachments/assets/9d4b0b4e-da99-43dd-8d66-543dcd96fcae)
![Screenshot 2024-09-24 121917](https://github.com/user-attachments/assets/8f248004-45f5-4341-857e-843c1277a379)
![Screenshot 2024-09-24 121928](https://github.com/user-attachments/assets/28712b66-7bfa-4dde-a2a7-845773a8621e)
![Screenshot 2024-09-24 121937](https://github.com/user-attachments/assets/e7b3202c-ccee-4c5d-8c80-6fb8f0ba3b65)

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
