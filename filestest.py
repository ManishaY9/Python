errors = []
warnings = []
info = []
with open("log.txt", "r") as file:
    for line in file.readlines():
        if "database" in line.lower():
            if "ERROR" in line:
                errors.append(line.strip()) 
            elif "WARNING" in line:
                    warnings.append(line.strip())  
            elif "INFO" in line:
                    info.append(line.strip())

    report = "Database Log Report\n"
    report += "--------------------------------------\n"
    report += "Total Database Errors: " + str(len(errors)) + "\n"
    report += "Total Database Warnings: " + str(len(warnings)) + "\n"
    report += "Total Database Info Messages: " + str(len(info)) + "\n"
    
if errors:
    report += "\nDatabase Errors:\n" 
    for error in errors:
        report += "- " + error + "\n"


if warnings:
    report += "\nDatabase Warning:\n" 
    for warning in warnings:
        report += "- " + warning + "\n"

print(report)