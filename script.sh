#!/bin/bash

# Function to create project structure for Keyword Driven Framework
create_keyword_driven() {
    mkdir -p $project_name/{locators,test_cases,keywords,data,utils,reports}
    echo "Created Keyword Driven Framework structure for $project_name"
    # Copy boilerplate code for each file
    cp boilerplates/keyword_driven/sample_locators.py "$project_name/locators/"
    cp boilerplates/keyword_driven/sample_keywords.py "$project_name/keywords/"
    cp boilerplates/keyword_driven/sample_test_cases.py "$project_name/test_cases/"
    cp boilerplates/keyword_driven/sample_data.py "$project_name/data/"
    cp boilerplates/keyword_driven/sample_utils.py "$project_name/utils/"
    cp boilerplates/keyword_driven/sample_reports.py "$project_name/reports/"
}

# Function to create project structure for Data Driven Framework
create_data_driven() {
    mkdir -p $project_name/{locators,test_cases,data,utils,reports}
    echo "Created Data Driven Framework structure for $project_name"
    # Copy boilerplate code for each file
    cp boilerplates/data_driven/sample_locators.py "$project_name/locators/"
    cp boilerplates/data_driven/sample_test_cases.py "$project_name/test_cases/"
    cp boilerplates/data_driven/sample_data.py "$project_name/data/"
    cp boilerplates/data_driven/sample_utils.py "$project_name/utils/"
    cp boilerplates/data_driven/sample_reports.py "$project_name/reports/"
}

# Function to create project structure for Hybrid Framework
create_hybrid() {
    mkdir -p $project_name/{locators,test_cases,keywords,data,utils,reports}
    echo "Created Hybrid Framework structure for $project_name"
    # Copy boilerplate code for each file
    cp boilerplates/hybrid/sample_locators.py "$project_name/locators/"
    cp boilerplates/hybrid/sample_keywords.py "$project_name/keywords/"
    cp boilerplates/hybrid/sample_test_cases.py "$project_name/test_cases/"
    cp boilerplates/hybrid/sample_data.py "$project_name/data/"
    cp boilerplates/hybrid/sample_utils.py "$project_name/utils/"
    cp boilerplates/hybrid/sample_reports.py "$project_name/reports/"
}

# Function to create project structure for Behavior Driven Framework
create_behavior_driven() {
    mkdir -p $project_name/{features,step_definitions,utils,reports}
    echo "Created Behavior Driven Framework structure for $project_name"
    # Copy boilerplate code for each file
    cp boilerplates/behavior_driven/sample_feature.feature "$project_name/features/"
    cp boilerplates/behavior_driven/sample_steps.py "$project_name/step_definitions/"
    cp boilerplates/behavior_driven/sample_utils.py "$project_name/utils/"
    cp boilerplates/behavior_driven/sample_reports.py "$project_name/reports/"
}

# Function to create project structure for Modular Framework
create_modular() {
    mkdir -p $project_name/{modules,test_cases,data,utils,reports}
    echo "Created Modular Framework structure for $project_name"
    # Copy boilerplate code for each file
    cp boilerplates/modular/sample_module.py "$project_name/modules/"
    cp boilerplates/modular/sample_test_cases.py "$project_name/test_cases/"
    cp boilerplates/modular/sample_data.py "$project_name/data/"
    cp boilerplates/modular/sample_utils.py "$project_name/utils/"
    cp boilerplates/modular/sample_reports.py "$project_name/reports/"
}

# Main menu
echo "Welcome to the Selenium Testing Framework Setup Script"

while true; do
    echo "Please enter the project name:"
    read project_name
    if [ -z "$project_name" ]; then
        echo "Project name cannot be empty. Please try again."
    else
        break
    fi
done

echo "Please select the testing framework:"
echo "1. Keyword Driven Framework"
echo "2. Data Driven Framework"
echo "3. Hybrid Framework"
echo "4. Behavior Driven Framework"
echo "5. Modular Framework"

while true; do
    read framework_choice
    case $framework_choice in
        1)
            create_keyword_driven
            break
            ;;
        2)
            create_data_driven
            break
            ;;
        3)
            create_hybrid
            break
            ;;
        4)
            create_behavior_driven
            break
            ;;
        5)
            create_modular
            break
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
done

echo "Project structure created successfully!"
