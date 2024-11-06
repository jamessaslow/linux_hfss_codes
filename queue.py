# Define the setup name to run in each project
setup_name = "Setup"  # Replace with the actual setup name in each project

# List of project files to process
base_string = "/home/id_number/Ansoft/CPW_port_impedance_sweep/CPWport"
project_files = []

index = ["10", "20", "30", "40", "41", "42", "43", "44", "45", "46","47",
         "47_5", "48", "48_5",
         "49", "49_5", "50", "50_5", "51", "51_5", "52", "52_5", "53", "54",
         "55", "56", "57", "58","59","60",
         "70", "80", "90", "100"]

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

        # Run the specified setup
        print("Running setup: " + setup_name + " for project " + project_file)
        oDesign.Analyze(setup_name)

        # Save and close the project after the simulation is complete
        oProject.Save()

        print("Project '" + project_file + "' completed, analyzed, and saved.")

        # Close the project to free resources
        oDesktop.CloseProject(oProject.GetName())


    except Exception as e:
        print("An error occurred with project '" + project_file + "': " + str(e))

# Loop through each project in the list and process it
for project_file in project_files:

    process_project(project_file)

print("All projects in the queue have been processed.")