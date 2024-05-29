import re
from datetime import datetime, timedelta
from pprint import pprint 

def clean_data(input_data):
    output_data = []
    # regex to get the patten
    date_time_pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})'  
    for item in input_data:
        # get the the match
        date_time_match = re.search(date_time_pattern, item)
        if date_time_match:
            date = date_time_match.group(1)
            time = date_time_match.group(2)
            output_data.append(date + ' ' + time)
    return output_data

def sort_data(input_data):
    # sort the date_time
    output_data = sorted(input_data)
    return output_data

def arrange_data(input_data):
    # parse string to date
    parsed_data = []
    for i in input_data:
        parsed_data.append(datetime.strptime(i, '%Y-%m-%d %H:%M:%S').date())
    #pprint(parsed_data)
    output_data = []
    previous_date = None
    line = []
    for current_date in parsed_data:
        # first row or first non-consecutive number
        reset = (previous_date is None) or (current_date - previous_date) > timedelta(days=1)
        # if meet reset condition, reset line
        if reset:
            line = []
        # add current item into the line 
        line.append(current_date)
        # if meet reset condition, add line into output_data
        if reset:
            # only add if line is not empty
            if len(line) > 0:
                output_data.append(line)
        previous_date = current_date
    return output_data

def count_data(input_data):
    output_data = []
    for item in input_data:
        # get start date, end date and length of consecutive day
        new_item = (item[0].strftime('%Y-%m-%d'), item[-1].strftime('%Y-%m-%d'), len(item))
        output_data.append(new_item)
    return output_data

def main(raw_data):
    cleaned_data = clean_data(raw_data)
    sorted_data = sort_data(cleaned_data)
    arranged_data = arrange_data(sorted_data)
    counted_data = count_data(arranged_data)
    finalized_data = sorted(counted_data, key=lambda x:x[2],reverse=True)
    return finalized_data

if __name__ == '__main__':
    import seed
    output = main(seed.res)
    print("| START      | END        | LENGTH |")
    print("|------------|------------|--------|")
    for row in output:
        print("| {0} | {1} | {2:6d} |".format(row[0], row[1], row[2]))