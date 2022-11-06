# Author Name: Pritam Suwal Shrestha (23771397)
# Date: 15 October, 2022
# CITS1401: Computational Thinking with Python Project 2 Semester 2 2022

COLUMN_NAMES = {
    'SUB_ID': 'SUBJID',
    'LANDMARK': 'LANDMARK',
    'OX': 'OX',
    'OY': 'OY',
    'OZ': 'OZ',
    'MX': 'MX',
    'MY': 'MY',
    'MZ': 'MZ'
}

FACIAL_DISTANCES = {
    'EXEN': ('EX', 'EN'),
    'ENAL': ('EN', 'AL'),
    'ALEX': ('AL', 'EX'),
    'FTSBAL': ('FT', 'SBAL'),
    'SBALCH': ('SBAL', 'CH'),
    'CHFT': ('CH', 'FT')
}

LANDMARKS = {
    'FT': 'FT',
    'EX': 'EX',
    'EN': 'EN',
    'AL': 'AL',
    'SBAL': 'SBAL',
    'CH': 'CH',
    'PRN': 'PRN'
}

OP1_LANDMARKS = {
    'FT': 'FT',
    'EX': 'EX',
    'EN': 'EN',
    'AL': 'AL',
    'SBAL': 'SBAL',
    'CH': 'CH',

}

OUTPUT_KEYS = {
    'OP1': 'OP1',
    'OP2': 'OP2',
    'OP3': 'OP3',
    'OP4': 'OP4'
}


def main(csvfile, SubjIDs):
    """
    :param csvfile: The name of the CSV file containing the facial data record which needs to be analysed.
                    Below are the first two rows of the sample file.

        +─────────+───────────+───────────+───────────+───────────+──────────────+───────────────+───────────────+
        | SubjID  | Landmark  | OX        | OY        | OZ        | MX           | MY            | MZ            |
        +─────────+───────────+───────────+───────────+───────────+──────────────+───────────────+───────────────+
        | B7033   | Ft        | -48.5857  | -17.8732  | -24.9483  | -47.9819987  | -16.20372355  | -25.67910384  |
        +─────────+───────────+───────────+───────────+───────────+──────────────+───────────────+───────────────+

        The first row of the CSV file contains the following headers:
            1. SubjID: The identity of a human subject.

            2. Landmark: The facial landmark as mentioned in Table 1.

            3. “OX”, “OY” and “OZ”: The 3D location of the landmark in X, Y and Z axes respectively on the original
                face (See Figure-1 (left)).

            4. “MX”, “MY” and “MZ”: The 3D location of the landmark in X, Y and Z axes respectively on the mirrored
                face (See Figure-1 (right)).

            Note: The X, Y and Z coordinates are in millimetres and need to be within the bounds [-200,200].

        We do not have prior knowledge about the number of subjects we have to analyse (i.e. the number of rows) that
        the CSV file contains. Also, we are not aware of the order of the columns, so your program needs to check for
        the column heading to retrieve respective information. The columns ‘SubjID’ and ‘Landmark’ are strings while
        the remaining data is numeric.


    :param SubjIDs: A list of two IDs of the subjects which need to be analysed. Remember that the ID is a string and
                    is case insensitive.

    :return: The function is required to return the following outputs in the order provided below. For ease of
    description, we will refer to the input SubjID containing two IDs: “F1” and “F2” as [“F1”,”F2”].

        • OP1: A list of two dictionaries containing the facial asymmetry values between the original and mirrored
        face for the landmarks mentioned in Table-1 for each face F1 and F2 respectively. The keys in the
        dictionaries are the abbreviations ( upper case) of the landmarks (e.g. EX, FT etc.) and their values contain
        the 3D asymmetry between the original and mirrored landmarks. The formula to calculate the 3D asymmetry is
        given at the end of this project sheet.

        OP1 =>  [
                {'FT': 1.9198, 'EX': 1.8028, 'EN': 1.6555, 'AL': 2.5577, 'SBAL': 0.9023, 'CH': 1.7901},
                {'FT': 1.807, 'EX': 2.2892, 'EN': 0.9371, 'AL': 1.9393, 'SBAL': 1.1624, 'CH': 2.7713}
                ]


        • OP2: A list of two dictionaries containing the facial distances (as mentioned in Table-2) for each face F1
        and F2 respectively. The keys in the dictionaries are the abbreviations (upper case) of the distances (e.g.
        EXEN, ENAL etc.) and their values contain the 3D Euclidean distance between the corresponding landmarks (see
        last two columns of Table-2) on the original face. The formula to calculate the Euclidean distance between
        two 3D landmarks is given at the end of this project sheet.

        OP2 =>  [
                {'EXEN': 33.092, 'ENAL': 34.6946, 'ALEX': 50.1037, 'FTSBAL': 91.5324, 'SBALCH': 33.7109,
                'CHFT': 98.1642},
                {'EXEN': 34.4401, 'ENAL': 37.7494, 'ALEX': 54.0952, 'FTSBAL': 90.3202, 'SBALCH': 38.4123,
                'CHFT': 104.8566}
                ]

        • OP3: First calculate the total facial asymmetries of each subject in the CSV file. Your task is to
        return a list of Tuple sequences of the 5 faces having the lowest total face asymmetry. The first member of
        each tuple is the “SubjID” of the face while the second member is the total asymmetry of this face. The list
        must be in increasing order of total facial asymmetry such that the first tuple would indicate the face that
        has the lowest total facial asymmetry. Therefore, the 5 tuple sequences will represent 5 lowest total facial
        asymmetries.

        OP3 => [
                ('E4996', 8.3254),
                ('H1178', 9.1597),
                ('F7831', 9.3268),
                ('J6687', 9.3878),
                ('K6431', 9.6359)
            ]


        OP4: The cosine similarity between faces F1 and F2 based on the six distances calculated above (OP2). The
        formula to calculate cosine similarity is provided at the end of this project sheet.

        OP4 => 0.9991

    """

    raw_rows = extract_raw_data(csvfile)

    if not raw_rows:
        outputs = {
            OUTPUT_KEYS['OP1']: None,
            OUTPUT_KEYS['OP2']: None,
            OUTPUT_KEYS['OP3']: None,
            OUTPUT_KEYS['OP4']: None
        }

        return outputs['OP1'], outputs['OP2'], outputs['OP3'], outputs['OP4']

    raw_row_headers_as_string = raw_rows[0].upper()
    row_headers = raw_row_headers_as_string.split(',')

    raw_data_rows = raw_rows[1:]
    processed_rows = get_processed_rows(row_headers, raw_data_rows)
    subjects_data = get_subjects_data(processed_rows)

    subj_ids = extract_sub_ids(SubjIDs)

    list_of_facial_asymmetries = get_list_of_facial_asymmetries(subj_ids, subjects_data)
    list_of_euclidean_distances = get_list_of_euclidean_distances(subj_ids, subjects_data)
    list_of_ids_and_asymmetries = get_list_of_ids_and_total_symmetries(subjects_data)
    cos_sim = get_cosine_similarity(list_of_euclidean_distances)

    outputs = {
        OUTPUT_KEYS['OP1']: list_of_facial_asymmetries,
        OUTPUT_KEYS['OP2']: list_of_euclidean_distances,
        OUTPUT_KEYS['OP3']: list_of_ids_and_asymmetries[:5],
        OUTPUT_KEYS['OP4']: cos_sim
    }

    return outputs['OP1'], outputs['OP2'], outputs['OP3'], outputs['OP4']


def get_list_of_ids_and_total_symmetries(subjects_data):
    """
    :param subjects_data: dictionary of the form
        {
        "SUBJID": {
            "LANDMARK": {
                  "ORIGINAL": {
                    "X": <OX_VALUE>,
                    "Y": <OY_VALUE>,
                    "Z": <OZ_VALUE>
                  },
                  "MIRROR": {
                    "X": <MX_VALUE>,
                    "Y": <MY_VALUE>,
                    "Z": <MZ_VALUE>
                  }
                }
            }, ...
        }
    :return: list of tuple of the with id and total asymmetries
            [("SUBJ_ID", sum_of_asymmetries_of_landmarks), ...]
    """
    total_subject_ids = subjects_data.keys()
    ids_and_asymmetries = []

    for sub_id in total_subject_ids:

        sub_data = subjects_data[sub_id]
        sub_asymmetries = get_facial_asymmetries_for_id(sub_data)

        if sub_asymmetries is not None:
            ids_and_asymmetries.append((sub_id, sum_of_asymmetries(sub_asymmetries)))

    ids_and_asymmetries.sort(key=lambda x: x[1])

    return ids_and_asymmetries


def sum_of_asymmetries(sub_asymmetries):
    """

    :param sub_asymmetries: dictionary with landmark as keys of the form
            {
                'LANDMARK_1': <LANDMARK_1_VALUE>,
                'LANDMARK_2': <LANDMARK_2_VALUE>, ...
            }
    :return: sum of asymmetries i.e. <LANDMARK_1_VALUE> + <LANDMARK_2_VALUES> + ...
    """
    total = 0

    for landmark in sub_asymmetries.keys():
        total = total + sub_asymmetries[landmark]

    return round(total, 4)


def get_list_of_euclidean_distances(subj_ids, subjects_data):
    """

    :param subj_ids: dictionary of input ids of form {'SUB_1': <id1>, 'SUB_2': <id2>}
    :param subjects_data: dictionary with ids and their landmarks
    :return: list of dictionaries with euclidean distances calculated for given facial landmarks in Table 2
    """
    total_subject_ids = subjects_data.keys()

    list_of_euclidean_distances = []

    for sub_id in subj_ids:
        if subj_ids[sub_id] in total_subject_ids:
            sub_data = subjects_data[subj_ids[sub_id]]
            sub_distances = get_euclidean_distances_for_id(sub_data)
            list_of_euclidean_distances.append(sub_distances)
        else:
            list_of_euclidean_distances.append(None)

    return list_of_euclidean_distances


def get_euclidean_distances_for_id(sub_data):
    """
    :param sub_data: landmark data for a subject of the form
                    {
                    'LANDMARK_1': {
                        'ORIGINAL: {
                            'X': <OX_value>
                            'Y': <OY_values>
                            'Z': <OZ_values>
                            },
                        'MIRROR: {
                            'X': <MX_value>
                            'Y': <MY_values>
                            'Z': <MZ_values>
                            }
                        }, ...
                    }

    :return: dictionary of form {
                                'EXEN': <distance_between_EX_and_EN>,
                                'ENAL': <distance between EN and AL>,
                                'ALEX': <distance between AL and EX>,
                                'FTSBAL': <distance between FT and SBAL>,
                                'SBALCH': <distance between SBAL and CH>,
                                'CHFT': <distance between CH and FT>
                                }
    """
    euclidean_distances = {}

    for landmark in FACIAL_DISTANCES:
        try:
            euclidean_distances[landmark] = get_euclidean_distance(sub_data[FACIAL_DISTANCES[landmark][1]],
                                                                   sub_data[FACIAL_DISTANCES[landmark][0]])
        except:
            euclidean_distances[landmark] = None

    if None in euclidean_distances.values():
        return None

    return euclidean_distances


def get_list_of_facial_asymmetries(subj_ids, subjects_data):
    """

    :param subj_ids: dictionary of input ids of form {'SUB_1': <id1>, 'SUB_2': <id2>}
    :param subjects_data:  dictionary with ids and their landmarks
    :return: list of dictionary with facial asymmetry across different landmark for given ids
    """
    list_of_facial_asymmetries = []
    total_subject_ids = subjects_data.keys()

    for sub_id in subj_ids:
        if subj_ids[sub_id] in total_subject_ids:
            sub_data = subjects_data[subj_ids[sub_id]]
            sub_asymmetries = get_facial_asymmetries_for_id(sub_data)
            rounded_sub_asymmetries = {}

            for key in sub_asymmetries.keys():
                rounded_sub_asymmetries[key] = round(sub_asymmetries[key], 4)

            list_of_facial_asymmetries.append(rounded_sub_asymmetries)
        else:
            list_of_facial_asymmetries.append(None)

    return list_of_facial_asymmetries


def get_facial_asymmetries_for_id(sub_data):
    """
    :param sub_data: landmark data for a subject of the form
                    {
                    'LANDMARK_1': {
                        'ORIGINAL: {
                            'X': <OX_value>
                            'Y': <OY_values>
                            'Z': <OZ_values>
                            },
                        'MIRROR: {
                            'X': <MX_value>
                            'Y': <MY_values>
                            'Z': <MZ_values>
                            }
                        }, ...
                    }
    :return: dictionary with asymmetry for different landmarks
    """
    landmark_asymmetries = {}
    landmark_asymmetries_except_prn = {}

    for landmark in LANDMARKS.keys():
        if landmark in sub_data.keys():
            landmark_asymmetries[landmark] = get_facial_asymmetry(sub_data[landmark]['MIRROR'],
                                                                  sub_data[landmark]['ORIGINAL'])
        else:
            landmark_asymmetries[landmark] = None

    if None in landmark_asymmetries.values() or landmark_asymmetries['PRN'] != 0:
        return None

    for landmark in OP1_LANDMARKS.keys():
        landmark_asymmetries_except_prn[landmark] = landmark_asymmetries[landmark]

    return landmark_asymmetries_except_prn


def get_facial_asymmetry(original, mirror):
    """

    :param original: original coordinates for the landmark
    :param mirror: mirrored coordinates for landmark
    :return: facial asymmetry for a landmark
    """
    try:
        facial_sum_of_squares = (square(mirror['X'] - original['X']) +
                                 square(mirror['Y'] - original['Y']) +
                                 square(mirror['Z'] - original['Z']))

        return square_root(facial_sum_of_squares)

    except:
        return None


def get_euclidean_distance(landmark1, landmark2):
    """

    :param landmark1: original data for landmark 1
    :param landmark2: original data for landmark 2
    :return: euclidean distance between landmark 1 and landmark 2
    """
    try:
        sum_of_squares_of_distances = (square(landmark2['ORIGINAL']['X'] - landmark1['ORIGINAL']['X']) +
                                       square(landmark2['ORIGINAL']['Y'] - landmark1['ORIGINAL']['Y']) +
                                       square(landmark2['ORIGINAL']['Z'] - landmark1['ORIGINAL']['Z']))

        return round(square_root(sum_of_squares_of_distances), 4)

    except:
        return None


def square(num):
    return num ** 2


def square_root(num):
    return num ** 0.5


def extract_sub_ids(SubjIDs):
    """

    :param SubjIDs: list of subject ids e.g. [id1, id2]
    :return: dictionary of form {
                                'SUB_1': id1,
                                'SUB_2': id2
                                }
    """
    if not SubjIDs or not isinstance(SubjIDs, list):
        print("Invalid Input. Expected list of string.")

        return {
            'SUB_1': None,
            'SUB_2': None
        }

    return {
        'SUB_1': str(SubjIDs[0]).upper() if (len(SubjIDs) >= 1) else None,
        'SUB_2': str(SubjIDs[1]).upper() if (len(SubjIDs) >= 2) else None
    }


def extract_raw_data(csvfile):
    """

    :param csvfile: a file which contains the data
    :return: list of raw data extracted from given csvfile
    """
    try:
        with open(csvfile, mode='r', encoding='utf-8') as file:
            raw_data = file.read().strip()

            if is_blank(raw_data):
                print(f'File {csvfile} is empty')
                return None

            raw_rows = raw_data.split('\n')

            if len(raw_rows) <= 1:
                return None

            return raw_rows

    except FileNotFoundError:
        print(f'File {csvfile} not found.')
        return None

    except PermissionError:
        print(f'You do not have permission to read the {csvfile} file.')
        return None

    except:
        print(f'Something went wrong. You cannot read/open the {csvfile} file.')
        return None


def get_valid_input(data):
    try:
        numeric_data = float(data)

        if -200 <= numeric_data <= 200:
            return numeric_data
        else:
            return None
    except ValueError or TypeError:
        return None
    except:
        return None


def get_column_indices(row_headers):
    return {
        'SUB_ID_INDEX': row_headers.index(COLUMN_NAMES['SUB_ID']) if (
                COLUMN_NAMES['SUB_ID'] in row_headers) else None,

        'LANDMARK_INDEX': row_headers.index(COLUMN_NAMES['LANDMARK']) if (
                COLUMN_NAMES['LANDMARK'] in row_headers) else None,

        'OX_INDEX': row_headers.index(COLUMN_NAMES['OX']) if (
                COLUMN_NAMES['OX'] in row_headers) else None,

        'OY_INDEX': row_headers.index(COLUMN_NAMES['OY']) if (
                COLUMN_NAMES['OY'] in row_headers) else None,

        'OZ_INDEX': row_headers.index(COLUMN_NAMES['OZ']) if (
                COLUMN_NAMES['OZ'] in row_headers) else None,

        'MX_INDEX': row_headers.index(COLUMN_NAMES['MX']) if (
                COLUMN_NAMES['MX'] in row_headers) else None,

        'MY_INDEX': row_headers.index(COLUMN_NAMES['MY']) if (
                COLUMN_NAMES['MY'] in row_headers) else None,

        'MZ_INDEX': row_headers.index(COLUMN_NAMES['MZ']) if (
                COLUMN_NAMES['MZ'] in row_headers) else None
    }


def get_processed_rows(row_headers, raw_data_rows):
    processed_rows = []

    for raw_row_as_string in raw_data_rows:
        row_dict = get_processed_row(row_headers, raw_row_as_string)

        processed_rows.append(row_dict)

    return processed_rows


def get_processed_row(row_headers, raw_row_as_string):
    row = raw_row_as_string.split(',')
    COLUMN_INDICES = get_column_indices(row_headers)

    return {
        COLUMN_NAMES['SUB_ID']: row[COLUMN_INDICES['SUB_ID_INDEX']].upper(),
        COLUMN_NAMES['LANDMARK']: row[COLUMN_INDICES['LANDMARK_INDEX']].upper(),
        COLUMN_NAMES['OX']: get_valid_input(row[COLUMN_INDICES['OX_INDEX']]),
        COLUMN_NAMES['OY']: get_valid_input(row[COLUMN_INDICES['OY_INDEX']]),
        COLUMN_NAMES['OZ']: get_valid_input(row[COLUMN_INDICES['OZ_INDEX']]),
        COLUMN_NAMES['MX']: get_valid_input(row[COLUMN_INDICES['MX_INDEX']]),
        COLUMN_NAMES['MY']: get_valid_input(row[COLUMN_INDICES['MY_INDEX']]),
        COLUMN_NAMES['MZ']: get_valid_input(row[COLUMN_INDICES['MZ_INDEX']])
    }


def is_blank(string):
    if string and string.strip():
        return False

    return True


def get_subjects_data(processed_rows):
    subjects_data = {}

    for processed_row in processed_rows:
        subjects_data[processed_row['SUBJID']] = subjects_data.get(processed_row['SUBJID'], {})

        subjects_data[processed_row['SUBJID']][LANDMARKS[processed_row['LANDMARK']]] = {
            'ORIGINAL': {
                'X': processed_row['OX'],
                'Y': processed_row['OY'],
                'Z': processed_row['OZ']
            },
            'MIRROR': {
                'X': processed_row['MX'],
                'Y': processed_row['MY'],
                'Z': processed_row['MZ']
            }
        }

    return subjects_data


def get_cosine_similarity(list_of_euclidean_distances):
    if None in list_of_euclidean_distances:
        return None

    SUB_1 = list_of_euclidean_distances[0]
    SUB_2 = list_of_euclidean_distances[1]

    sum_of_products = 0
    sub1_sum_of_squares = sum_of_squares(SUB_1.values())
    sub2_sum_of_squares = sum_of_squares(SUB_2.values())

    for key in SUB_1.keys():
        sum_of_products = sum_of_products + SUB_1[key] * SUB_2[key]

    if sub1_sum_of_squares == 0 or sub2_sum_of_squares == 0:
        return 0

    cos_sim = sum_of_products / (
            square_root(sub1_sum_of_squares) * square_root(sub2_sum_of_squares))

    return round(cos_sim, 4)


def sum_of_squares(data_list):
    total_sum = 0
    for item in data_list:
        total_sum = total_sum + item ** 2

    return total_sum
