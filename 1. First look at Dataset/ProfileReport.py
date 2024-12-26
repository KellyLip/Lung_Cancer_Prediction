# Install the necessary package
!pip install ydata-profiling

# Import the profiling library
from ydata_profiling import ProfileReport

def generate_profiling_report(df, title="Data Profiling Report", output_file=None):
    profile = ProfileReport(df, title=title)
    
    # Display the report in the notebook
    profile.to_notebook_iframe()
    
    # Save the report if an output file is specified
    if output_file:
        profile.to_file(output_file)
        print(f"Report saved to {output_file}")
    
    return profile

report = generate_profiling_report(df, title="Cancer Patients Report", output_file="cancer_patients_report.html")
