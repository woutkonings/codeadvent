def read_reports(filename):
    reports = []
    
    with open(filename, 'r') as file:
        for line in file:
            # Convert each line into a list of integers
            report = list(map(int, line.strip().split()))
            reports.append(report)
    
    return reports

def check_report(report: list[int]) -> bool:
    differences = [b - a for a, b in zip(report[:-1], report[1:])]
    
    # Check if differences are between 1 and 3 or between -3 and -1
    if not all(1 <= d <= 3 or -3 <= d <= -1 for d in differences):
        return False
        
    # Check if all differences are in the same direction (all positive or all negative)
    if not (all(d > 0 for d in differences) or all(d < 0 for d in differences)):
        return False
        
    return True

def check_report_with_dampener(report: list[int]) -> bool:
    # First check if it's already safe without removing anything
    if check_report(report):
        return True
        
    # Try removing each level one at a time
    for i in range(len(report)):
        # Create new list without the current index
        dampened_report = report[:i] + report[i+1:]
        if check_report(dampened_report):
            return True
            
    return False

if __name__ == "__main__":
    reports = read_reports('day2input.txt')
    
    # Example: Print the first 3 reports
    for i, report in enumerate(reports[:6]):
        print(f"Report {i+1}: {report}. Status: {check_report(report)}")

    safe_reports = [x for x in reports if check_report(x)]
    print(len(safe_reports))


    safe_reports = [x for x in reports if check_report_with_dampener(x)]
    print(len(safe_reports))