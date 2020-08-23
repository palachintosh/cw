import copy

def manhattan_distance(wires_coordinates):

    general_array = [[], []]

    segment_map = {'from': {'x': 0, 'y': 0}, 'to': {'x': 0, 'y': 0}}
    temp_dict = []

    counter = 0
    for string_mass in wires_coordinates:
        
        segment_x = 0
        segment_y = 0
        position = dict.fromkeys(['x', 'y'], 0)
        
        start_segment = dict.fromkeys(['x', 'y'], 0)

        for elem in string_mass:
            elem_index = int(elem.replace(elem[0], ''))

            if elem[0] == "U":
                segment_y += elem_index

            if elem[0] == "R":
                segment_x += elem_index

            if elem[0] == "D":
                segment_y -= elem_index

            if elem[0] == "L":
                segment_x -= elem_index


            position.update({
                'x': segment_x,
                'y': segment_y,
            })


            segment_map.update({
                'from': start_segment,
                'to': position,
            })

            temp_dict.append(segment_map['from'].copy())
            temp_dict.append(segment_map['to'].copy())

            if segment_map['from'].get('x') == segment_map['to'].get('x'):
                temp_dict.append(abs(segment_map['from'].get('y') - segment_map['to'].get('y')))
            else:
                temp_dict.append(abs(segment_map['from'].get('x') - segment_map['to'].get('x')))


            general_array[counter].append(temp_dict.copy())

            temp_dict.clear()
           
            start_segment.update({
                'x': position['x'],
                'y': position['y'],
            })

        counter += 1

    distance = 0
    curent_lengt = 0
    curent_lengt2 = 0
    vector_length = []
    

    for i in range(0, len(general_array[0])):
        curent_lengt2 += general_array[0][i][2]
        curent_lengt = 0


        for j in range(0, len(general_array[1])):
            curent_lengt += general_array[1][j][2]
            
            if general_array[0][i][0].get('x') == general_array[0][i][1].get('x'):
                vertical = general_array[0][i]
                horizontal = general_array[1][j]

            if general_array[1][j][0].get('x') == general_array[1][j][1].get('x'):
                vertical = general_array[1][j]
                horizontal = general_array[0][i]
            
            if general_array[0][i][0].get('y') == general_array[0][i][1].get('y') and general_array[1][j][0].get('y') == general_array[1][j][1].get('y'):
                continue

            minX = min(horizontal[0].get('x'), horizontal[1].get('x'))
            maxX = max(horizontal[0].get('x'), horizontal[1].get('x'))

            minY = min(vertical[0].get('y'), vertical[1].get('y'))
            maxY = max(vertical[0].get('y'), vertical[1].get('y'))


            if (minX <= vertical[0].get('x') and vertical[0].get('x') <= maxX) and (minY <= horizontal[0].get('y') and horizontal[0].get('y') <= maxY):
                if abs(vertical[0].get('x')) + abs(horizontal[0].get('y')) != 0:
                
                    if distance == 0:
                        distance = abs(vertical[0].get('x')) + abs(horizontal[0].get('y'))
                        
                    if distance > abs(vertical[0].get('x')) + abs(horizontal[0].get('y')):
                        distance = abs(vertical[0].get('x')) + abs(horizontal[0].get('y'))
                        

                    temp = curent_lengt2 + curent_lengt
                    sector_length = abs(vertical[1].get('y') - horizontal[0].get('y'))
                    sector_length2 = abs(horizontal[1].get('x') - vertical[1].get('x'))
                    total = abs(sector_length2 + sector_length)
                    vector_length.append(temp - total)

    print("The manhattan distance is: ", distance)
    print("The minimal length is: ", min(vector_length))


if __name__ == "__main__":
    
    wires_coordinates = []
    
    with open("puzzle_input", "r") as file:
        for i in file:
            wires_coordinates.append(i.split(','))

    manhattan_distance(wires_coordinates)


