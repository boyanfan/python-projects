#
# ELEC 292 Final Project - Group 53
# Created by Boyan Fan, Naman Nagia, Walker Yee on 03/24/2024
#

import h5py
import pandas as pd

# All CSV files will be stored in a list
data_jump = [
    pd.read_csv('data_jump_all_nagia.csv'),
    pd.read_csv('data_jump_all_yee.csv'),
    pd.read_csv('data_jump_pos1_fan.csv'),
    pd.read_csv('data_jump_pos2_fan.csv'),
    pd.read_csv('data_jump_pos3_fan.csv'),
]

data_walk = [
    pd.read_csv('data_walk_all_nagia.csv'),
    pd.read_csv('data_walk_pos1_fan.csv'),
    pd.read_csv('data_walk_pos2_fan.csv'),
    pd.read_csv('data_walk_pos3_fan.csv'),
    pd.read_csv('data_walk_all_yee.csv'),
]

# The dataset is stored in an HDF5 file called "dataset", in a structure of:
#
#           Root_____________________
#           /    \         \         \
#    Dataset     Member1   Member2   Member3
#    /   \       |         |         |
# Test   Train   name      name      name
#
# Note that comparing with the structure shown in the instruction
# An additional group called "AllData" is created to storing all the data segments
#
with h5py.File('./dataset.h5', 'w') as data:
    Dataset = data.create_group('Dataset')
    Member1 = data.create_group('Member1')
    Member2 = data.create_group('Member2')
    Member3 = data.create_group('Member3')

    # Temporary group for storing all segments, which will be deleted later
    AllData = Dataset.create_group('AllData')

    Test = Dataset.create_group('Test')
    Train = Dataset.create_group('Train')

    Member1.create_dataset('name', data="Boyan Fan")
    Member2.create_dataset('name', data="Naman Nagia")
    Member3.create_dataset('name', data="Walker Yee")

    # The index for each segment
    file_index = 1

    # Mark the data as "jump" and slice them into 5-second segments
    for csv in data_jump:
        # The measurement used a time interval as small as possible
        # The time interval may vary for different datasets
        # Therefore, an average time interval for each set must be estimated
        time_interval = csv.iloc[-1, 0] / (len(csv) - 1)

        # Create an additional column, where 1 indicate that the target is "jump"
        csv['isJump'] = 1

        # Find the number of element in the cvs for a 5-second window
        segment_length = int(5 / time_interval)

        # Find the number of segments
        number_of_segment = int((len(csv) - 1) / segment_length)

        # Drop the first segment and the last segment
        # Since these data are collected during the setting-up phase, a.k.a. noise
        for segment_index in range(1, number_of_segment - 2):
            # Get the start index
            start = segment_index * segment_length
            # Get the end index
            end = (segment_index + 1) * segment_length
            # Create the segment
            segment = csv.iloc[start:end, :]
            # Store the segment
            AllData.create_dataset(name=f'segment{file_index}', data=segment)
            # Increment in index
            file_index += 1

    # The file index for walk data starts at this index
    file_index_walk_start = file_index

    # Mark the data as "walk" and slice them into 5-second segments
    for csv in data_walk:
        # The measurement used a time interval as small as possible
        # The time interval may vary for different datasets
        # Therefore, an average time interval for each set must be estimated
        time_interval = csv.iloc[-1, 0] / (len(csv) - 1)

        # Create an additional column, where 1 indicate that the target is "jump"
        csv['isJump'] = 0

        # Find the number of element in the cvs for a 5-second window
        segment_length = int(5 / time_interval)

        # Find the number of segments
        number_of_segment = int((len(csv) - 1) / segment_length)

        # Drop the first segment and the last segment
        # Since these data are collected during the setting-up phase, a.k.a. noise
        for segment_index in range(1, number_of_segment - 2):
            # Get the start index
            start = segment_index * segment_length
            # Get the end index
            end = (segment_index + 1) * segment_length
            # Create the segment
            segment = csv.iloc[start:end, :]
            # Store the segment
            AllData.create_dataset(name=f'segment{file_index}', data=segment)
            # Increment in index
            file_index += 1

    # The total number of segments
    total_number_of_segment = len(AllData.items())

    # Use 10% of segments for testing
    number_of_test = int(total_number_of_segment * 0.055) * 2

    # New file index for Test and Train
    test_index, walk_index = 0, 0

    # Copy segments from "AllData" to "Test" and "Train" with the given proportion
    for index in range(1, total_number_of_segment + 1):
        if index <= number_of_test / 2 or (file_index_walk_start <= index < file_index_walk_start + number_of_test / 2):
            Test.create_dataset(f'segment{test_index}', data=data.get(f'Dataset/AllData/segment{index}'))
            test_index += 1
        else:
            Train.create_dataset(f'segment{walk_index}', data=data.get(f'Dataset/AllData/segment{index}'))
            walk_index += 1

    # Delete the temporary group
    del data['/Dataset/AllData']