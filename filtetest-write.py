def generate_database_report(log_file):
    # Open the log file and separate the entries into errors, warnings, and info
    with open(log_file, "r") as file:
        # Open separate files for each type of log entry (errors, warnings, info)
        with open("database_errors.txt", "w") as error_file, \
             open("database_warnings.txt", "w") as warning_file, \
             open("database_info.txt", "w") as info_file:
            
            # Read each line in the log file
            for line in file.readlines():
                # Check if the line contains "database" related entries
                if "database" in line.lower():
                    # Write to appropriate file based on log level
                    if "ERROR" in line:
                        error_file.write(line.strip() + "\n")  # Write error message to file
                    elif "WARNING" in line:
                        warning_file.write(line.strip() + "\n")  # Write warning message to file
                    elif "INFO" in line:
                        info_file.write(line.strip() + "\n")  # Write info message to file

    # After processing, create a summary report
    errors_count = sum(1 for line in open("database_errors.txt"))
    warnings_count = sum(1 for line in open("database_warnings.txt"))
    info_count = sum(1 for line in open("database_info.txt"))

    report = "Database Log Report\n"
    report += "--------------------------------------\n"
    report += "Total Database Errors: " + str(errors_count) + "\n"
    report += "Total Database Warnings: " + str(warnings_count) + "\n"
    report += "Total Database Info Messages: " + str(info_count) + "\n"
    report += "\nDetails are stored in the following files:\n"
    report += "1. database_errors.txt\n"
    report += "2. database_warnings.txt\n"
    report += "3. database_info.txt\n"

    return report

# Example usage:
log_file = "log.txt"  # Path to your log file
report = generate_database_report(log_file)

# Print the summary report to the console
print(report)
