# Author Name: Pritam Suwal Shrestha (23771397)
# Date: 14 September, 2022
# CITS1401: Computational Thinking with Python Project 1 Semester 2 2022

"""
This program analyses eight geodesic (surface) and eight 3D Euclidian distances between
a few facial landmarks across four expressions 'Neutral', 'Angry', 'Disgust', 'Happy'.

These distances on one face (in Neutral expression) is used to calculate similarity with
the same face in different expressions or with other faces in the data set to see which faces
are closer to (or look like) the reference face.

Sample Data in file:
+--------------+--------------+---------+---------------+-----------------+
| Adult ID     | Expression  | Distance |     GDis      |  LDis           |
+--------------+-------------+----------+---------------+-----------------+
|   E001       |   Neutral   |    1     |  48.44795743  | 32.13047933     |
+--------------+-------------+----------+---------------+-----------------+

"""


def create_expression_row(expression_row):
    """
    :param expression_row: [<id>, <expression>, <distance_name>, <geodesic_distance>, <euclidean_distance>]
    :return: {
             "id": <id>,
             "expression": <expression>,
             "distance": <distance_name>,
             "g_dis": <geodesic_distance>,
             "l_dis": <euclidean_distance>
             }
    """
    REPLACE_VALUE = 50

    if float(expression_row[3]) >= 0:
        g_dis = float(expression_row[3])
    else:
        g_dis = REPLACE_VALUE

    if float(expression_row[4]) >= 0:
        l_dis = float(expression_row[4])
    else:
        l_dis = REPLACE_VALUE

    return {
        "id": expression_row[0],
        "expression": expression_row[1].upper(),
        "distance": int(expression_row[2]),
        "g_dis": g_dis,
        "l_dis": l_dis
    }


def create_expression_rows(csv_expression_rows):
    """
    :param csv_expression_rows: [<id>, <expression>, <distance_name>, <geodesic_distance>, <euclidean_distance>]
    :return: [{
             "id": <id>,
             "expression": <expression>,
             "distance": <distance_name>,
             "g_dis": <geodesic_distance>,
             "l_dis": <euclidean_distance>
             }]
    """
    expression_rows = []

    for row in csv_expression_rows:
        expression_row = row.split(',')
        expression_row_obj = create_expression_row(expression_row)
        expression_rows.append(expression_row_obj)

    return expression_rows


def find_expression_rows_for_id(adultID, expression_rows):
    """
    :param adultID:
    :param expression_rows:
    :return:
    """
    expression_rows_for_id = []

    for expression_group in expression_rows:
        for expression_row in expression_group:
            if expression_row['id'] == adultID:
                expression_rows_for_id.append(expression_row)

    return expression_rows_for_id


def list_of_distances_for_distance_name(distance_name, distance_type, grouped_expression_rows_for_id):
    """
    :param distance_name: 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8
    :param distance_type: GDis | LDis
    :param grouped_expression_rows_for_id:
    :return: list_of_distance
    """
    list_of_distance_across_expressions = []

    for item in grouped_expression_rows_for_id:
        if item['distance'] == distance_name:
            list_of_distance_across_expressions.append(item[distance_type])

    return list_of_distance_across_expressions


def min_max_distances_for_each_distance_name(distance_name, grouped_expression_rows_for_id):
    """
    :param distance_name:
    :param grouped_expression_rows_for_id:
    :return: This function returns list of minimum and maximum geodesic distances and euclidean distances in the format
             [min gdis, max gdis, min ldis, max ldis]
    """
    gdis_distances_for_distance_name = list_of_distances_for_distance_name(
        distance_name, 'g_dis', grouped_expression_rows_for_id
    )

    ldis_distances_for_distance_name = list_of_distances_for_distance_name(
        distance_name, 'l_dis', grouped_expression_rows_for_id
    )

    min_gdis = round(min(gdis_distances_for_distance_name), 4)
    max_gdis = round(max(gdis_distances_for_distance_name), 4)
    min_ldis = round(min(ldis_distances_for_distance_name), 4)
    max_ldis = round(max(ldis_distances_for_distance_name), 4)

    return [min_gdis, max_gdis, min_ldis, max_ldis]


def list_of_min_max_distances(grouped_expression_rows_for_id):
    """
    :param grouped_expression_rows_for_id:
    :return: It returns list of lists containing the minimum (non-zero) and
    maximum GDis and LDis of each distance across the four expressions. For example, the minimum (non-zero)
    intercanthal width (geodesic and 3D Euclidean) in Neutral, Angry, Disgust and Happy expressions. There will be 8
    lists inside the main list and each list will have four elements in the order :
    [[min gdis, max gdis, min ldis, max ldis]]
    """
    min_max_distance_list = []

    for i in range(1, 9):
        min_max_distances_for_distance_name = min_max_distances_for_each_distance_name(i,
                                                                                       grouped_expression_rows_for_id)
        min_max_distance_list.append(min_max_distances_for_distance_name)

    return min_max_distance_list


def list_of_distance_difference_for_expression(expressions_type, grouped_expression_rows_for_id):
    """
    :param expressions_type:
    :param grouped_expression_rows_for_id:
    :return: It returns list containing the difference between the geodesic and 3D Euclidean distances.
    """

    distance_difference_for_exp = []

    for expression_row in grouped_expression_rows_for_id:
        if expression_row['expression'] == expressions_type:
            difference = round(expression_row['g_dis'] - expression_row['l_dis'], 4)
            distance_difference_for_exp.append(difference)

    return distance_difference_for_exp


def list_of_distance_difference_for_all_expressions(grouped_expression_rows_for_id):
    """
    :param grouped_expression_rows_for_id:
    :return: It returns list of lists containing the difference between the geodesic and 3D Euclidean distances for each
            expression. There will be 4 lists inside the main list and each list will have eight elements.
    """
    distance_difference_for_all_expressions = []

    expressions = ['NEUTRAL', 'ANGRY', 'DISGUST', 'HAPPY']

    for expression in expressions:
        distance_difference_for_exp = list_of_distance_difference_for_expression(expression,
                                                                                 grouped_expression_rows_for_id)
        distance_difference_for_all_expressions.append(distance_difference_for_exp)

    return distance_difference_for_all_expressions


def average_of_list(data_list):
    """
    :param data_list:
    :return: Average of the list
    """
    if len(data_list) == 0:
        return 0

    total_sum = sum(data_list)
    average = total_sum / len(data_list)

    return round(average, 4)


def list_of_average_gdis_distances(grouped_expression_rows_for_id):
    """
    :param grouped_expression_rows_for_id:
    :return: A list containing the average geodesic distance of the eight distances across the four expressions.
            This list will have 8 elements.
    """
    average_gdis_distances = []

    for i in range(1, 9):
        gdis_distances_for_distance_name = list_of_distances_for_distance_name(i, 'g_dis',
                                                                               grouped_expression_rows_for_id)
        average_gdis_distance_for_distance_name = average_of_list(gdis_distances_for_distance_name)
        average_gdis_distances.append(average_gdis_distance_for_distance_name)

    return average_gdis_distances


def standard_deviation_of_list(list_of_distances):
    """
    :param list_of_distances:
    :return: standard deviation of list
    """
    if len(list_of_distances) == 0:
        return 0

    sum_of_squared_diff = 0

    average_ldis_distance_for_distance_name = average_of_list(list_of_distances)

    for distance in list_of_distances:
        squared_diff = (distance - average_ldis_distance_for_distance_name) ** 2
        sum_of_squared_diff += squared_diff

    standard_deviation_of_ldis_distances = round((sum_of_squared_diff / len(list_of_distances)) ** (1 / 2), 4)

    return standard_deviation_of_ldis_distances


def list_of_standard_deviation_for_distance_name(grouped_expression_rows_for_id):
    """
    :param grouped_expression_rows_for_id
    :return: A list containing the standard deviation of the 3D Euclidean distance of the eight distances across
            the four expressions. This list will have 8 elements.
    """
    standard_deviations_of_ldis_distances_for_distance_name = []

    for i in range(1, 9):
        ldis_distances_for_distance_name = list_of_distances_for_distance_name(i, 'l_dis',
                                                                               grouped_expression_rows_for_id)
        standard_deviation_of_ldis_distances_for_distance_name = standard_deviation_of_list(
            ldis_distances_for_distance_name)
        standard_deviations_of_ldis_distances_for_distance_name.append(
            standard_deviation_of_ldis_distances_for_distance_name)

    return standard_deviations_of_ldis_distances_for_distance_name


def list_of_neutral_expression_rows_for_id(adultID, expression_rows):
    neutral_expression_rows = []

    for expression_group in expression_rows:
        for expression_row in expression_group:
            if expression_row['id'] == adultID and expression_row['expression'] == 'NEUTRAL':
                neutral_expression_rows.append(expression_row)

    return neutral_expression_rows


def list_of_non_neutral_expression_rows_for_id(adultID, expression_rows):
    remaining_expression_rows = []

    for expression_group in expression_rows:
        for expression_row in expression_group:
            if expression_row['id'] == adultID and expression_row['expression'] != 'NEUTRAL':
                remaining_expression_rows.append(expression_row)

    return remaining_expression_rows


def list_of_neutral_expression_rows_for_non_selected_ids(adultID, grouped_expression_rows):
    neutral_expression_rows_for_non_selected_ids = []

    for expression_group in grouped_expression_rows:
        for expression_row in expression_group:
            if expression_row['id'] != adultID and expression_row['expression'] == 'NEUTRAL':
                neutral_expression_rows_for_non_selected_ids.append(expression_row)

    return neutral_expression_rows_for_non_selected_ids


def group_by_id_and_exp_type(expressions_rows):
    sorted_expression_rows = []
    counter = 1

    for i in range(0, len(expressions_rows), 8):
        sorted_grouped_expression_rows = sort_group_by_distance_name((expressions_rows[i: 8 * counter]))
        sorted_expression_rows.append(sorted_grouped_expression_rows)

        counter = counter + 1

    return sorted_expression_rows


def sort_group_by_distance_name(grouped_expression_rows):
    sorted_grouped_expression_rows = []

    for i in range(1, len(grouped_expression_rows) + 1):
        for item in grouped_expression_rows:
            if item['distance'] == i:
                sorted_grouped_expression_rows.append(item)

    return sorted_grouped_expression_rows


def list_of_gdis_distances(expression_rows):
    geodesic_distances = []

    for item in expression_rows:
        geodesic_distances.append(item['g_dis'])

    return geodesic_distances


def sum_of_squares(data_list):
    """
    :param data_list:
    :return: sum of squares
    """
    total_sum = 0
    for item in data_list:
        total_sum = total_sum + item ** 2

    return total_sum


def square_root(num):
    return num ** (1 / 2)


def cosine_similarity(neutral_distances, exp_gdis_distances):
    sum_of_products = 0
    sum_of_squares_of_neutral_distances = sum_of_squares(neutral_distances)
    sum_of_squares_of_exp_gdis_distances = sum_of_squares(exp_gdis_distances)

    for i in range(len(neutral_distances)):
        sum_of_products = sum_of_products + neutral_distances[i] * exp_gdis_distances[i]

    if sum_of_squares_of_exp_gdis_distances == 0 or sum_of_squares_of_exp_gdis_distances == 0:
        return 0

    cos_sim = sum_of_products / (
                square_root(sum_of_squares_of_neutral_distances) * square_root(sum_of_squares_of_exp_gdis_distances))

    return round(cos_sim, 4)


def list_of_ids_and_cos_sim(neutral_expression_rows_for_id, expression_rows_for_comparison):
    counter = 1
    ids_and_cosine_similarity = []
    neutral_distances_for_id = list_of_gdis_distances(neutral_expression_rows_for_id)

    for i in range(0, len(expression_rows_for_comparison), 8):
        grouped_expression_rows_with_same_id_and_expression = expression_rows_for_comparison[i: 8 * counter]
        current_id = grouped_expression_rows_with_same_id_and_expression[0]['id']

        gdis_distances_for_same_id_and_expression = list_of_gdis_distances(
            grouped_expression_rows_with_same_id_and_expression)
        cos_sim = cosine_similarity(neutral_distances_for_id, gdis_distances_for_same_id_and_expression)

        counter = counter + 1

        ids_and_cosine_similarity.append({'current_id': current_id, "cos_sim": cos_sim})

    return ids_and_cosine_similarity


def max_of_cosine_sim(list_of_cosines):
    max_cossim = 0
    e_id = ''

    for item in list_of_cosines:
        if item['cos_sim'] > max_cossim:
            max_cossim = item['cos_sim']
            e_id = item['current_id']

    return e_id, max_cossim


def main(csvfile, adultID, Option):
    STATS_OPTION = 'STATS'
    FR_OPTION = 'FR'
    NEWLINE = '\n'

    with open(csvfile) as filein:
        raw_data = filein.read()
        csv_expression_rows = raw_data.split(NEWLINE)[1: -1]

    expression_rows = create_expression_rows(csv_expression_rows)
    grouped_expression_rows = group_by_id_and_exp_type(expression_rows)

    if Option.upper() == STATS_OPTION:
        grouped_expression_rows_for_id = find_expression_rows_for_id(adultID, grouped_expression_rows)

        op1 = list_of_min_max_distances(grouped_expression_rows_for_id)
        op2 = list_of_distance_difference_for_all_expressions(grouped_expression_rows_for_id)
        op3 = list_of_average_gdis_distances(grouped_expression_rows_for_id)
        op4 = list_of_standard_deviation_for_distance_name(grouped_expression_rows_for_id)

        return op1, op2, op3, op4

    if Option.upper() == FR_OPTION:
        neutral_expression_rows_for_id = list_of_neutral_expression_rows_for_id(adultID, grouped_expression_rows)
        non_neutral_expression_rows_for_id = list_of_non_neutral_expression_rows_for_id(adultID,
                                                                                        grouped_expression_rows)
        neutral_expression_rows_for_non_selected_ids = list_of_neutral_expression_rows_for_non_selected_ids(adultID,
                                                                                                            grouped_expression_rows)

        expression_rows_for_comparison = non_neutral_expression_rows_for_id + neutral_expression_rows_for_non_selected_ids

        list_of_gdis_cosine_sims = list_of_ids_and_cos_sim(neutral_expression_rows_for_id,
                                                           expression_rows_for_comparison)
        e_id, cosim = max_of_cosine_sim(list_of_gdis_cosine_sims)

        return e_id, cosim
