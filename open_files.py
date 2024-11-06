# Define the setup name to run in each project
setup_name = "Setup"  # Replace with the actual setup name in each project

# List of project files to process
base_string = "/home/id_number/Ansoft/CPW_port_impedance_sweep/CPWport"
project_files = []

index = ["47_1", "47_2", "47_3", "47_4", "47_6", "47_7", "47_8", "47_9"]

for i in index:
    total_string = base_string + i + ".aedt"
    project_files.append(total_string)
# Function to process each project file
def process_project(project_file):
    try:
        # Open the project
        print("Opening project: " + project_file)
        oDesktop.OpenProject(project_file)

        # Access the active project and design
        oProject = oDesktop.GetActiveProject()
        if oProject is None:
            print("Failed to open project: " + project_file)
            return

        oDesign = oProject.GetActiveDesign()

        if oDesign is None:
            print("No active design found in project: " + project_file)
            return

        # Fit all objects in the view
        oEditor = oDesign.SetActiveEditor("3D Modeler")
        oEditor.FitAll()
        print("View fitted for project: " + project_file)

    except Exception as e:
        print("An error occurred with project '" + project_file + "': " + str(e))

# Loop through each project in the list and process it
for project_file in project_files:

    process_project(project_file)

print("All projects in the queue have been processed.")